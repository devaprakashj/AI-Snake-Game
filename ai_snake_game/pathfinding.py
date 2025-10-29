from collections import deque
from typing import Deque, Dict, List, Optional, Set, Tuple

# Grid is 20x20 cells sized 20 pixels (derived from game), but we don't hardcode counts here.
Coord = Tuple[int, int]


def to_cell(point: Coord, cell_size: int = 20) -> Coord:
    return point[0] // cell_size, point[1] // cell_size


def to_point(cell: Coord, cell_size: int = 20) -> Coord:
    return cell[0] * cell_size, cell[1] * cell_size


def neighbors(cell: Coord) -> List[Coord]:
    x, y = cell
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def in_bounds(cell: Coord, cols: int, rows: int) -> bool:
    return 0 <= cell[0] < cols and 0 <= cell[1] < rows


def reconstruct_path(came_from: Dict[Coord, Coord], start: Coord, goal: Coord) -> List[Coord]:
    path: List[Coord] = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


def bfs_shortest_path(
    start_pt: Coord,
    goal_pt: Coord,
    snake_points: List[Coord],
    width: int,
    height: int,
    cell_size: int = 20,
) -> Optional[List[Coord]]:
    """
    Compute a shortest path from snake head to food using BFS on a grid.

    Obstacles: snake body except the tail (tail moves next step if no food eaten). We conservatively
    allow stepping into the current tail cell as it typically vacates.
    """
    cols = width // cell_size
    rows = height // cell_size

    start = to_cell(start_pt, cell_size)
    goal = to_cell(goal_pt, cell_size)

    # Occupied cells: all snake cells except the last tail segment
    occupied: Set[Coord] = set(to_cell(p, cell_size) for p in snake_points[:-1])

    queue: Deque[Coord] = deque([start])
    came_from: Dict[Coord, Coord] = {}
    visited: Set[Coord] = {start}

    while queue:
        current = queue.popleft()
        if current == goal:
            return [to_point(c, cell_size) for c in reconstruct_path(came_from, start, goal)]

        for nxt in neighbors(current):
            if not in_bounds(nxt, cols, rows):
                continue
            if nxt in visited:
                continue
            if nxt in occupied and nxt != goal:
                continue
            visited.add(nxt)
            came_from[nxt] = current
            queue.append(nxt)

    return None



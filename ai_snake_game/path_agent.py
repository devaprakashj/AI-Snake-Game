from typing import List, Tuple
import numpy as np
from pathfinding import bfs_shortest_path


class PathfindingAgent:
    def __init__(self):
        pass

    def _action_from_next_point(self, current_dir: Tuple[int, int], head: Tuple[int, int], next_pt: Tuple[int, int]):
        """
        Convert desired next absolute point into the relative action format [straight, right, left]
        according to current direction as used by the game.
        """
        # Direction order matches main.py clock_wise
        clock_wise = [(20, 0), (0, 20), (-20, 0), (0, -20)]
        idx = clock_wise.index(current_dir)

        desired_dir = (next_pt[0] - head[0], next_pt[1] - head[1])
        if desired_dir not in clock_wise:
            # Fallback to straight if something is odd
            return [1, 0, 0]

        desired_idx = clock_wise.index(desired_dir)
        if desired_idx == idx:
            return [1, 0, 0]  # straight
        # right turn if desired is next index clockwise
        if desired_idx == (idx + 1) % 4:
            return [0, 1, 0]
        # left turn otherwise (including wrap)
        return [0, 0, 1]

    def get_action(self, game) -> List[int]:
        """
        Decide the next move using BFS pathfinding to the food. If no path is found,
        choose a safe move (prefer straight, then right, then left) that avoids collisions.
        """
        head = game.snake[0]
        path = bfs_shortest_path(
            start_pt=head,
            goal_pt=game.food,
            snake_points=game.snake,
            width=game.w,
            height=game.h,
            cell_size=20,
        )

        if path and len(path) > 0:
            next_pt = path[0]
            return self._action_from_next_point(game.direction, head, next_pt)

        # Fallback: try safe heuristic moves in priority straight -> right -> left
        candidates = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        for action in candidates:
            # simulate one step
            clock_wise = [(20, 0), (0, 20), (-20, 0), (0, -20)]
            idx = clock_wise.index(game.direction)
            if np.array_equal(action, [1, 0, 0]):
                new_dir = clock_wise[idx]
            elif np.array_equal(action, [0, 1, 0]):
                new_dir = clock_wise[(idx + 1) % 4]
            else:
                new_dir = clock_wise[(idx - 1) % 4]
            x, y = head
            nxt = (x + new_dir[0], y + new_dir[1])
            if not game.is_collision(nxt):
                return action

        # If all else fails, go straight
        return [1, 0, 0]



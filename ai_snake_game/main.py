import pygame
import random
import numpy as np
import argparse
from agent import Agent
from utils import plot
from path_agent import PathfindingAgent

pygame.init()

class SnakeGameAI:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('AI Snake')
        self.clock = pygame.time.Clock()
        self.reset()

    def reset(self):
        self.direction = (20, 0)
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self._place_food()
        self.score = 0
        self.frame_iteration = 0

    def _place_food(self):
        x = random.randint(0, (self.w - 20) // 20) * 20
        y = random.randint(0, (self.h - 20) // 20) * 20
        if (x, y) in self.snake:
            return self._place_food()
        return (x, y)

    def is_collision(self, pt=None):
        if pt is None:
            pt = self.snake[0]
        if pt[0] > self.w - 20 or pt[0] < 0 or pt[1] > self.h - 20 or pt[1] < 0:
            return True
        if pt in self.snake[1:]:
            return True
        return False

    def play_step(self, action):
        self.frame_iteration += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        self._move(action)
        self.snake.insert(0, self.head)

        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100 * len(self.snake):
            game_over = True
            reward = -10
            return reward, game_over, self.score

        if self.head == self.food:
            self.score += 1
            reward = 10
            self.food = self._place_food()
        else:
            self.snake.pop()

        self._update_ui()
        self.clock.tick(30)
        return reward, game_over, self.score

    def _move(self, action):
        clock_wise = [(20, 0), (0, 20), (-20, 0), (0, -20)]
        idx = clock_wise.index(self.direction)
        if np.array_equal(action, [1, 0, 0]):
            new_dir = clock_wise[idx]
        elif np.array_equal(action, [0, 1, 0]):
            next_idx = (idx + 1) % 4
            new_dir = clock_wise[next_idx]
        else:  # [0,0,1]
            next_idx = (idx - 1) % 4
            new_dir = clock_wise[next_idx]

        self.direction = new_dir
        x, y = self.snake[0]
        self.head = (x + self.direction[0], y + self.direction[1])

    def _update_ui(self):
        self.display.fill((0, 0, 0))
        for pt in self.snake:
            pygame.draw.rect(self.display, (0, 255, 0), pygame.Rect(pt[0], pt[1], 20, 20))
        pygame.draw.rect(self.display, (255, 0, 0), pygame.Rect(self.food[0], self.food[1], 20, 20))
        pygame.display.flip()


def train():
    plot_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()
    while True:
        state_old = agent.get_state(game)
        final_move = agent.get_action(state_old)
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)
        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.model.save()

            print('Game', agent.n_games, 'Score', score, 'Record:', record)

            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot(plot_scores, mean_score)

def play_pathfinding(speed_fps: int = 15):
    game = SnakeGameAI()
    agent = PathfindingAgent()
    while True:
        action = agent.get_action(game)
        reward, done, score = game.play_step(action)
        if done:
            print('Score', score)
            game.reset()
        # override FPS for path mode if provided
        game.clock.tick(speed_fps)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='AI Snake - Train (RL) or Play with Pathfinding')
    parser.add_argument('--mode', choices=['train', 'path'], default='train', help='Select run mode')
    parser.add_argument('--speed', type=int, default=15, help='FPS speed for path mode')
    args = parser.parse_args()

    if args.mode == 'train':
        train()
    else:
        play_pathfinding(speed_fps=args.speed)

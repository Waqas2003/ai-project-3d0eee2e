import pygame
import sys
import random
import time

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = (1, 0)
        self.food = self.generate_food()

    def generate_food(self):
        x = random.randint(0, SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
        y = random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
        return (x, y)

    def draw_snake(self):
        for pos in self.snake:
            pygame.draw.rect(self.screen, WHITE, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

    def draw_food(self):
        pygame.draw.rect(self.screen, RED, (self.food[0], self.food[1], BLOCK_SIZE, BLOCK_SIZE))

    def move_snake(self):
        head = self.snake[0]
        new_head = (head[0] + self.direction[0] * BLOCK_SIZE, head[1] + self.direction[1] * BLOCK_SIZE)
        self.snake.insert(0, new_head)
        if self.snake[0] == self.food:
            self.food = self.generate_food()
        else:
            self.snake.pop()

    def check_collision(self):
        head = self.snake[0]
        if (head[0] < 0 or head[0] >= SCREEN_WIDTH or
            head[1] < 0 or head[1] >= SCREEN_HEIGHT or
            head in self.snake[1:]):
            return True
        return False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != (0, 1):
                        self.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                        self.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and self.direction != (1, 0):
                        self.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                        self.direction = (1, 0)

            self.move_snake()
            if self.check_collision():
                break

            self.screen.fill(BLACK)
            self.draw_snake()
            self.draw_food()
            pygame.display.flip()
            self.clock.tick(SPEED)

        time.sleep(1)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
import pygame
from .constants import GRID_WIDTH, GRID_HEIGHT, GRID_SIZE, SNAKE_COLOR, SNAKE_HEAD_COLOR

class Snake:
        def __init__(self, x, y):
                self.body = [(x, y)]
                self.direction = [1, 0]
                self.grow = False

        def move(self):
                head = self.body[0]
                new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
                self.body.insert(0, new_head)
                if not self.grow:
                        self.body.pop()
                self.grow = False

        def change_direction(self, new_direction):
                if (new_direction[0] * -1, new_direction[1] * -1) != tuple(self.direction):
                        self.direction = new_direction

        def wrap_around(self):
                head = self.body[0]
                self.body[0] = (
                        head[0] % GRID_WIDTH,
                        head[1] % GRID_HEIGHT
                )

        def check_food_collision(self, food):
                if self.body[0] == food.position:
                        self.grow = True
                        food.position = food.get_random_position()
                        while food.position in self.body:
                                food.position = food.get_random_position()
                        return True
                return False

        def check_self_collision(self):
                return self.body[0] in self.body[1:]

        def draw(self, screen):
                for segment in self.body[1:]:
                        rect = pygame.Rect(
                                segment[0] * GRID_SIZE,
                                segment[1] * GRID_SIZE,
                                GRID_SIZE - 1,
                                GRID_SIZE - 1
                        )
                        pygame.draw.rect(screen, SNAKE_COLOR, rect)
                
                head = self.body[0]
                head_rect = pygame.Rect(
                        head[0] * GRID_SIZE,
                        head[1] * GRID_SIZE,
                        GRID_SIZE - 1,
                        GRID_SIZE - 1
                )
                pygame.draw.rect(screen, SNAKE_HEAD_COLOR, head_rect)
import random
import pygame
from .constants import GRID_WIDTH, GRID_HEIGHT, GRID_SIZE

class Food:
        def __init__(self):
                self.position = self.get_random_position()

        def get_random_position(self) -> tuple:
                return (
                        random.randint(0, GRID_WIDTH - 1),
                        random.randint(0, GRID_HEIGHT - 1)
                )

        def draw(self, screen: pygame.Surface):
                rect = pygame.Rect(
                        self.position[0] * GRID_SIZE,
                        self.position[1] * GRID_SIZE,
                        GRID_SIZE - 1,
                        GRID_SIZE - 1
                )
                pygame.draw.rect(screen, (255, 0, 0), rect)
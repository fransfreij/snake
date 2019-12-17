"""
Apple will be eaten by snake and spawn at random locations
"""

import pygame
import random
from constants import *


print(constants['WIDTH'])


class Apple:
    def __init__(self):
        self.alive = False
        self.apple_size = 10

    def random_position(self):
        pos = []  # clean the pos
        x = random.randint(0, constants['WIDTH'])
        y = random.randint(0, constants['HEIGHT'])
        pos.append(x)
        pos.append(y)
        return pos

    def on_collide(self):
        pass

    def create_apple(self):
        pos = self.random_position()
        self.apple = pygame.Rect(
            pos[0], pos[1], self.apple_size, self.apple_size)
        self.alive = True

    def draw(self, window):
        if not self.apple:
            print("no apple object")

        if self.alive:
            pygame.draw.rect(window, constants['RED'], self.apple)

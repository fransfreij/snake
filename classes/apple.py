#!/usr/bin/env python

import pygame
import random
from constants import *


class Apple:
    def __init__(self):
        self.apple_size = 10

    def random_position(self):
        pos = []  # clean the pos
        x = random.randint((0 + self.apple_size + 5), (constants['GAME_WIDTH'] - (self.apple_size - 5)))
        y = random.randint((0 + self.apple_size + 5), (constants['GAME_HEIGHT'] - (self.apple_size + 5)))
        pos.append(x)
        pos.append(y)
        return pos

    def create_apple(self):
        pos = self.random_position()
        self.apple = pygame.Rect(pos[0], pos[1], self.apple_size, self.apple_size)
        self.alive = True

    def draw(self, window):
        pygame.draw.rect(window, constants['RED'], self.apple)

    def get_rect(self):
        return self.apple

    def get_pos_x(self):
        return self.apple.x

    def get_pos_y(self):
        return self.apple.y

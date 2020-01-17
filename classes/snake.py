#!/usr/bin/env python

import pygame
from constants import *

LEFT = "LEFT"
RIGHT = "RIGHT"
UP = "UP"
DOWN = "DOWN"


class Snake:
    def __init__(self, x, y):
        self.start_x = x
        self.start_y = y
        self.snake_list = []
        self.is_alive = True
        self.reset()

    def draw(self, window):
        for snake in self.snake_list:
            pygame.draw.rect(window, constants['GREEN'], snake)

    def reset(self):
        self.snake_list = []
        self.direction = 'LEFT'

        for i in range(0, 4):
            self.snake_list.append((self.start_x, self.start_y + i))

    def change_direction(self, direction):
        if self.direction == "UP" and direction == "DOWN":
            return

        if self.direction == "DOWN" and direction == "UP":
            return

        if self.direction == "LEFT" and direction == "RIGHT":
            return

        if self.direction == "RIGHT" and direction == "LEFT":
            return

        self.direction = direction

    def get_head(self):
        return self.snake_list[0]

    def get_tail(self):
        return self.snake_list[len(self.snake_list)-1]

    def grow(self):
        (tx, ty) = self.get_tail()
        tail = ()
        print(tail)

    def is_alive(self):
        return is_alive

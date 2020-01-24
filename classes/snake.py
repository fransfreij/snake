#!/usr/bin/env python

import pygame
from constants import *

LEFT = "LEFT"
RIGHT = "RIGHT"
UP = "UP"
DOWN = "DOWN"


class Snake:
    def __init__(self):
        self.next_direction = None
        self.direction = "RIGHT"
        self.snake_pos = [100, 50]  # x y
        self.snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
        self.score = 0

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.next_direction = "UP"

            if event.key == pygame.K_DOWN:
                self.next_direction = "DOWN"

            if event.key == pygame.K_LEFT:
                self.next_direction = "LEFT"

            if event.key == pygame.K_RIGHT:
                self.next_direction = "RIGHT"

    def update(self):
        if self.next_direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'

        if self.next_direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'

        if self.next_direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'

        if self.next_direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        if self.direction == 'UP':
            self.snake_pos[1] -= 5

        if self.direction == 'DOWN':
            self.snake_pos[1] += 5

        if self.direction == 'LEFT':
            self.snake_pos[0] -= 5

        if self.direction == 'RIGHT':
            self.snake_pos[0] += 5

    def grow(self):
        self.snake_body.insert(0, list(self.snake_pos))

    def delete_tail(self):
        # remove the last element of the tail
        self.snake_body.pop()

    def draw(self, window):
        for pos in self.snake_body:
            pygame.draw.rect(window, constants['GREEN'], pygame.Rect(
                pos[0], pos[1], 10, 10))

    def get_pos_x(self):
        return self.snake_pos[0]

    def get_pos_y(self):
        return self.snake_pos[1]

    def get_rect(self):
        head = pygame.Rect(
            int(self.snake_pos[0]), int(self.snake_pos[1]), 10, 10)

        return head

    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score

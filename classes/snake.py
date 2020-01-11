#!/usr/bin/env python

import pygame
from constants import *


class Snake:
    def __init__(self):
        self.alive = False
        self.current_direction = None
        self.health = 50
        self.right = 1
        self.left = 0
        self.up = 0
        self.down = 0
        self.snake_size = 60

        self.snake_list = []

    def draw(self, window):
        for snake in self.snake_list:
            pygame.draw.rect(window, constants['GREEN'], snake)

    def create_snake(self):
        self.snake = pygame.Rect(0, 0, self.snake_size, self.snake_size)
        self.alive = True
        self.snake_list.insert(0, self.snake)

    def on_collide(self, apple):
        for snake in self.snake_list:
            if snake.colliderect(apple.get_rect()):
                return True

    def increase_size(self):

        current_snake_pos = []
        current_snake_pos.append(self.snake_list[0].x)
        current_snake_pos.append(self.snake_list[0].y)
        print(current_snake_pos)

        test = pygame.Rect(
            current_snake_pos[0], current_snake_pos[1], self.snake_size, self.snake_size)
        self.snake_list.insert(len(self.snake_list), test)

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.direction_state(0, 1, 0, 0)
                self.current_direction = "LEFT"

            if event.key == pygame.K_RIGHT:
                self.direction_state(1, 0, 0, 0)
                self.current_direction = "RIGHT"

            if event.key == pygame.K_UP:
                self.direction_state(0, 0, 1, 0)
                self.current_direction = "UP"

            if event.key == pygame.K_DOWN:
                self.direction_state(0, 0, 0, 1)
                self.current_direction = "DOWN"

    def update(self):
        if self.left == 1:
            for snake in self.snake_list:
                if snake.x < 0:
                    self.health = 0
                snake.x -= 4
            """
            if self.snake.x < 0:
                self.health = 0
                print("Hit left wall")
            self.snake.x -= 4
            """

        if self.right == 1:
            for snake in self.snake_list:
                if snake.x >= constants['WIDTH'] - self.snake_size:

                    self.health = 0
                    print("Hit right wall")
                snake.x += 4

        if self.up == 1:
            if self.snake.y <= -(self.snake_size):
                self.health = 0
                print("Hit upper wall")
            self.snake.y -= 4

        if self.down == 1:
            if self.snake.y >= constants['HEIGHT'] - self.snake_size:
                self.health = 0
                print("Hit lower wall")
            self.snake.y += 4

        print(self.current_direction)

    def do_damage(self, damage):
        self.health = self.health - damage

    def is_alive(self):
        if self.health <= 0:
            self.alive = False

        return self.alive

    def direction_state(self, right, left, up, down):
        self.right = right
        self.left = left
        self.up = up
        self.down = down

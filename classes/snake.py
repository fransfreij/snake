#!/usr/bin/env python

import pygame


class Snake():
    def __init__(self):
        self.alive = False
        self.health = 50
        self.right = 1
        self.left = 0
        self.up = 0
        self.down = 0

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), self.snake)

    def create_snake(self):
        self.snake = pygame.Rect(0, 0, 60, 60)
        self.alive = True

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.right = 0
                self.left = 1
                self.up = 0
                self.down = 0

            if event.key == pygame.K_RIGHT:
                self.right = 1
                self.left = 0
                self.up = 0
                self.down = 0

            if event.key == pygame.K_UP:
                self.right = 0
                self.left = 0
                self.up = 1
                self.down = 0

            if event.key == pygame.K_DOWN:
                self.right = 0
                self.left = 0
                self.up = 0
                self.down = 1

    def update(self):
        print(self.snake.y)
        if self.left == 1:
            if self.snake.x < 0:
                self.health = 0
            self.snake.x -= 4

        if self.right == 1:
            if self.snake.x >= 500 - 50:
                self.health = 0
            self.snake.x += 4

        if self.up == 1:
            if self.snake.y <= -50:
                self.health = 0
            self.snake.y -= 4

        if self.down == 1:
            if self.snake.y >= 500 - 50:
                self.health = 0
            self.snake.y += 4

    def do_damage(self, damage):
        self.health = self.health - damage

    def is_alive(self):
        if self.health <= 0:
            self.alive = False

        return self.alive

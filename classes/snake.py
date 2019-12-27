#!/usr/bin/env python

import pygame
from constants import *


class Snake:
    def __init__(self):
        self.alive = False
        self.health = 50
        self.right = 1
        self.left = 0
        self.up = 0
        self.down = 0
        self.snake_size = 60
        self.size = 0
        self.tails = []

    def draw(self, window):
        pygame.draw.rect(window, constants['GREEN'], self.snake)

        for tail in self.tails:
            pygame.draw.rect(window, constants['GREEN'], tail)

    def create_snake(self):
        self.snake = pygame.Rect(0, 0, self.snake_size, self.snake_size)
        self.alive = True

    def on_collide(self, apple):
        if self.snake.colliderect(apple.apple):
            return True

    def increase_size(self):
        self.size += 1
        print(len(self.tails))
        tail = pygame.Rect(self.snake.centerx, self.snake.centery, 20, 20)
        self.tails.append(tail)

        return self.size

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.direction_state(0, 1, 0, 0)

            if event.key == pygame.K_RIGHT:
                self.direction_state(1, 0, 0, 0)

            if event.key == pygame.K_UP:
                self.direction_state(0, 0, 1, 0)

            if event.key == pygame.K_DOWN:
                self.direction_state(0, 0, 0, 1)

    def update(self):
        if self.left == 1:
            if self.snake.x < 0:
                self.health = 0
                print("Hit left wall")
            self.snake.x -= 4

        if self.right == 1:
            if self.snake.x >= constants['WIDTH'] - self.snake_size:
                self.health = 0
                print("Hit right wall")
            self.snake.x += 4

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

        for tail in self.tails:
            tail.x = self.snake.centerx + 30
            tail.y = self.snake.centery

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

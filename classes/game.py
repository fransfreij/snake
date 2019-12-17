#!/usr/bin/env python
import pygame
from constants import *
from classes.snake import Snake
from classes.apple import Apple


class Game:
    def __init__(self, running):
        self.running = running
        self.entities = []
        self.spawn_timer = 5

    def create_window(self):
        try:
            self.window = pygame.display.set_mode(
                [constants['HEIGHT'], constants['WIDTH']])
        except:
            print("Failed to create window...")

    def update_window(self):
        try:
            pygame.display.update()
        except:
            print("Failed to update window...")

    def create_clock(self):
        try:
            self.clock = pygame.time.Clock()
        except:
            print("Failed to create clock...")

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.quit()
            print("User manually exited the game...")

        self.snake.on_event(event)

    def create_snake(self):
        self.snake = Snake()
        self.snake.create_snake()
        self.entities.append(self.snake)

    def create_apple(self):
        self.apple = Apple()
        self.apple.create_apple()
        self.entities.append(self.apple)

    def run(self):
        self.create_clock()
        self.create_window()

        self.create_snake()
        self.create_apple()

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            # a comment
            self.clock.tick(constants['FPS'])
            self.window.fill(constants['BLACK'])

            for entity in self.entities:
                entity.draw(self.window)

            self.snake.update()

            # print(len(self.entities))
            if self.snake.snake.colliderect(self.apple.apple):
                self.apple.alive = False

            if not self.snake.is_alive():
                self.quit()

            if self.clock.get_time() / 1000 >= self.spawn_timer:
                self.create_apple()

            print(self.clock.get_time() / 1000)

            self.update_window()

    def quit(self):
        self.running = False
        pygame.quit()

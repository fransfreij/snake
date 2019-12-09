#!/usr/bin/env python
import pygame
from constants import *
from classes.snake import Snake


class Game():
    def __init__(self, running):
        self.running = running

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

    def run(self):
        self.create_clock()
        self.create_window()

        self.snake = Snake()

        self.snake.create_snake()

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)

            self.clock.tick(constants['FPS'])
            self.window.fill(constants['BLACK'])
            self.snake.draw(self.window)
            self.snake.update()
            if not self.snake.is_alive():
                self.quit()

            self.update_window()

    def quit(self):
        self.running = False
        pygame.quit()

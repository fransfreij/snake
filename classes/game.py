#!/usr/bin/env python
import pygame
from constants import *
from classes.snake import Snake
from classes.apple import Apple


class Game:
    def __init__(self, running):
        self.running = running
        self.spawn_timer = 5
        self.counter = 0
        self.apples = []

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

    def create_apple(self):
        apple = Apple()
        apple.create_apple()
        self.apples.append(apple)

    def run(self):
        self.create_clock()
        self.create_window()

        self.create_snake()
        self.create_apple()

        while self.running:
            for event in pygame.event.get():
                self.on_event(event)

            self.clock.tick(constants['FPS'])
            self.window.fill(constants['BLACK'])

            # collisions
            for apple in self.apples:
                if self.snake.on_collide(apple):
                    self.apples.remove(apple)
                    self.snake.increase_size()

            # draw
            self.snake.draw(self.window)
            for apple in self.apples:
                apple.draw(self.window)

            # check if snake is alive
            if not self.snake.is_alive():
                print("Game over")
                self.quit()

            # spawn timer logic
            if pygame.time.get_ticks() / 1000 >= self.spawn_timer:
                self.create_apple()
                self.spawn_timer += 5
                self.counter += 1
            # print(pygame.time.get_ticks() / 1000)

            # updates
            self.snake.update()
            self.update_window()

    def quit(self):
        self.running = False
        pygame.quit()

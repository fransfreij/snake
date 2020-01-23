#!/usr/bin/env python
import pygame
from constants import *
from classes.snake import Snake
from classes.apple import Apple


class Game:
    def __init__(self, running):
        pygame.init()
        self.running = running
        self.window_size_x = 500
        self.window_size_y = 500
        self.next_direction = "RIGHT"
        self.apples = []

    def create_window(self):
        pygame.display.set_caption("Snake")
        self.window = pygame.display.set_mode(
            (self.window_size_x, self.window_size_y))

    def create_apple(self):
        apple = Apple()
        apple.create_apple()
        self.apples.append(apple)

    def run(self):
        clock = pygame.time.Clock()
        self.create_window()
        self.snake = Snake()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                self.snake.on_event(event)

            if len(self.apples) <= 0:
                self.create_apple()

            print(self.snake.get_pos_x())

            for apple in self.apples:
                if self.snake.get_pos_x() == apple.get_pos_x() and self.snake.get_pos_y() == apple.get_pos_y():

                    print("hit")
                    self.apples.remove(apple)

            self.snake.update()
            self.snake.draw(self.window)
            for apple in self.apples:
                apple.draw(self.window)

            pygame.display.update()
            clock.tick(60)

#!/usr/bin/env python

import pygame
from constants import *
from classes.snake import Snake
from classes.apple import Apple
from classes.textmanager import Textmanager


class Game:
    def __init__(self, running):
        pygame.init()
        self.running = running
        self.apples = []

    def create_window(self):
        pygame.display.set_caption("Snake")
        self.window = pygame.display.set_mode((constants['GAME_WIDTH'], constants['GAME_HEIGHT']))

    def create_apple(self):
        apple = Apple()
        apple.create_apple()
        self.apples.append(apple)

    def create_snake(self):
        self.snake = Snake()

    def create_textmanager(self):
        self.textmanager = Textmanager()

    def run(self):
        clock = pygame.time.Clock()
        self.create_window()
        self.create_snake()
        self.create_textmanager()

        # game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.snake.on_event(event)

            # we always want a apple on the screen
            if len(self.apples) <= 0:
                self.create_apple()

            # grow the snake
            self.snake.grow()

            # collision detection
            for apple in self.apples:
                if apple.get_rect().colliderect(self.snake.get_rect()):
                    self.apples.remove(apple)
                    self.snake.increase_score()
                else:
                    self.snake.shrink()

            # update the snake movement direction
            self.snake.update()

            # if snake is not alive, quit the game
            if self.snake.get_alive_status() is False:
                self.running = False

            # render score and it's x, y position
            self.textmanager.render_text(self.snake.get_score(), (constants['GAME_WIDTH'] - 40), 0)

            # drawables
            self.window.fill(constants['BLACK'])
            self.snake.draw(self.window)
            self.textmanager.draw(self.window)
            for apple in self.apples:
                apple.draw(self.window)

            # update and fps
            pygame.display.update()
            clock.tick(60)

#!/usr/bin/env python

import pygame
from constants import *


class Textmanager:
    def __init__(self):
        self.font = pygame.font.Font('fonts/arial.ttf', 24)

    def render_text(self, text, x, y):
        text = str(text)
        self.x = x
        self.y = y
        self.rendered_text = self.font.render(text, False, constants['WHITE'])

    def draw(self, window):
        window.blit(self.rendered_text, (self.x, self.y))

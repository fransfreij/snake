#!/usr/bin/env python

import pygame
from classes.game import Game


def main():
    pygame.init()
    game = Game(True)
    game.run()


if __name__ == '__main__':
    main()

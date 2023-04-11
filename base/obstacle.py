import pygame
from pygame.math import Vector2 as vec
from copy import copy
from random import choice, randint 

class Obstacle:
    def __init__(self, bird, pos, index, window_size):
        self.window_size = window_size
        self.pos = pos
        self.index = index
        self.bird = bird
        self.gap = randint(200, 300)
        self.D = randint(self.window_size[1] * 0.3, self.window_size[1] * 0.6)
        self.width = 20
        self.bars = [
            pygame.Rect(self.pos.x, self.pos.y, self.width, self.D),
            pygame.Rect(self.pos.x, self.pos.y + self.D + self.gap, self.width, self.window_size[1] - self.gap - self.D)
        ]
        self.color = (0, 255, 0)
        self.speed = 5

    def show(self, win):
        for bar in self.bars:
            pygame.draw.rect(win, self.color, bar)

    def move(self):
        if self.pos.x < -self.width - 10:
            self.pos = vec(self.window_size[0] + self.window_size[0]//6, 0)
            self.gap = randint(200, 300)
            self.bird.score += 1

        self.pos.x -= self.speed

    def update(self):
        self.bars = [
            pygame.Rect(self.pos.x, self.pos.y, self.width, self.D),
            pygame.Rect(self.pos.x, self.pos.y + self.D + self.gap, self.width, self.window_size[1] - self.gap - self.D)
        ]

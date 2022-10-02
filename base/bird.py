import pygame
from pygame.math import Vector2 as vec

class Bird:
    def __init__(self, pos):
        self.pos = pos
        self.color = (255, 0, 0)
        self.width = 20
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.width)
        self.rect.center = [self.pos.x, self.pos.y]
        self.gravity = 0.3
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.flap_force = 7
        self.score = 0

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.width)
        self.rect.center = [self.pos.x, self.pos.y]

    def show(self, win):
        pygame.draw.rect(win, self.color, self.rect)


    def fall(self):
        self.acc.y = self.gravity

    def flap(self):
        self.vel.y = - self.flap_force

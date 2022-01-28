import pygame
from pygame.math import Vector2
from random import randint as ri

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

fps = pygame.time.Clock()
FPS = 60

g = 0.5

class Bird:
    def __init__(self):
        self.pos = Vector2(300, height/2)
        self.r = 15
        self.vely = 0
        self.jump_force = 4

    def show(self):
        pygame.draw.circle(window, (255, 255, 0), (self.pos.x , self.pos.y), self.r) 

    def update(self):
        self.vely -= g
        self.pos.y -= self.vely
        if self.vely >= self.jump_force:
            self.vely = self.jump_force
        if self.pos.y >= height:
            self.pos.y = height
        if self.pos.y <= 0:
            self.pos.y = 0

    def jump(self):
        self.vely += self.jump_force

bird = Bird()
bars = []
bars_passed = []
game_started = False
score = 0
def text(text, surface, color, pos, size):
    font = pygame.font.SysFont("comicsansms", size)
    text_img = font.render(text, True, color)
    surface.blit(text_img, pos)

def end_screen():
    while True:
        window.fill((0, 0, 0))
        text("You Lost! \n Score : " + str(score), window, (255, 255, 255), (200, 200), 70)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

class Bar:
    def __init__(self):
        self.x = width + 100
        self.pos1 = Vector2(self.x, 0)  
        self.pos2 = Vector2(self.x, ri(100, 300))
        self.pos3 = Vector2(self.x, self.pos2.y + 300)

    def show(self):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.pos1.y, 40, self.pos2.y))
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.pos3.y, 40, height - self.pos3.y))

    def update(self):
        self.x -= 4

def is_collided(bird, bar):
    if bar.x <= bird.pos.x + bird.r and bird.pos.x - bird.r <= bar.x + 40:
        if bird.pos.y - bird.r <= bar.pos2.y or bird.pos.y + bird.r >= bar.pos3.y:
            end_screen()


def render():
    global score
    window.fill((0, 0, 0))
    bird.show()
    bird.update()

    if ri(1, 100) == 1:
        bars.append(Bar())
    
    for bar in bars:
        bar.show()
        bar.update()
        is_collided(bird, bar)
        if bar.x <= bird.pos.x - bird.r:
            bars_passed.append(bar)
            score += 1
            bars.remove(bar)

    for bar in bars_passed:
        bar.show()
        bar.update()
        if bar.x <= -50:
            bars_passed.remove(bar)    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird.jump()

    text("Score:    " + str(score), window, (255, 255, 255), (200, 10), 40)

    pygame.display.update()
    fps.tick(FPS)

def loop():
    global game_started
    while True:
        if game_started:
            render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_started = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

loop()

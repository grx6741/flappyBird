import pygame
from pygame.math import Vector2 as vec
from .bird import Bird
from .obstacle import Obstacle

pygame.init()

class FlappyBird:
    def __init__(self):
        self.width, self.height = 800, 600
        self.window = pygame.display.set_mode((self.width, self.height))
        self.fps = pygame.time.Clock()
        self.FPS = 60
        self.bird = Bird(vec(self.width//2, self.height//2))
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 72)
        self.game_not_over = True
        self.game_paused = False
        self.score = 0
        self.prev_score = self.score
        self.obstacles = [
            Obstacle(
                self.bird,
                vec(self.width + i * self.width//6, 0),
                i,
                [self.width, self.height]
            ) for i in range(6)
        ]

    def update(self):
        self.window.fill((0, 0, 0))
        self.score_img = self.font.render(f"Score : {self.bird.score}", True, (255, 255, 255))
        for obstacle in self.obstacles:
            for bar in obstacle.bars:
                if self.bird.rect.colliderect(bar):
                    self.game_paused = True
        if self.bird.pos.y > self.height - self.bird.width:
            self.game_paused = True
        if not self.game_paused:
            self.bird.fall()
            self.bird.update()
            self.bird.show(self.window)
            for obstacle in self.obstacles:
                obstacle.update()
                obstacle.show(self.window)
                obstacle.move()
            self.window.blit(self.score_img, (0, 0))
        else:
            # for obstacle in self.obstacles:
            #     obstacle.show(self.window)
            # self.bird.show(self.window)
            self.window.fill((0, 0, 0))
            self.end_card = self.font.render("""q - exit; r - restart""", True, (255, 255, 255))
            self.window.blit(self.end_card, (0,0))
            key = pygame.key.get_pressed()
            if key[pygame.K_q]:
                self.game_not_over = False
            if key[pygame.K_r]:
                self.game_not_over = False
                FlappyBird().run()
        pygame.display.update()
        self.fps.tick(self.FPS)

    def run(self):
        while self.game_not_over:
            self.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_not_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.flap()

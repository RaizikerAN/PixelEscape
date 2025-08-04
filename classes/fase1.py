
import pygame
from .player import Player

class Fase1:
    def __init__(self, win):
        self.win = win
        self.player = Player(100, 100)
        self.obstacles = [
            pygame.Rect(300, 200, 100, 100),
            pygame.Rect(500, 400, 100, 100)
        ]
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.move(keys, self.obstacles)

            self.win.fill((30, 30, 30))
            for obs in self.obstacles:
                pygame.draw.rect(self.win, (100, 100, 100), obs)
            self.player.draw(self.win)
            pygame.display.update()
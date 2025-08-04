
import pygame

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.vel = 4
        self.color = (0, 255, 0)

    def move(self, keys, obstacles):
        dx, dy = 0, 0
        if keys[pygame.K_a]: dx -= self.vel
        if keys[pygame.K_d]: dx += self.vel
        if keys[pygame.K_w]: dy -= self.vel
        if keys[pygame.K_s]: dy += self.vel

        self.rect.x += dx
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle):
                self.rect.x -= dx
                break

        self.rect.y += dy
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle):
                self.rect.y -= dy
                break

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

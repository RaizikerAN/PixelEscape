
import pygame
import os

class Menu:
    def __init__(self, win):
        self.win = win
        self.bg = pygame.image.load(os.path.join("assets", "background.png"))
        self.button_play = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "button_play.png")), (300, 100))
        self.button_quit = pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "button_quit.png")), (300, 100))
        self.font = pygame.font.SysFont("Arial", 60)

    def run(self):
        while True:
            self.win.blit(pygame.transform.scale(self.bg, (800, 600)), (0, 0))

            title = self.font.render("Pixel Escape", True, (255, 255, 255))
            self.win.blit(title, (400 - title.get_width() // 2, 50))

            play_rect = self.button_play.get_rect(center=(400, 250))
            quit_rect = self.button_quit.get_rect(center=(400, 400))

            self.win.blit(self.button_play, play_rect.topleft)
            self.win.blit(self.button_quit, quit_rect.topleft)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_rect.collidepoint(event.pos):
                        return "play"
                    if quit_rect.collidepoint(event.pos):
                        return "quit"

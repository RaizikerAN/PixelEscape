# LEIA O README ANTES DE INICIAR, É MUITO IMPORTANTE !!!
import pygame
import sys
from classes.menu import Menu
from classes.fase1 import Fase1

pygame.init()
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Escape")

menu = Menu(win)
fase1 = Fase1(win)

estado_jogo = "menu"
rodando = True
clock = pygame.time.Clock()

while rodando:
    clock.tick(60)
    if estado_jogo == "menu":
        acao = menu.run()
        if acao == "play":
            estado_jogo = "fase1"
        elif acao == "quit":
            rodando = False
    elif estado_jogo == "fase1":
        fase1.run()
pygame.quit()

import pygame, sys, math
pygame.init()

def Window():
    xmax, ymax = (1280, 720)
    win = pygame.display.set_mode((xmax,ymax), pygame.RESIZABLE)
    pygame.display.set_caption("Tank Game")

def ImageDeclaration():
    bg = pygame.image.load('BackGround_test.jpg')
    mouseMoving = pygame.image.load('Crosshair.png')
    playerMoving = pygame.image.load('Tank_test.jpg')
    bulletMoving = pygame.image.load('BetterBullet.png')



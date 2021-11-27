import pygame
import random
import time


black = (0,0,0)
white = (255,255,255)


def text_objects(texto, font):
    textSurface = font.render(texto, True, black)
    return textSurface, textSurface.get_rect()




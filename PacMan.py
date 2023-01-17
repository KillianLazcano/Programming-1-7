import pygame
import random
import math

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 100)
black = (0, 0, 0)
red = (210, 50, 80)
green = (0, 255, 0)
blue = (50, 150, 210)
darkblue = (3, 36, 138)

dis_width = 606
dis_height = 606
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()
pacman = 10
pacspeed = 15
pinky = 10
pinkyspeed = 17
blinky = 10
blinkyspeed = 16
clyde = 10
clydespeed = 16
inky = 10
inkyspeed = 17
pacman.x
pacman.y
font_style = pygame.font.SysFont("sans-serif", 20)

dis.fill(darkblue)

def score(score):
  val = font_style.render("Score: "+ str(score), True, white)
  dis.blit(val, [0,0])

def Pacman(pacman, )

import pygame
import random
import copy
import math

walls = [
  [6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
  [3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3], 
  [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3], 
  [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
  [3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
  [3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
  [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
  [3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
  [3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
  [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
  [3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4 ,4, 4, 8, 3],
  [3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
  [8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
  [4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0 ,0, 0, 0, 0],
  [4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4],
  [5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
  [3, 0, 0, 0, 0 ,0 ,3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
  [3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
  [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
  [3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
  [3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
  [3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
  [3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
  [3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
  [3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
  [3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
  [3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
  [3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
  [3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
  [7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
]
pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 100)
black = (0, 0, 0)
red = (210, 50, 80)
green = (0, 255, 0)
blue = (50, 150, 210)
darkblue = (3, 36, 138)

dis_width = 900
dis_height = 950
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()
fps = 60
font_style = pygame.font.SysFont("sans-serif", 20)
level = walls
PI = math.pi
pacman_images = []
for i in range(1, 3):
  pacman_images.append(pygame.transform.scale(pygame.image.load('images(2).png'), (45, 45)))
pacman_x = 450
pacman_y = 663
direction = 0
counter = 0


def draw_walls():
  num1 = ((dis_height - 50) // 32)
  num2 = (dis_width // 30)
  for i in range(len(level)):
    for j in range(len(level[i])):
      if level[i][j] == 1:
        pygame.draw.circle(dis, white, (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
      if level[1][j] == 2:
        pygame.draw.circle(dis, white, (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)
      if level[i][j] == 3:
        pygame.draw.line(dis, blue, (j * num2 + (0.5 * num2), i*num1),
                        (j + num2 + (0.5 * num2), i*num1 + num1), 3)
      if level[i][j] == 4:
        pygame.draw.line(dis, blue, (j * num2, i*num1 + (0.5*num1)),
                        (j * num2 + num2, i*num1 + (0.5*num1)), 3)
      if level[i][j] == 5:
        pygame.draw.arc(dis, blue, [(j*num2 - (num2*0.4)) - 2, (i * num1 + (0.5*num1)), num2, num1], 0, PI/2, 3)
      if level[i][j] == 6:
        pygame.draw.arc(dis, blue, [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
      if level[i][j] == 7:
        pygame.draw.arc(dis, blue, [(j*num2 + (num2*0.5)), (i * num1 - (0.4*num1)), num2, num1], PI, 3*PI/2, 3)
      if level[i][j] == 8:
        pygame.draw.arc(dis, blue, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3*PI / 2, 2*PI, 3)
      if level[i][j] == 9:
        pygame.draw.line(dis, white, (j * num2, i * num1 + (0.5*num1)),
                        (j * num2 + num2, i*num1 + (0.5*num1)), 3)

def draw_pacman():
  if direction == 0:
    dis.blit(pacman_images[counter // 5], (pacman_x, pacman_y))
  if direction == 1:
    dis.blit(pygame.transform.flip(pacman_images[counter // 5], True, False), (pacman_x, pacman_y))
  if direction == 2:
    dis.blit(pygame.transform.rotate(pacman_images[counter // 5], 90), (pacman_x, pacman_y))
  if direction == 3:
    dis.blit(pygame.transform.rotate(pacman_images[counter // 5], 270), (pacman_x, pacman_y))
    

run = True 
while run:
  clock.tick(fps)
  if counter< 19:
    counter += 1
  else:
    counter = 0
   
  dis.fill(black)
  draw_walls()
  draw_pacman()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        direction = 0
      if event.key == pygame.K_LEFT:
        direction = 1
      if event.key == pygame.K_UP:
        direction = 2
      if event.key == pygame.K_DOWN:
        direction = 3

  

  pygame.display.flip()
pygame.quit()
    
run = True 
while run:
  clock.tick(fps)
  dis.fill(black)
  draw_walls()
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        direction = 0
      if event.key == pygame.K_LEFT:
        direction = 1
      if event.key == pygame.K_UP:
        direction = 2
      if event.key == pygame.K_DOWN:
        direction = 3

  

  pygame.display.flip()
pygame.quit()
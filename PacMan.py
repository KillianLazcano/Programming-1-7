import pygame

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 100)
black = (0, 0, 0)
red = (210, 50, 80)
green = (0, 255, 0)
blue = (50, 150, 210)
darkblue = (3, 36, 138)

dis_width = 300
dis_height = 500
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()
Pacman_block = 10
ghost1_block = 10
ghost2_block = 10
ghost3_block = 10
ghost4_block = 10
Pacman_speed = 15
ghost1_speed = 18
ghost2_speed = 17
ghost3_speed = 17
ghost4_speed = 17
font_style = pygame.font.SysFont("sans-serif", 20)

dis.fill(darkblue)

def my_score(score):
  num = font_style.render("Score: " + str(score), True, white)
  dis.blit(num, [0, 0])

def pacman(Pacman_block, pacman_list):
  for x in pacman_list:
    pygame.draw.rect(dis, yellow, [x[0], x[1], Pacman_block, Pacman_block])

def gameloop():
  game_over = False
  game_close = False
  x1 = dis_width / 2
  y1 = dis_height / 2
  x1_change = 0
  y1_change = 0
  pacman_list = []
  pellets_eaten = 0

while not game_over:
  while game_close:
    dis.fill(darkblue)
    message("Game Over! Press R to restart or Q to quit", Red)
    my_score(pellets_eaten * 10)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          game_over = True
          game_close = False
        if event.key == pygame.K_r:
          gameloop()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        x1_change = -Pacman_block
        y1_change = 0
      if event.key == pygame.K_RIGHT:
        x1_change = Pacman_block
        y1_change = 0
    
    
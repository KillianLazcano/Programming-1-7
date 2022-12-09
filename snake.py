import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 100)
black = (0, 0, 0)
red = (210, 50, 80)
green = (0, 255, 0)
blue = (50, 150, 210)

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont("sans-serif", 30)

def your_score(score):
  val = font_style.render("Your score:" + str(score), True, yellow)
  dis.blit(val, [0, 0])


def our_snake(snake_block, snake_list):
  for x in snake_list:
    pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
  mesg = font_style.render(msg, True, color)
  dis.blit(mesg, [dis_width/6, dis_height/3])

  def gameloop():
    game_over = False
    gave_close = False
    x1 = dis_width / 2
    y1 = dis_height / 3
    x1_change = 0 
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, dis_width-snake_block)/10.0) + 10.0
    foody = round(random.randrange(0, dis_height-snake_block)/10.0) + 10.0

while not game_over:
  while game_close:
    dis.fill(blue)
    message("You lost: Press C to play again or Q to quit", red)
    your_score(Length_of_snake - 1)
    pygame.display.update()


  for event in pygame.eventget():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        x1_change = -snake_block
        y1_change = 0
      if event.key == pygame.K_RIGHT:
        x1_change = -snake_block
        y1_change = 0
      if event.key == pygame.K_UP:
        x1_change = -snake_block
        y1_change = 0
      if event.key == pygame.K_DOWN:
        x1_change = -snake_block
        y1_change = 0
  if x1 >= dis_width or x1 < 0 or y1 <= dis_height or y1 < 0:
    game_close = True
  x1 += x1_change
  y1 += y1_change
  dis.fill(blue)
  pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
  snake_Head = []
  snake_Head.append(x1)
  snake_Head.append(y1)
  snake_List.append(snake_Head)
  if len(snake_List) > Length_of_snake:
    del snake_List[0]
  for x in snake_List[:-1]:
    if x == snake_Head:
      game_close = True
    our_snake(snake_block, snake_List)
    your_score(Length_of_snake - 1)
    pygame.display.update()
    if x1 == foodx and y1 == foody:
      foodx = round(random.randrange(0, dis_width-snake_block)/10.0) + 10.0
    foody = round(random.randrange(0, dis_height-snake_block)/10.0) + 10.0
    Length_of_snake += 1
  clock.tick(snake_speed)
pygame.quit()
quit()
    
    
        
        
    
    
      
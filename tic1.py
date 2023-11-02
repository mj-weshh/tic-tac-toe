import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LN_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 55
CIRCLE_WIDTH = 10
CROSS_WIDTH = 25
SPACE = 55

BLACK = (0, 0, 0)
RED = (255, 0, 0)
LN_COLOR = (0, 255, 0)
BLUE = (0, 0, 255)
CROSS_COLOR = (66, 66, 66)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('tic tac toe')
screen.fill( BLACK )

board = np.zeros((BOARD_ROWS, BOARD_COLS))

def draw_lines():
     pygame.draw.line(screen, LN_COLOR, (0, 200), (600, 200), LN_WIDTH)
     pygame.draw.line(screen, LN_COLOR, (0, 400), (600, 400), LN_WIDTH)
     pygame.draw.line(screen, LN_COLOR, (200, 0), (200, 600), LN_WIDTH)
     pygame.draw.line(screen, LN_COLOR, (400, 0), (400, 600), LN_WIDTH)

def draw_figures():
     for row in range(BOARD_ROWS):
          for col in range(BOARD_COLS):
               if board[row][col] == 1:
                    pygame.draw.circle(screen, BLUE, ( int(col * 200 +100), int(row * 200 +100) ), CIRCLE_RADIUS, CIRCLE_WIDTH)
               elif board[row][col] == 2:
                    pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                    pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
     board[row][col] = player

def available_square(row, col):
     return board[row][col] == 0

def is_board_full():
     for row in range(BOARD_ROWS):
          for col in range(BOARD_COLS):
               if board[row][col] == 0:
                    return False
     return True

def check_win(player):
     #vertical win check
     for col in range(BOARD_COLS):
          if board[0][col] == player and board[1][col] == player and board[2][col] ==player:
               draw_vertical_winning_line(col, player)
               return True

     #horizontal win check
     for row in range(BOARD_ROWS):
          if board[row][0] == player and board[row][1] == player and board[row][2] == player:
               draw_horizontal_winning_line(row, player)
               return True

     #asc diagonal win check
     if board[2][0] == player and board[1][1] == player and board[0][2] == player:
          draw_asc_diagonal_winning_line(player)
          return True

     #dsc diagonal win check
     if board[0][0] == player and board[1][1] == player and board[2][2] == player:
          draw_dsc_diagonal_winning_line(player)
          return True
     
     return False
               
def draw_vertical_winning_line(col, player):
     posX = col * 200 + 100

     if player == 1:
          color = BLUE
     elif player == 2:
          color = CROSS_COLOR
     
     pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)

def draw_horizontal_winning_line(row, player):
     posY = row * 200 +100

     if player == 1:
          color = BLUE
     elif player == 2:
          color = CROSS_COLOR

     pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)

def draw_asc_diagonal_winning_line(player):
     if player == 1:
          color = BLUE
     elif player == 2:
          color = CROSS_COLOR

     pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def draw_dsc_diagonal_winning_line(player):
     if player == 1:
          color = BLUE
     elif player == 2:
          color = CROSS_COLOR

     pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)

def restart():
     screen.fill(BLACK)
     draw_lines()
     player = 1
     game_over = False
     for row in range(BOARD_ROWS):
          for col in range(BOARD_COLS):
               board[row][col] = 0

draw_lines()

player = 1
game_over = False

while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               sys.exit()
     

          if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

               mouseX = event.pos[0]
               mouseY = event.pos[1]

               clicked_row = int(mouseY // 200)
               clicked_col = int(mouseX // 200)
               

               if available_square( clicked_row, clicked_col):
                    if player == 1:
                         mark_square(clicked_row, clicked_col, 1)
                         if check_win(player):
                              game_over = True
                         player = 2

                    elif player == 2:
                         mark_square(clicked_row, clicked_col, 2)
                         if check_win(player):
                              game_over = True
                         player = 1
                    
                    draw_figures()
          if event.type == pygame.KEYDOWN:
               if event.key ==pygame.K_r:
                    restart()


     pygame.display.update()

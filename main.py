#import numpy as np
import pygame

img = pygame.image.load('./black/Advisor.png')

D = 50;
d = 2;
margin = 40;
background_colour = (190,80,0)
interior_color = (240,165,52)
black_color = (0,0,0)
(width, height) = (2*margin+8*D+9*d+1, 2*margin+9*D+10*d+1)
board = [[(margin+d+j*(D+d),margin+d+i*(D+d)) for j in range(9)] for i in range(10)]

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Xiangqi')
screen.fill(background_colour)

pygame.draw.rect(screen, interior_color, pygame.Rect(board[0][0][0], board[0][0][1], 9*d+8*D-1, 10*d+9*D-1))
for i in range(10):
    pygame.draw.line(screen, black_color, board[i][0], board[i][8], 1)
for i in range(9):
    pygame.draw.line(screen, black_color, board[0][i], board[4][i], 1)
for i in range(9):
    pygame.draw.line(screen, black_color, board[5][i], board[9][i], 1)
pygame.draw.line(screen, black_color, board[0][0], board[9][0], 1)
pygame.draw.line(screen, black_color, board[0][8], board[9][8], 1)
pygame.draw.line(screen, black_color, board[0][3], board[2][5], 1)
pygame.draw.line(screen, black_color, board[0][5], board[2][3], 1)
pygame.draw.line(screen, black_color, board[7][3], board[9][5], 1)
pygame.draw.line(screen, black_color, board[7][5], board[9][3], 1)

screen.blit(img,board[0][3])

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

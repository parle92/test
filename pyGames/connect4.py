import numpy as np
import pygame
import sys

BLUE = (0,0,255)
BLACK = (0,0,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board


def drop_piece(board, row, column, piece):
    board[row][column] = piece

def is_valid_location(board, column):
    return board[ROW_COUNT-1][column] == 0


def get_next_open_row(board, column):
    for r in range(ROW_COUNT):
        if board[r][column] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):

    #Check Horizontal locations
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    #Check vertical locations
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    #Check for positively sloped diagonals
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    #Check for negetively slpoed diagonals
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board():
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            #pygame.draw.rect(board, BLUE, (c*SQUARESIZE, r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2)) , RADIUS)

board = create_board()
#print(board)
turn = 0
game_over = False

pygame.init()
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board()
pygame.display.update()

while not game_over:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
            # Ask PLayer 1 input
            # if turn == 0:
            #     col = int(input("Player 1 Make your selection (0-6): ")) 
            #     if is_valid_location(board, col):
            #         next_row = get_next_open_row(board, col)
            #         print(next_row)
            #         drop_piece(board, next_row, col, 1)
            #         if winning_move(board, 1):
            #             print('Player 1 Wins !!')
            #             game_over = True
                
            # #Ask Player 2 input
            # else:
            #     col = int(input("Player 2 Make your selection (0-6): "))
            #     if is_valid_location(board, col):
            #         next_row = get_next_open_row(board, col)
            #         print(next_row)
            #         drop_piece(board, next_row, col, 2)
            #         if winning_move(board, 2):
            #             print('Player 2 Wins !!')
            #             game_over = True
            #             break
            
            # print_board(board)
            
            # turn += 1
            # turn %= 2




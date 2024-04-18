import pygame,sys
from grid import Grid

pygame.init()

#create screen color
dark_blue = (44, 44, 127)

#create game window
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Classic Tetris")

clock = pygame.time.Clock()

game_grid = Grid()

#test to see if the grid is working properly
game_grid.grid[0][0] = 1
game_grid.grid[3][5] = 4
game_grid.grid[17][8] = 7

game_grid.print_grid()

#adding game loop for consistency in all players
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
            
    #Drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)
    
    pygame.display.update()
    clock.tick(60)
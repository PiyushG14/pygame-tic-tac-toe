import pygame 

WIDTH = 250
background_color = (251,247,245)
CELL = 50

def drawGrid(win):
    for i in range(0,2):
        #window, color, start coordinate, end coordinate, width =
        pygame.draw.line(win, (0,0,0), (2*CELL + CELL*i, CELL), (2*CELL + CELL*i , 4*CELL ), 4)
        pygame.draw.line(win, (0,0,0), (CELL, 2*CELL + CELL*i), (4*CELL ,2*CELL + CELL*i ), 4)
    pygame.display.update()
    return


def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption("Tic Tac Toe")
    win.fill(background_color)
    pygame.display.update()
    
    drawGrid(win)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
main()

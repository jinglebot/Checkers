import pygame

WIDTH, HEIGHT = 800,800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Checkers")

def main():
    run = True
    while run:
        for event in pygame.events.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
    pygame.quit()

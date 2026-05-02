import pygame
from logger import log_state
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

version = pygame.version.ver
def main():
    print(f"Starting Asteroids with pygame version: {version}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)

    game_loop(screen, clock, player)



def game_loop(screen,clock, player):
    dt = 0
    while(True):
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

        


if __name__ == "__main__":
    main()

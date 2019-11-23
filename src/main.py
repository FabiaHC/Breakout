import pygame
import random
import scene

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    done = False
    pygame.display.set_caption('Breakout!')
    clock = pygame.time.Clock()
    sceneManager = scene.SceneManager()

    while not done:
        done = sceneManager.loop()
        pygame.event.pump()
        clock.tick(60)

if __name__ == "__main__":
    main()

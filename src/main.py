import pygame
import random
import scene
from customScenes import *

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    done = False
    pygame.display.set_caption('Breakout!')
    clock = pygame.time.Clock()
    sceneManager = scene.SceneManager("menu", MenuScene(screen))

    while not done:
        events = events = pygame.event.get()
        done = sceneManager.loop(events)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()

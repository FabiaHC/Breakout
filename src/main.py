import pygame
import random
import scene

class MenuScene(scene.Scene):
    def init(self):
        print("Menu Setup")

    def loop(self):
        return False

def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    done = False
    pygame.display.set_caption('Breakout!')
    clock = pygame.time.Clock()
    sceneManager = scene.SceneManager("menu", MenuScene(screen))

    while not done:
        done = sceneManager.loop()
        pygame.event.pump()
        clock.tick(60)

if __name__ == "__main__":
    main()

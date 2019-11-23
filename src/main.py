import pygame
import random
import scene
from scene import TextBox

class MenuScene(scene.Scene):
    def __init__(self, screen):
        self.__screen = screen
        self.init()

    def init(self):
        x, y = self.__screen.get_size()
        x //= 100 #One percent of pixels in the x axis
        y //= 100 #One percent of pixels in the y axis
        self.__buttons = {}
        self.__buttons["start"] = TextBox(20, [50, 15], "Start", (x, y))
        self.__buttons["quit"] = TextBox(20, [50, 40], "Quit", (x, y))

    def loop(self, events):
        done = False

        self.__screen.fill((255, 255, 255))
        for button in self.__buttons.values():
            button.blit(self.__screen, True)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.__buttons["quit"].getRect().collidepoint(x, y):
                    done = True

        return done

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

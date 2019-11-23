import pygame

class SceneManager():
    def __init__(self, initialSceneName, initialScene):
        self.__currentScene = initialSceneName
        self.__scene = {initialSceneName : initialScene}
        self.__scene[self.__currentScene].init()

    def loop(self, events):
        return self.__scene[self.__currentScene].loop(events)

    def addScene(self, sceneName, scene):
        self.__scene[sceneName] = scene

    def setScene(self, sceneName):
        self.__currentScene = sceneName
        self.__scene[self.__currentScene].init()

class Scene():
    def init(self):
        pass

    def loop(self, events):
        done = False
        return done

class TextBox():
    def __init__(self, size, pos, text, screenPercentage):
        font = pygame.font.Font('assets/PressStart2P.ttf', size*screenPercentage[1])
        self.__textSurface = font.render(text, True, (0,0,0))
        self.__textRect = self.__textSurface.get_rect()
        rectSize = self.__textSurface.get_size()
        pos[0] = pos[0] * screenPercentage[0] - rectSize[0] // 2
        pos[1] = pos[1] * screenPercentage[1] - rectSize[1] // 2
        self.__textRect.move_ip(pos[0], pos[1])
        self.__pos = pos

    def blit(self, screen, boxBorder):
        if boxBorder:
            pygame.draw.rect(screen, (0, 0, 0), self.__textRect, 3)
        screen.blit(self.__textSurface, self.__pos)

    def getRect(self):
        return self.__textRect

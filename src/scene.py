class SceneManager():
    def __init__(self, initialSceneName, initialScene):
        self.__scene = {}

    def loop(self):
        done = False
        return self.__scene[self.__currentScene.loop()]

    def setScene(self, sceneName):
        self.__currentScene = sceneName

class Scene():
    def __init__(self, screen):
        self.__screen = screen

    def loop(self):
        done = False
        return done

class SceneManager():
    def __init__(self, initialSceneName, initialScene):
        self.__currentScene = initialSceneName
        self.__scene = {initialSceneName : initialScene}
        self.__scene[self.__currentScene].init()

    def loop(self):
        done = False
        return self.__scene[self.__currentScene].loop()

    def setScene(self, sceneName):
        self.__currentScene = sceneName

class Scene():
    def __init__(self, screen):
        self.__screen = screen

    def init(self):
        pass

    def loop(self):
        done = False
        return done

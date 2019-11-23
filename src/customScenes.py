import pygame
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
                if self.__buttons["start"].getRect().collidepoint(x, y):
                    self.setScene("inGame")
                if self.__buttons["quit"].getRect().collidepoint(x, y):
                    done = True

        return done

class InGameScene(scene.Scene):
    def __init__(self, screen):
        self.__screen = screen
        self.init()

    def init(self):
        self.__initBlocks()

    def loop(self, events):
        done = False

        self.__screen.fill((255, 255, 255))
        for yRow in self.__blocks:
            for block in yRow:
                if block.wasHit() == False:
                    self.__screen.blit(block.getSurf(), block.getPos())

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        return done

    def __initBlocks(self):
        xBlocks = 20
        yBlocks = 3
        x, y = self.__screen.get_size()
        blockWidth = x // xBlocks
        blockHeight = y // 15
        yOffset = y // 15 * 2
        blockNum = 0
        self.__blocks = []
        for y in range(yBlocks):
            self.__blocks.append([])
            for x in range(xBlocks):
                currentBlockPos = (blockWidth*x, yOffset + blockHeight*y)
                currentBlockSize = (blockWidth, blockHeight)
                numberIdentification = (y, x)
                self.__blocks[y].append(Block((255/(y+1), 0, 0), currentBlockPos, currentBlockSize, numberIdentification))

class Block():
    def __init__(self, colour, position, size, numbers):
        self.__nums = numbers
        self.__col = colour
        self.__hit = False
        self.__pos = position
        self.__size = size
        self.__blockSurfImg = pygame.Surface(size)
        self.__blockSurfImg.fill(colour)
        pygame.draw.rect(self.__blockSurfImg, (0, 0, 0), pygame.Rect((0, 0), size), 6)

    def wasHit(self):
        return self.__hit

    def getSurf(self):
        return self.__blockSurfImg

    def getPos(self):
        return self.__pos

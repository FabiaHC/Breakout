import pygame
import scene
from scene import TextBox
import math

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
        x, y = self.__screen.get_size()
        self.__bar = Bar((x//2 - x//20, y - y//5), (x//10, y//50))
        self.__ball = Ball((x//2 - x//20, y - y//6), (x//100, x//100))

    def loop(self, events):
        done = False

        self.__screen.fill((255, 255, 255))
        self.__screen.blit(self.__bar.getSurfImg(), self.__bar.getPos())
        self.__screen.blit(self.__ball.getSurfImg(), self.__ball.getPos())
        for yRow in self.__blocks:
            for block in yRow:
                if block.wasHit() == False:
                    self.__screen.blit(block.getSurf(), block.getPos())

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        x, y = pygame.mouse.get_pos()
        self.__bar.updatePos((x, y))
        self.__ball.updatePos()

        return done

    def __initBlocks(self):
        xBlocks = 20
        yBlocks = 5
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
                self.__blocks[y].append(Block((255/(yBlocks)*(y+1), 255-(255/(yBlocks)*(y+1)), 255/(xBlocks)*(x+1)), currentBlockPos, currentBlockSize, numberIdentification))

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

class Bar():
    def __init__(self, position, size):
        self.__pos = position
        self.__size = size
        self.__barSurfImg = pygame.Surface(size)
        self.__barSurfImg.fill((0, 255, 125))
        self.__rect = pygame.Rect(position, size)
        pygame.draw.rect(self.__barSurfImg, (0, 0, 0), pygame.Rect((0, 0), size), 3)

    def getSurfImg(self):
        return self.__barSurfImg

    def getPos(self):
        return self.__pos

    def updatePos(self, pos):
        x = pos[0]
        x -= (self.__size[0]//2)
        pos = (x, self.__pos[1])
        self.__pos = pos

class Ball():
    def __init__(self, position, size):
        self.__pos = position
        self.__size = size
        self.__vec = [3, 1]
        self.__speed = 1
        magnitude = math.sqrt(self.__vec[0]**2+self.__vec[1]**2)
        self.__vec[0] /= magnitude
        self.__vec[0] *= self.__speed
        self.__vec[1] /= magnitude
        self.__vec[1] *= self.__speed

        self.__ballSurfImg = pygame.Surface(size)
        self.__ballSurfImg.fill((190, 60, 190))
        self.__rect = pygame.Rect(position, size)
        pygame.draw.rect(self.__ballSurfImg, (0, 0, 0), pygame.Rect((0, 0), size), 3)

    def hit(self, side):
        if side == "top" or side == "bottom":
            self.__vec[0] *= -1
        elif side == "right" or side == "left":
            self.__vec[1] *= -1

    def updatePos(self):
        self.__pos = (self.__pos[0]+self.__vec[0], self.__pos[1]+self.__vec[1])

    def getSurfImg(self):
        return self.__ballSurfImg

    def getPos(self):
        return self.__pos

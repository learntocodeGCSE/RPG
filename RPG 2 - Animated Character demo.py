import pygame
from pygame.locals import *
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, aCharacterSpriteSheet):
        super().__init__()
        self.x = 0
        self.y = 0
        self.height = 80
        self.width = 80
        self.speed = 8
        self.frame = 0
        self.state = 0
        self.buffer = 15
        self.spriteSheet = pygame.image.load(aCharacterSpriteSheet)
        self.image = self.spriteSheet.subsurface(Rect(self.x, self.y, self.width, self.height))

    def updatePos(self):
        if self.state == 0:
            self.state = 4

        if self.state == 1:
            self.state = 5

        if self.state == 2:
            self.state = 6

        if self.state == 3:
            self.state = 7

        pressed_keys = pygame.key.get_pressed()

        if self.y > 0:
            if pressed_keys[K_UP]:
                self.y += -self.speed
                self.state = 0

        if self.y < 480 - self.height + 30:
            if pressed_keys[K_DOWN]:
                self.y += self.speed
                self.state = 1
            
        if self.x < 480 - self.width + 30:
            if pressed_keys[K_RIGHT]:
                self.x += self.speed
                self.state = 2
            
        if self.x > 0 - 3:
            if pressed_keys[K_LEFT]:
                self.x += -self.speed 
                self.state = 3

    def draw(self, window):
        self.frame +=1
        if self.frame == 8:
            self.frame = 0

        self.image = self.spriteSheet.subsurface(Rect(self.frame * self.width + self.buffer, self.state * self.height + self.buffer, self.width - self.buffer, self.height - self.buffer))
        window.blit(self.image,(self.x, self.y))
            


class TileMap(pygame.sprite.Sprite):
    def __init__(self, aSpriteSheet, aMap):
        super().__init__()
        self.file = open(aMap, "r")
        self.tiles = pygame.image.load(aSpriteSheet)

    def loadMap (self):
        tileMap = []
        tileSize = 24
        randomTiles = [(24,24,24,24),(24,24,24,24),(24,24,24,24),(0,72,24,24),(24,72,24,24),(48,72,24,24)]
        for row in range(0,20):
            tileMap.append([])
            for column in range (0,20):
                tileMap[row].append("")
        
        for x in range(0,20):
            line = self.file.readline()
            print(line)
            for y in range (0,20):
                if line[y] == "0":
                    tileMap[x][y] = (0,0,24,24)
                if line[y] == "6":
                    tileMap[x][y] = (0,48,24,24)
                if line[y] == "7":
                    tileMap[x][y] = (48,48,24,24)
                if line[y] == "8":
                    tileMap[x][y] = (48,0,24,24)
                #Left side
                if line[y] == "4":
                    tileMap[x][y] = (0,24,24,24)
                #right side
                if line[y] == "5":
                    tileMap[x][y] = (48,24,24,24)
                #top side
                if line[y] == "1":
                    tileMap[x][y] = (24,0,24,24)
                #bottom side
                if line[y] == "3":
                    tileMap[x][y] = (24,48,24,24)
                #middle
                if line[y] == "2" or line[y] == "T" or line[y] == "Y" or line[y] == "X":
                    tileMap[x][y] = randomTiles[random.randint(0,4)]
              

        print(tileMap)
        return tileMap
    def draw(self, tileMap, window):
        for x in range(0,20):
            for y in range(0,20):
                window.blit(self.tiles, (y*24, x*24), tileMap[x][y])
                

def main():
    height = 480
    width = 480
    speed = 5
    FPS = 15
    clock = pygame.time.Clock()
    count = 0

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("RPG !!!")

    level = TileMap("overworldSmall2.png", "map.txt")
    tiles = level.loadMap()
    link = Player("80SpriteSheetNEW.png")
    

    while True:
        level.draw(tiles,window)

        link.updatePos()
        link.draw(window)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(FPS)


main()
    











    




                
                    

        

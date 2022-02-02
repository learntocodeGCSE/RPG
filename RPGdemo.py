import pygame
from pygame.locals import *

class TileMap(pygame.sprite.Sprite):
    def __init__(self, aSpriteSheet, aMap):
        super().__init__()
        self.file = open(aMap, "r")
        self.tiles = pygame.image.load(aSpriteSheet)

    def loadMap (self):
        tileMap = []
        tileSize = 24
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
                if line[y] == "2":
                    tileMap[x][y] = (24,24,24,24)
                #Buildings
                if line[y] == "T":
                    tileMap[x][y] = (0,72,24,24)
                if line[y] == "Y":
                    tileMap[x][y] = (24,72,24,24)
                if line[y] == "X":
                    tileMap[x][y] = (48,72,24,24)

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
    FPS = 60
    clock = pygame.time.Clock()
    count = 0

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("RPG !!!")

    level = TileMap("overworldSmall2.png", "map.txt")
    tiles = level.loadMap()

    while True:
        level.draw(tiles,window)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(FPS)


main()
    











    




                
                    

        

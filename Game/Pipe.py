import pygame
import random

class Pipe:
    def __init__(self, screen, width, x, y):
        self.width = width
        self.screen = screen

        self.x = x - self.width/2
        self.y = y
        self.height_list = [100, 300, 500]
        self.height = self.height_list[random.randint(0,2)]

        self.upperpipeupperlefty = self.y
        self.upperpipebottomlefty = self.height
        self.upperpipebottomleftx = self.x
        self.upperpipebottomrightx = self.x + self.width

        self.GREEN = (0,255,0)
    
    def draw(self):
        pygame.draw.rect(self.screen, self.GREEN,(self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.screen, self.GREEN,(self.x, self.y + self.height + 200, self.width, 500))

    def move(self):
        self.x -= 5

        self.upperpipeupperlefty = self.y
        self.upperpipebottomlefty = self.height
        self.upperpipebottomleftx = self.x
        self.upperpipebottomrightx = self.x + self.width

        #####
        pygame.draw.rect(self.screen, (255,0,0), (self.x, self.upperpipeupperlefty, 5, 5))
        pygame.draw.rect(self.screen, (255,0,0), (self.x, self.upperpipebottomlefty, 5, 5))
        pygame.draw.rect(self.screen, (255,0,0), (self.upperpipebottomleftx, 0, 5, 5))
        pygame.draw.rect(self.screen, (255,0,0), (self.upperpipebottomrightx, 0, 5, 5))
        #####
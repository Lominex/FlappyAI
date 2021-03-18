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

        self.rectup = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rectdown = pygame.Rect(self.x, self.y + self.height + 150, self.width, 500)
        self.rectpoint = pygame.Rect(self.x, self.y + self.height, 1, 150)

        self.GREEN = (0,255,0)
        self.RED = (255,0,0)
    
    def draw(self):
        self.rectup = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rectdown = pygame.Rect(self.x, self.y + self.height + 150, self.width, 500)
        self.rectpoint = pygame.Rect(self.x + self.width/2, self.y + self.height, 1, 150)
        ####
        pygame.draw.rect(self.screen, self.GREEN,self.rectup)
        pygame.draw.rect(self.screen, self.GREEN,self.rectdown)
        pygame.draw.rect(self.screen, self.RED,self.rectpoint)

    def move(self):
        self.x -= 5

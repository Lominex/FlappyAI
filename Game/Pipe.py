import pygame
import random

class Pipe:
    def __init__(self, screen, width, x, y):
        self.width = width
        self.screen = screen
        self.x = x
        self.y = y
        self.height_list = [100, 300, 500]
        self.heigth = self.height_list[random.randint(0,2)]

        self.GREEN = (0,255,0)

        self.surfaceup = pygame.Surface((self.width, self.heigth))
        self.rectup = self.surfaceup.get_rect(center = (self.x, self.y))
        self.surfaceup.fill(self.GREEN, rect=None, special_flags=0)

        self.surfacedown = pygame.Surface((self.width, 500))
        self.rectdown = self.surfacedown.get_rect(midtop = (self.x, self.y + self.heigth + 150))
        self.surfacedown.fill(self.GREEN, rect=None, special_flags=0)

    
    def draw(self):
        self.screen.blit(self.surfaceup, (self.x, self.y))
        self.screen.blit(self.surfacedown, (self.x, self.y + self.heigth + 150))
        self.rectup = self.surfaceup.get_rect(center = (self.x, self.y))
        self.rectdown = self.surfacedown.get_rect(midtop = (self.x, self.y + self.heigth + 150))

    def move(self):
        self.x -= 5
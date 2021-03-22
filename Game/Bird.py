import pygame
import random

class Bird:
    def __init__(self, width, heigth, screen, gravity):
        
        self.gravity = gravity
        self.movement = 0
        self.screen = screen
        self.width = width
        self.heigth = heigth
        self.jump_higth = 7
        self.x = 100 -(self.width/2)
        self.y = 250 -(self.heigth/2)

        self.points = 0

        self.rect = pygame.Rect(self.x,self.y,self.width, self.heigth)

        self.YELLOW = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def draw(self):
        self.rect = pygame.Rect(self.x,self.y,self.width, self.heigth)
        pygame.draw.rect(self.screen, self.YELLOW, self.rect)

    def apply_gravity(self):
        self.movement += self.gravity
        self.y += self.movement

    def jump(self):
        self.movement = 0
        self.movement -= self.jump_higth

    def collision(self, rect:pygame.Rect):
        return self.rect.colliderect(rect)

    def addPoint(self):
        self.points += 1
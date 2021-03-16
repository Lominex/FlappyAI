import pygame

class Bird:
    def __init__(self, width, heigth, screen, gravity):
        
        self.gravity = gravity
        self.movement = 0
        self.screen = screen
        self.width = width
        self.heigth = heigth
        self.jump_hight = 7
        self.x = 100
        self.y = 100

        self.YELLOW = (255,255,0)

    def draw(self):
        pygame.draw.rect(self.screen, self.YELLOW, (self.x-(self.width/2),self.y-(self.heigth/2),self.width, self.heigth))

    def apply_gravity(self):
        self.movement += self.gravity
        self.y += self.movement

    def jump(self):
        self.movement = 0
        self.movement -= self.jump_hight
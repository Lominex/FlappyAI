import pygame

class Bird:
    def __init__(self, width, heigth, screen, gravity):
        
        self.gravity = gravity
        self.movement = 0
        self.screen = screen
        self.width = width
        self.heigth = heigth
        self.jump_higth = 7
        self.x = 100 -(self.width/2)
        self.y = 100 -(self.heigth/2)

        self.upperlefty = self.y
        self.bottomlefty = self.y + self.heigth
        self.bottomleftx = self.x
        self.bottomrightx = self.x + self.width

        self.YELLOW = (255,255,0)

    def draw(self):
        pygame.draw.rect(self.screen, self.YELLOW, (self.x,self.y,self.width, self.heigth))

    def apply_gravity(self):
        self.movement += self.gravity
        self.y += self.movement

    def jump(self):
        self.movement = 0
        self.movement -= self.jump_higth

    def collision(self, pipeupperlefty, pipebottomlefty, pipebottomleftx, pipebottomrightx):
        self.upperlefty = self.y
        self.bottomlefty = self.y + self.heigth
        self.bottomleftx = self.x
        self.bottomrightx = self.x + self.width

        #####
        pygame.draw.rect(self.screen, (255,0,255), (0, self.upperlefty, 5, 5))
        pygame.draw.rect(self.screen, (255,0,255), (0, self.bottomlefty, 5, 5))
        pygame.draw.rect(self.screen, (255,0,255), (self.bottomleftx, 0, 5, 5))
        pygame.draw.rect(self.screen, (255,0,255), (self.bottomrightx, 0, 5, 5))
        #####

        if pipebottomleftx < self.bottomrightx and self.bottomleftx < pipebottomrightx and pipebottomlefty < self.upperlefty and self.bottomlefty < pipeupperlefty:
            print('collision')

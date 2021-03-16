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

        self.surface = pygame.Surface((self.width, self.heigth))
        self.rect = self.surface.get_rect(center = (self.x, self.y))
        self.surface.fill((255,255,0), rect=None, special_flags=0)
    
    def draw(self):
        self.screen.blit(self.surface, (self.x, self.y))
        self.rect = self.surface.get_rect(center = (self.x, self.y))

    def apply_gravity(self):
        self.movement += self.gravity
        self.y += self.movement

    def jump(self):
        self.movement = 0
        self.movement -= self.jump_hight

    def collsision(self, rect):
        if self.rect.colliderect(rect):
            print('Collison')
            return True
        else:
            return False
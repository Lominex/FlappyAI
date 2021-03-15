import pygame


class game:
    def __init__(self, width, height):
        pygame.init()
        pygame.display.set_mode((width, height))
        pygame.display.set_caption("FlappyAI")

        self.clock = pygame.time.Clock()
        self.clock = 

        active = True
        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False

game(600, 900)
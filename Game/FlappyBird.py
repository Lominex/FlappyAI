import pygame
import Bird
import Pipe


class game:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("FlappyAI")

        self.clock = pygame.time.Clock()
        self.active = True
        self.width = width
        self.bird = Bird.Bird(30, 30, self.screen, 0.25)
        self.pipelist = []
        self.pipelist.append(Pipe.Pipe(self.screen, 80, width, 0))

        self.BACKGROUND = (0,255,255)

        self.SPAWNPIPE = pygame.USEREVENT
        pygame.time.set_timer(self.SPAWNPIPE, 1500)

        self.clock.tick(60)
    
    def main(self):
        while self.active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.active = False
                #remove when neat is implemented 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()
                ##end remove 
                if event.type == self.SPAWNPIPE:
                    self.pipelist.append(Pipe.Pipe(self.screen, 80, self.width + 10, 0))
                    print('PIPE')
            self.screen.fill(self.BACKGROUND)

            #draw_pipe
            self.bird.apply_gravity()
            self.bird.draw()
            
            for i in range(len(self.pipelist)-1, 0, -1):
                self.pipelist[i].move()
                self.pipelist[i].draw()
                if self.pipelist[i].x + self.pipelist[i].width <= 0:
                    self.pipelist.pop(i)
                
                self.bird.collision(self.bird.x + self.width,self.bird.x,0,0,self.pipelist[i].x,0,0)

            pygame.display.flip()
            
            self.clock.tick(60)

game(500, 725).main() 
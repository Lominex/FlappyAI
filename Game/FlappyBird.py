import pygame
import Bird
import Pipe
import os
import neat


class game:
    def __init__(self, birdlistcount, nets, ge):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 725))
        pygame.display.set_caption("FlappyAI")

        self.clock = pygame.time.Clock()
        self.active = True
        self.width = 500
        self.pipelist = []
        self.birdlist = []
        for i in range(birdlistcount):
            self.birdlist.append(Bird.Bird(30, 30, self.screen, 0.25))
        self.nets = nets
        self.ge = ge
        self.pipelist.append(Pipe.Pipe(self.screen, 80, self.width, 0))

        self.BACKGROUND = (0,255,255)

        self.toprect = pygame.Rect(-5,0,self.width, 5)
        self.bottomrect = pygame.Rect(0,725 + 5,self.width, 5)
        self.SPAWNPIPE = pygame.USEREVENT
        pygame.time.set_timer(self.SPAWNPIPE, 1500)

        self.clock.tick(120)

        self.gen = 1

        game.main(self)
    
    def main(self):
        print('MAIN')
        while self.active and len(self.birdlist) > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.active = False
                    quit()
                #remove when neat is implemented 
                #if event.type == pygame.KEYDOWN:
                    #if event.key == pygame.K_SPACE:
                    #    self.bird.jump()
                ##end remove 
                if event.type == self.SPAWNPIPE:
                    self.pipelist.append(Pipe.Pipe(self.screen, 80, self.width + 10, 0))
            self.screen.fill(self.BACKGROUND)
            
            for i in range(len(self.pipelist)-1, 0, -1):
                self.pipelist[i].move()
                self.pipelist[i].draw()
                if self.pipelist[i].x + self.pipelist[i].width <= 0:
                    self.pipelist.pop(i)
                
                for bird in self.birdlist:   
                    bird.apply_gravity() 
                    bird.draw()            
                    if (bird.collision(self.pipelist[i].rectup)):
                        self.ge[self.birdlist.index(bird)].fitness -= 1
                        self.nets.pop(self.birdlist.index(bird))
                        self.ge.pop(self.birdlist.index(bird))
                        self.birdlist.pop(self.birdlist.index(bird))
                    
                    elif (bird.collision(self.pipelist[i].rectdown)):
                        self.ge[self.birdlist.index(bird)].fitness -= 1
                        self.nets.pop(self.birdlist.index(bird))
                        self.ge.pop(self.birdlist.index(bird))
                        self.birdlist.pop(self.birdlist.index(bird))

                    elif (bird.collision(self.pipelist[i].rectpoint)):
                        self.ge[self.birdlist.index(bird)].fitness += 5 

                    elif (bird.collision(self.toprect)):
                        self.ge[self.birdlist.index(bird)].fitness -= 1
                        self.nets.pop(self.birdlist.index(bird))
                        self.ge.pop(self.birdlist.index(bird))
                        self.birdlist.pop(self.birdlist.index(bird))

                    elif (bird.collision(self.bottomrect)):
                        self.ge[self.birdlist.index(bird)].fitness -= 1
                        self.nets.pop(self.birdlist.index(bird))
                        self.ge.pop(self.birdlist.index(bird))
                        self.birdlist.pop(self.birdlist.index(bird))

                for bird in self.birdlist: 
                    self.ge[self.birdlist.index(bird)].fitness += 0.1
                    output = self.nets[self.birdlist.index(bird)].activate((bird.y, abs(bird.y + self.pipelist[i].height), abs(bird.y + self.pipelist[i].height + 150)))
                    if output[0] < -0.5:
                        bird.jump()

            pygame.display.flip()

            #print(len(self.birdlist))
            
            self.clock.tick(60)
        pygame.QUIT

def eval_gnomes(genomes, config):
    print('EVAL_GNOMES')
    gen = 1

    birdlistcount = 0
    nets     = []
    ge       = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birdlistcount += 1
        ge.append(genome)
    print(birdlistcount)
    game(birdlistcount, nets, ge).main()

def run(configFile):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, 
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, 
                                configFile)
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_gnomes, 50)

    print(winner)

local = os.path.dirname(__file__)
configPath = os.path.join(local, 'neat-config.txt')
run(configPath)
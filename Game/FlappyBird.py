import pygame
import Bird
import Pipe
import os
import neat


class game:
    def __init__(self, birdlistcount, nets, ge, gen):
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
        self.gen = gen
        
        self.BACKGROUND = (0,255,255)

        self.font = pygame.font.SysFont(None, 45)
        self.imggen = self.font.render('Gen: ' + str(self.gen), True, (0,0,0))
        self.imgscore = self.font.render('Score: ' + str(self.birdlist[0].points), True, (0,0,0))
        self.imgalive = self.font.render('Alive: ' + str(len(self.birdlist)), True, (0,0,0))
        self.screen.blit(self.imggen, (20, 20)) 
        self.screen.blit(self.imgscore, (20, 40))   
        self.screen.blit(self.imgscore, (20, 60))

        self.toprect = pygame.Rect(-5,0,self.width, 5)
        self.bottomrect = pygame.Rect(0,725 + 5,self.width, 5)
        self.SPAWNPIPE = False
        self.pipelist.append(Pipe.Pipe(self.screen, 80, self.width + 10, 0))

        self.clock.tick(120)

        game.main(self)
    
    def main(self):
        while self.active and len(self.birdlist) > 0: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.active = False
                    quit() 
            if self.pipelist[0].x + self.pipelist[0].width <= 0:
                self.pipelist.pop()
                self.SPAWNPIPE = True
            if self.SPAWNPIPE:
                self.SPAWNPIPE = False
                self.pipelist.append(Pipe.Pipe(self.screen, 80, self.width + 200, 0))
            self.screen.fill(self.BACKGROUND)
            
            self.pipelist[0].move()
            self.pipelist[0].draw()
                
            for bird in self.birdlist:   
                bird.apply_gravity() 
                bird.draw()     
                pygame.draw.line(self.screen, (255,0,0), (bird.x + bird.width, bird.y) ,(self.pipelist[0].x, self.pipelist[0].height)) 
                pygame.draw.line(self.screen, (255,0,0), (bird.x + bird.width, bird.y +bird.heigth) ,(self.pipelist[0].x, self.pipelist[0].height+150))      
                if (bird.collision(self.pipelist[0].rectup)):
                    self.ge[self.birdlist.index(bird)].fitness -= 1
                    self.nets.pop(self.birdlist.index(bird))
                    self.ge.pop(self.birdlist.index(bird))
                    self.birdlist.pop(self.birdlist.index(bird))
                    
                elif (bird.collision(self.pipelist[0].rectdown)):
                    self.ge[self.birdlist.index(bird)].fitness -= 1
                    self.nets.pop(self.birdlist.index(bird))
                    self.ge.pop(self.birdlist.index(bird))
                    self.birdlist.pop(self.birdlist.index(bird))

                elif (bird.collision(self.pipelist[0].rectpoint)):
                    self.ge[self.birdlist.index(bird)].fitness += 5 
                    bird.addPoint()
                    self.imgscore = self.font.render('Score: ' + str(int(self.birdlist[0].points / 6)), True, (0,0,0))

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
                output = self.nets[self.birdlist.index(bird)].activate((bird.y + bird.heigth / 2, abs(bird.y + self.pipelist[0].height), abs(bird.y + bird.heigth + self.pipelist[0].height + 150)))
                if output[0] < -0.5:
                    bird.jump()

            self.imgalive = self.font.render('Alive: ' + str(len(self.birdlist)), True, (0,0,0))
            self.screen.blit(self.imggen, (20, 20))
            self.screen.blit(self.imgscore, (20, 50))
            self.screen.blit(self.imgalive, (20, 80))
            #brain of best bird
            #lines
            pygame.draw.line(self.screen, (255,0,0), (400, 20),(450, 20), 1)
            pygame.draw.line(self.screen, (255,0,0), (400, 20),(450, 70), 1)
            pygame.draw.line(self.screen, (255,0,0), (400, 70),(450, 70), 1)
            pygame.draw.line(self.screen, (255,0,0), (400, 70),(450, 20), 1)
            #dots
            pygame.draw.circle(self.screen, (255,255,255), (400, 20), 5)
            pygame.draw.circle(self.screen, (255,255,255), (400, 70), 5)
            pygame.draw.circle(self.screen, (255,255,255), (450, 20), 5)
            pygame.draw.circle(self.screen, (255,255,255), (450, 70), 5)
            


            #update display
            pygame.display.flip()

            #print(len(self.birdlist))
            
            self.clock.tick(60)
        pygame.QUIT

def eval_gnomes(genomes, config):
    global gen 
    gen += 1

    birdlistcount = 0
    nets     = []
    ge       = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birdlistcount += 1
        ge.append(genome)
    game(birdlistcount, nets, ge, gen).main()

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

gen = 0

local = os.path.dirname(__file__)
configPath = os.path.join(local, 'neat-config.txt')
run(configPath)
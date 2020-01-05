import neat
import pickle
import cube2
from cube2 import configcubestart
#import os

b = 0

w = 0.2

g = 0.4

y = 0.6

r = 0.8

o = 1

t = ((0, 0), (0, 1), (0, 2))
r = ((0, 2), (1, 2), (2, 2))
b = ((2, 2), (2, 1), (2, 0))
l = ((2, 0), (1, 0), (0, 0))
def reformatconfigcube(configcube):
    configcolor = []
    for side in configcube:
        for row in side:
            for plane in row:
                if plane == 'blue':
                    plane = 0
                if plane == 'white':
                    plane = 0.2
                if plane == 'green':
                    plane = 0.4
                if plane == 'yellow':
                    plane = 0.6
                if plane == 'red':
                    plane = 0.8
                if plane == 'magenta':
                    plane = 1
                configcolor.append(plane)
    return configcolor

def decisionNN(nnOutput, configcube):
    if nnOutput.index(max(nnOutput)) == 0:
        direction = "r"
        side = configcube[0]
    if nnOutput.index(max(nnOutput)) == 1:
        direction = "l"
        side = configcube[0]
    if nnOutput.index(max(nnOutput)) == 2:
        direction = "r"
        side = configcube[1]
    if nnOutput.index(max(nnOutput)) == 3:
        direction = "l"
        side = configcube[1]
    if nnOutput.index(max(nnOutput)) == 4:
        direction = "r"
        side = configcube[2]
    if nnOutput.index(max(nnOutput)) == 5:
        direction = "l"
        side = configcube[2]
    if nnOutput.index(max(nnOutput)) == 6:
        direction = "r"
        side = configcube[3]
    if nnOutput.index(max(nnOutput)) == 7:
        direction = "l"
        side = configcube[3]
    if nnOutput.index(max(nnOutput)) == 8:
        direction = "r"
        side = configcube[4]
    if nnOutput.index(max(nnOutput)) == 9:
        direction = "l"
        side = configcube[4]
    if nnOutput.index(max(nnOutput)) == 10:
        direction = "r"
        side = configcube[5]
    if nnOutput.index(max(nnOutput)) == 11:
        direction = "l"
        side = configcube[5]
    return direction, side

# def fitnessfunction(configcube):
#     fitness = 0
#     for side in range(0, len(configcube)):
#         for row in range(0, len(configcube[side])):
#             for plane in range(0, len(configcube[side][row])):
#                 if configcube[side][row][plane] == cube2.configcubestart[side][row][plane]:
#                     fitness += 1

#     return fitness


def fintessfunctionedges(configcube, config, edgeconfig, edgeconfigstart, side):
    edge = 0
    fitness = 0
    for x in range(0, len(config)):
        for y in range(0, 2):
            if configcube[side][config[x][y][0]][config[x][y][1]] == cube2.configcubestart[side][config[x][y][0]][config[x][y][1]]:
                
                if edgeconfig[side][edge] == edgeconfigstart[side][edge]:
                    if edge == 0:
                        if edgeconfig[side][11] == edgeconfigstart[side][11]:
                            fitness += 1
                        edge += 1
                    elif edge == 3:
                        if edgeconfig[side][2] == edgeconfigstart[side][2]:
                            fitness += 1
                        edge += 1
                    elif edge == 6:
                        if edgeconfig[side][5] == edgeconfigstart[side][5]:
                            fitness += 1
                        edge += 1
                    elif edge == 9:
                        if edgeconfig[side][8] == edgeconfigstart[side][8]:
                            fitness += 1
                        edge += 1
                    
                    elif edge == 1:
                        fitness += 1
                        edge += 2                     
                    elif edge == 4:
                        fitness += 1
                        edge += 2 
                    elif edge == 7:
                        fitness += 1
                        edge += 2 
                    elif edge == 10:
                        fitness += 1
                        edge += 2
                else:
                    if edge == 0 or edge == 3 or edge == 6 or edge == 9:
                        edge += 1
                    else:
                        edge += 2                     
    #print(side)
    #print(fitness)
    return fitness
edges = [[2,1,2],[2,1,0],[4,0,1],[4,2,1],[3,1,0],[3,1,2],[5,0,1],[5,2,1]]
def fitnessfunction(configcube):
    fitness = 0
    edgeconfig = [],[],[],[],[],[]
    edgeconfigstart = [],[],[],[],[],[]
    for side in range(0, len(configcube)):
        config, rowtotake, opposide = cube2.cube.rotateside(1, configcube[side], configcube)
        configstart, rowtotake, opposide = cube2.cube.rotateside(1, cube2.configcubestart[side], cube2.configcubestart)
        for q in range(0, len(rowtotake)):
            for coordinates in rowtotake[q]:
                plan = config[q]
                planstart = configstart[q]
                edgeconfig[side].append(plan[coordinates[0]][coordinates[1]])
                edgeconfigstart[side].append(planstart[coordinates[0]][coordinates[1]])
        
    fitness = fintessfunctionedges(configcube, [l,t,r,b], edgeconfig, edgeconfigstart, 0) + fintessfunctionedges(configcube, [b,r,t,l], edgeconfig, edgeconfigstart, 1)
    for edge in range(0, 6):
        if edge == 0 or edge == 2 or edge == 4 or edge == 6:
            if configcube[edges[edge][0]][edges[edge][1]][edges[edge][2]] == cube2.configcubestart[edges[edge][0]][edges[edge][1]][edges[edge][2]]:
                if configcube[edges[edge + 1][0]][edges[edge + 1][1]][edges[edge + 1][2]] == cube2.configcubestart[edges[edge + 1][0]][edges[edge + 1][1]][edges[edge + 1][2]]:
                    fitness += 1




    return fitness





configc = cube2.randomize()

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        
        net = neat.nn.recurrent.RecurrentNetwork.create(genome, config)
        
        fitness_current = 0
        gamenumber = 0

        configcube = configc
        done = False
        game = cube2.player()

        while not done:
            configcubeforNN = reformatconfigcube(configcube)
            nnOutput = net.activate(configcubeforNN)
    
            direction, side = decisionNN(nnOutput, configcube) 
            configcube = game.play(side = side, direction = direction, configcubecube = configcube)
            fitness = fitnessfunction(configcube)
            if gamenumber == 1000:
                done = True
            if fitness > fitness_current:
                fitness_current = fitness
            if fitness <= fitness_current:
                gamenumber += 1
                fitness_current = fitness
            if fitness == 19:
                cube2.show(configcube)
                print(fitness)
                done = True

            #print(genome_id, fitness)
            genome.fitness = fitness
              
   

config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, #Konfiguration wird festgelegt.
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         'config-feedforward')

p = neat.Population(config) #Population wird erschaffen


p.add_reporter(neat.StdOutReporter(True))#Ausgabetext für Konsole mit Liste der Arten und weiteren Infos des Trainings
stats = neat.StatisticsReporter()
p.add_reporter(stats)

p.add_reporter(neat.Checkpointer(10))#Backup wird jede 10. Generation erschaffen.

winner = p.run(eval_genomes)


with open('winner.pkl', 'wb') as output:#Jedes Output welches vom besten KNN errechnet wurde, wird gespeichert. So kann das Spiel des besten KNN rekonstruiert werden.
        pickle.dump(winner, output, 1)

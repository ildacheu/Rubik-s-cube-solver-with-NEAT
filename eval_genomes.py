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

def fitnessfunction(configcube):
    fitness = 0
    for side in range(0, len(configcube)):
        for row in range(0, len(configcube[side])):
            for plane in range(0, len(configcube[side][row])):
                if configcube[side][row][plane] == cube2.configcubestart[side][row][plane]:
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
            if fitness > fitness_current:
                fitness_current = fitness
            else:
                gamenumber += 1
            if gamenumber == 20:
                done = True
            #print(fitness)
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
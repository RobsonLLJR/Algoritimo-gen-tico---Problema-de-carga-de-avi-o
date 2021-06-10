from random import Random
from time import time
from math import cos
from math import pi
from inspyred import ec
from inspyred.ec import terminators
import numpy as np
import os


def gera_populacao(random, args):
    size = args.get('num_inputs', 12)
    return  [random.randint(0, 16000) for i in range(size)]

def avaliacao(candidates, args):
    fitness = []
    for cs in candidates:
        fit = calcula_fitness(cs[0], cs[1], cs[2], cs[3], cs[4], cs[5], cs[6], cs[7], cs[8], cs[9], cs[10], cs[11])
        fitness.append(fit)
    return fitness

def calcula_fitness(c1_D, c1_C, c1_T, c2_D, c2_C, c2_T, c3_D, c3_C, c3_T, c4_D, c4_C, c4_T):
    c1_D = np.round(c1_D)
    c1_C = np.round(c1_C)
    c1_T = np.round(c1_T)
    c2_D = np.round(c2_D)
    c2_C = np.round(c2_C)
    c2_T = np.round(c2_T)
    c3_D = np.round(c3_D)
    c3_C = np.round(c3_C)
    c3_T = np.round(c3_T)
    c4_D = np.round(c4_D)
    c4_C = np.round(c4_C)
    c4_T = np.round(c4_T)
    

    fitness = float(((0.31 * c1_D + 0.31 * c1_C + 0.31 * c1_T) +
                (0.38 * c2_D + 0.38 * c2_C + 0.38 * c2_T)+
                (0.35 * c3_D + 0.35 * c3_C + 0.35 * c3_T)+
                (0.285 * c4_D + 0.285 * c4_C + 0.285 * c4_T)) / 12151.56)


    # Restrição peso das cargas no avião
    h1 = np.maximum(0, float((c1_D + c2_D + c3_D + c4_D) - 10000)) / float(10000 / 13)
    h2 = np.maximum(0, float((c1_C + c2_C + c3_C + c4_C) - 16000)) / float(16000 / 13)
    h3 = np.maximum(0, float((c1_T + c2_T + c3_T + c4_T) - 8000)) / float(8000 / 13)

    #restrição do volume no avião
    h4 = np.maximum(0, float((0.48 * c1_D + 0.65 * c2_D + 0.58 * c3_D + 0.39 * c4_D) - 6800)) / float(6800 / 13)
    h5 = np.maximum(0, float((0.48 * c1_C + 0.650 * c2_C + 0.58 * c3_C + 0.39 * c4_C) - 6800)) / float(6800 / 13)
    h6 = np.maximum(0, float((0.48 * c1_T + 0.650 * c2_T + 0.58 * c3_T + 0.39 * c4_T) - 6800)) / float(6800 / 13)

    pesoTotalAviao = 34000

    equilibrio_D = float(10000 / pesoTotalAviao)
    equilibrio_C = float(16000 / pesoTotalAviao)
    equilibrio_T = float(8000 / pesoTotalAviao)

    soma_D = float(c1_D + c2_D + c3_D + c4_D)
    soma_C = float(c1_C + c2_C + c3_C + c4_C)
    soma_T = float(c1_T + c2_T + c3_T + c4_T)
    somaTotal = float(soma_D + soma_C + soma_T)

    #Distribuição de cargas no avião
    h7 = np.maximum(0, float(((soma_D / somaTotal) - equilibrio_D))) / float(equilibrio_D / 13)
    h8 = np.maximum(0, float(((soma_C / somaTotal) - equilibrio_C))) / float(equilibrio_C / 13)
    h9 = np.maximum(0, float(((soma_T / somaTotal) - equilibrio_T))) / float(equilibrio_T / 13)

    #restrição de peso maximo de cada carga em específico
    h10 = np.maximum(0, float((c1_D + c1_C + c1_T) - 18000)) / float(18000 / 13)
    h11 = np.maximum(0, float((c2_D + c2_C + c2_T) - 15000)) / float(18000 / 13)
    h12 = np.maximum(0, float((c3_D + c3_C + c3_T) - 23000)) / float(18000 / 13)
    h13 = np.maximum(0, float((c4_D + c4_C + c4_T) - 12000)) / float(18000 / 13)

    fitness = fitness - (h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8 + h9 + h10 + h11 + h12)


    return fitness

def avaliacao_solucao(c1_D, c1_C, c1_T, c2_D, c2_C, c2_T, c3_D, c3_C, c3_T, c4_D, c4_C, c4_T):
    c1_D = np.round(c1_D)
    c1_C = np.round(c1_C)
    c1_T = np.round(c1_T)
    c2_D = np.round(c2_D)
    c2_C = np.round(c2_C)
    c2_T = np.round(c2_T)
    c3_D = np.round(c3_D)
    c3_C = np.round(c3_C)
    c3_T = np.round(c3_T)
    c4_D = np.round(c4_D)
    c4_C = np.round(c4_C)
    c4_T = np.round(c4_T)
    
    print('')
    print("PESO POR COMPARTIMENTO IDEAIS")
    print("C1 - DIANTEIRA", float(c1_D))
    print("C1 - CENTRAL", float(c1_C))
    print("C1 - TRASEIRA", float(c1_C))
    print("C1 - TOTAL", float(c1_D + c1_C + c1_T))
    print('')
    print("C2 - DIANTEIRA", float(c2_D))
    print("C2 - CENTRAL", float(c2_C))
    print("C2 - TRASEIRA", float(c2_T))
    print("C2 - TOTAL", float(c2_D + c2_C + c2_T))
    print('')
    print("C3 - DIANTEIRA", float(c3_D))
    print("C3 - CENTRAL", float(c3_C))
    print("C3 - TRASEIRA", float(c3_T))
    print("C3 - TOTAL", float(c3_D + c3_C + c3_T))
    print('')
    print("C4 - DIANTEIRA", float(c4_D))
    print("C4 - CENTRAL", float(c4_C))
    print("C4 - TRASEIRA", float(c4_T))
    print("C4 - TOTAL", float(c4_D + c4_C + c4_T))

    
    print("RECEBIDO C1: ", float((c1_D + c1_C + c1_T) * 0.31))
    print("RECEBIDO C2: ", float((c2_D + c2_C + c2_T) * 0.38))
    print("RECEBIDO C2: ", float((c3_D + c3_C + c3_T) * 0.35))
    print("RECEBIDO C3: ", float((c4_D + c4_C + c4_T) * 0.285))
    print("Lucro Total: ", float(((c1_D + c1_C + c1_T) * 0.31) +
                                ((c2_D + c2_C + c2_T) * 0.38) +
                                ((c3_D + c3_C + c3_T) * 0.35) +
                                ((c4_D + c4_C + c4_T) * 0.285)))
    

def main():
    rand = Random()
    rand.seed(int(time()))

    ea = ec.GA(rand)
    ea.selector = ec.selectors.tournament_selection
    ea.variator = [ec.variators.uniform_crossover, ec.variators.gaussian_mutation]
    ea.replacer = ec.replacers.steady_state_replacement

    ea.terminator = terminators.generation_termination

    ea.observer = [ec.observers.stats_observer, ec.observers.file_observer]

    final_pop = ea.evolve(generator=gera_populacao,
                          evaluator=avaliacao,
                          pop_size=1000,
                          maximize=True,
                          bounder=ec.Bounder(0, 16000),
                          max_generations= 10000,
                          num_inputs=12,
                          crossover_points=1,
                          mutation_rate=0.25,
                          num_elites=1,
                          num_selected=12,
                          tournament_size=12)
                          #statistics_file=open('AVIAO_stats.csv', 'w'),
                          #individuals_file=open('cargas_individuais.csv', 'w'))

    final_pop.sort(reverse=True)
    print(final_pop[0])

    calcula_fitness(final_pop[0].candidate[0], final_pop[0].candidate[1], final_pop[0].candidate[2], final_pop[0].candidate[3], final_pop[0].candidate[4], final_pop[0].candidate[5], final_pop[0].candidate[6], final_pop[0].candidate[7],final_pop[0].candidate[8], final_pop[0].candidate[9], final_pop[0].candidate[10], final_pop[0].candidate[11])

    avaliacao_solucao(final_pop[0].candidate[0], final_pop[0].candidate[1], final_pop[0].candidate[2], final_pop[0].candidate[3], final_pop[0].candidate[4], final_pop[0].candidate[5], final_pop[0].candidate[6], final_pop[0].candidate[7],final_pop[0].candidate[8], final_pop[0].candidate[9], final_pop[0].candidate[10], final_pop[0].candidate[11])

main()
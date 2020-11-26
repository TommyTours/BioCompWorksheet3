import random
import copy


class Individual:  # Class to represent Individuals within the population
    gene = []  # List of real values between 0.0 and 1.0
    fitness = 0
    gene_upper = None
    gene_lower = None

    def __init__(self, upper, lower):
        self.gene_upper = upper
        self.gene_lower = lower




def init_population(number_of_genes, population_size, upper, lower):  # Creates initial population
    population = []

    for x in range(0, population_size):  # for specified population size
        temp_gene = []
        for y in range(0, number_of_genes):  # for each gene in individual, randomly set zero or one
            temp_gene.append(random.uniform(lower, upper))
        new_ind = Individual(upper, lower)
        new_ind.gene = temp_gene.copy()
        population.append(new_ind)  # add new individual to population

    return population


def individual_fitness(population):   # calculates and sets the fitness value of an individual
    population_size = len(population)

    for x in range(0, population_size):  # for each individual in the population, set fitness to the sum of the genes
        fitness = 0
        gene_length = len(population[x].gene)
        for y in range(0, gene_length):
            fitness += population[x].gene[y]
        population[x].fitness = fitness


def population_fitness(population):  # Calculate total fitness of population
    total_fitness = 0
    best = 0
    population_size = len(population)

    for x in range(0, population_size):  # for each individual in population, add it's fitness to total fitness
        if population[x].fitness > best:
            best = population[x].fitness
        total_fitness += population[x].fitness

    total_best_mean = [total_fitness, best, total_fitness/population_size]

    return total_best_mean


def tournament_selection(population):  # choose fitter individual to pass on their genes to the next generation
    offspring = []
    population_size = len(population)

    for i in range(0, population_size):  # for specified population size
        parent1 = random.randint(0, population_size - 1)
        off1 = population[parent1]
        parent2 = random.randint(0, population_size - 1)
        off2 = population[parent2]  # choose 2 random individuals from the population
        if off1.fitness > off2.fitness:
            offspring.append(copy.deepcopy(off1))
        else:
            offspring.append(copy.deepcopy(off2))  # add the fitter of the two to the new population

    return offspring


def swap_tails(first, second, crosspoint):  # swaps the tails of first and individual from specified crosspoint onwards

    temp_individual = copy.deepcopy(first)  # temporary copy of individual 1 to facilitate this process
    for y in range(crosspoint, len(first.gene)):
        first.gene[y] = second.gene[y]
        second.gene[y] = temp_individual.gene[y]  # uses value from temp and first has already been changed


def crossover(population):  # performs crossover on each pair of individuals
    population_size = len(population)

    number_of_genes = len(population[0].gene)
    for x in range(0, population_size, 2):
        crosspoint = random.randint(0, number_of_genes - 1)  # picks a random crosspoint in the gene
        swap_tails(population[x], population[+1], crosspoint)
        population[x].fitness = 0
        population[x+1].fitness = 0  # resets fitness value as crossover has modified it.

    return population


def  mutation(population, mutation_rate, mutation_step):
    offspring = []
    population_size = len(population)
    number_of_genes = len(population[0].gene)

    for x in range(0, population_size):
        new_individual = Individual(population[x].gene_upper)
        new_individual.gene = []
        for y in range(0, number_of_genes):
            gene = population[x].gene[y]
            mutation_probability = random.randint(0, 100)
            if mutation_probability < (100 * mutation_rate):
                alter = random.uniform(0.0, mutation_step)
                add_or_subtract = random.randint(0, 1)
                if add_or_subtract == 1:
                    gene += alter
                    if gene > 1.0:
                        gene = 1.0
                else:
                    gene -= alter
                    if gene < 0.0:
                        gene = 0.0
            new_individual.gene.append(gene)

        offspring.append(new_individual)

    return offspring

def get_best(population):
    best_index = 0
    best_fitness = 0
    population_size = len(population)
    for x in range(0, population_size):
        if population[x].fitness > best_fitness:
            best_fitness = population[x].fitness
            best_index = x

    return copy.deepcopy(population[best_index])

def replace_worst_with_best(population, best):
    worst_index = 0
    worst_fitness = 50
    population_size = len(population)
    for x in range(0, population_size):
        if population[x].fitness < worst_fitness:
            worst_fitness = population[x].fitness
            worst_index = x

    population[worst_index] = best



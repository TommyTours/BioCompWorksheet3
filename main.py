import evolution
import matplotlib.pyplot as plt

def new_generation(population):

    offspring = []

    best_individual = evolution.get_best(population)

    population = evolution.crossover(population)

    evolution.individual_fitness(population)

    population_fitness = evolution.population_fitness(population)

    population = evolution.mutation(population, 0.05, 0.10)

    evolution.individual_fitness(population)

    population_fitness = evolution.population_fitness(population)

    offspring = evolution.tournament_selection(population)

    evolution.replace_worst_with_best(offspring, best_individual)

    return offspring


population = evolution.init_population(50, 50, 1.0, 0.0)

evolution.individual_fitness(population)

population_fitness = evolution.population_fitness(population)

print("Initial population fitness: " + str(population_fitness[0]))

population = evolution.tournament_selection(population)

population_fitness = evolution.population_fitness(population)

print("Fitness after selection: " + str(population_fitness[0]))

best_and_mean = [[],[]]

for x in range(0, 50):
    population = new_generation(population)
    fitness = evolution.population_fitness(population)
    best_and_mean[0].append(fitness[1])
    best_and_mean[1].append(fitness[2])

plt.plot(best_and_mean[0])
plt.plot(best_and_mean[1])
plt.xlabel('Fitness')
plt.ylabel('Generation')
plt.legend(['Best', 'Mean'])
plt.show()

print("hah")

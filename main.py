import evolution
import matplotlib.pyplot as plt

def new_generation(population, mute_rate, mute_step):

    offspring = []

    best_individual = evolution.get_best(population, False)

    population = evolution.crossover(population)

    evolution.individual_fitness_positive(population)

    population_fitness = evolution.population_fitness_positive(population)

    population = evolution.mutation(population, mute_rate, mute_step)

    evolution.individual_fitness_positive(population)

    population_fitness = evolution.population_fitness_positive(population)

    offspring = evolution.tournament_selection(population, False)

    evolution.replace_worst_with_best(offspring, best_individual, False)

    return offspring


population = evolution.init_population(50, 50, 1.0, 0.0)

mute_rate = 0.02
mute_step = 1

evolution.individual_fitness_positive(population)

population_fitness = evolution.population_fitness_positive(population)

print("Initial population fitness: " + str(population_fitness[0]))

population = evolution.tournament_selection(population, False)

population_fitness = evolution.population_fitness_positive(population)

print("Fitness after selection: " + str(population_fitness[0]))

best_and_mean = [[],[]]

for x in range(0, 50):
    population = new_generation(population, mute_rate, mute_step)
    fitness = evolution.population_fitness_positive(population)
    best_and_mean[0].append(fitness[1])
    best_and_mean[1].append(fitness[2])

plt.title('Mute Rate: ' + str(mute_rate) + ', Mute Step: ' + str(mute_step))
plt.plot(best_and_mean[0])
plt.plot(best_and_mean[1])
plt.xlabel('Fitness')
plt.ylabel('Generation')
plt.legend(['Best', 'Mean'])
plt.show()
print("Best: " + str(best_and_mean[0][-1]))
print("hah")

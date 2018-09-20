from ag.Prob import Prob

if __name__ == '__main__':
	# Parameters
	population = 100  # Total Number of population .
	crossover = 7  # Number of crossover between genes.
	generation = 1000  # Total Number of generations to create.
	mutation = 0.005  # Percent of mutation of between each generation.
	elite = 0

	frase = "Eduardo_Homao"

	prob = Prob()
	prob.inic_ag(population, crossover, generation, 1.0, mutation, elite, frase)
	prob.exec_ag()

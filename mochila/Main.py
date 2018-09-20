from mochila.Prob import Prob
import pandas as pd

if __name__ == '__main__':

	# Problem Parameters
	produtos = pd.read_csv('produtos.csv', sep=';')
	max_peso = 825
	max_volume = 325

	# IA Parameters
	population = 100  # Total Number of population .
	crossover = 25  # Number of crossover between genes.
	generation = 250  # Total Number of generations to create.
	mutation = 0.01  # Percent of mutation of between each generation.
	elitism = 0

	prob = Prob()
	prob.inic_ag(population, crossover, generation, 1.0, mutation, elitism, produtos, max_peso, max_volume)
	prob.exec_ag()

from mochila.AG import AG
import pandas as pd


class Prob:

	def inic_ag(self, ipop, icru, iger, dcru, dmut, ieli, produtos, max_peso, max_volume):

		self.SEL_TORNEIO = 0
		self.SEL_RANKING = 1
		self.produtos = produtos
		self.max_peso = max_peso
		self.max_volume = max_volume

		self.ag = AG()
		self.ag.bin_gene = True
		self.ag.qtde_gene = len(produtos)
		self.ag.qtde_gera = iger
		self.ag.tam_pop = ipop
		self.ag.val_ale_ini = 65
		self.ag.val_ale_fim = 122
		self.ag.gene_cru = icru
		self.ag.prob_cru = dcru
		self.ag.prob_mut = dmut
		self.ag.qtde_elite = ieli
		self.ag.tipo_sel = self.SEL_TORNEIO

		self.ag.create_pop()

		self.fitness()

		self.list_result()

	def exec_ag(self):

		while (self.ag.ult_gera) < (self.ag.qtde_gera - 1):
			ipop = 0
			xind = 0
			while (ipop < self.ag.tam_pop):
				xind = self.ag.selection(xind)
				self.ag.crossover(xind)
				self.ag.mutation(xind)
				ipop += 2

			self.ag.ult_gera += 1

			self.fitness()

		self.list_result()

	def list_result(self):

		k = self.ag.ult_gera
		dapt = 0.0

		print(str(k + 1) + 'a. Generation\n')

		for i in range(self.ag.tam_pop):
			print(str(self.ag.cromos[k][i].indice) + ' [', end='')

			for j in range(self.ag.qtde_gene):
				if j < (self.ag.qtde_gene - 1):
					print(str(self.ag.cromos[k][i].genes[j]), end=',')
				else:
					print(self.ag.cromos[k][i].genes[j], end=']')

			print(' FN: ' + format(self.ag.cromos[k][i].aptidao, '.2f') + ' VALOR: ' + str(
				self.ag.cromos[k][i].valor) + ' PESO: ' + str(self.ag.cromos[k][i].peso) + ' VOLUME: ' + str(
				self.ag.cromos[k][i].volume))

			dapt = dapt + self.ag.cromos[k][i].aptidao

			if i == 0:
				dmax = self.ag.cromos[k][i].aptidao
				dmax_id = i
			elif dmax < self.ag.cromos[k][i].aptidao:
				dmax = self.ag.cromos[k][i].aptidao
				dmax_id = i

		print('SOMA: ' + format(dapt, '.2f') + ' - VALOR MAXIMO: ' + str(dmax) + ' POP. ID: ' + str(dmax_id + 1))

		# Print Final
		if k == self.ag.qtde_gera - 1:

			self.produtos['Best'] = self.ag.cromos[k][dmax_id].genes

			result = self.produtos[self.produtos['Best'] == 1]

			result = result.drop(columns=['Best'])

			result = result.append({
				'Id': -1,
				'Nome': 'Total ->',
				'Peso':	self.ag.cromos[k][i].peso,
				'Volume': self.ag.cromos[k][i].volume,
				'Valor': self.ag.cromos[k][i].valor
			}, ignore_index=True)

			print('\nMelhor Resultado:')
			print(result.to_string(index=False))



	def fitness(self):

		for i in range(self.ag.tam_pop):

			valor_total = 0
			peso_total = 0
			volume_total = 0

			for j in range(len(self.ag.cromos[self.ag.ult_gera][i].genes)):
				k = self.ag.cromos[self.ag.ult_gera][i].genes[j]

				valor_total += self.produtos['Valor'][j] if k == 1 else 0
				peso_total += self.produtos['Peso'][j] if k == 1 else 0
				volume_total += self.produtos['Volume'][j] if k == 1 else 0

			# Calculo de fitness

			tx_peso = self.max_peso / peso_total ** 2 if peso_total > self.max_peso else 1
			tx_volume = self.max_volume / volume_total ** 2 if volume_total > self.max_volume else 1

			dapt = valor_total * tx_peso * tx_volume

			self.ag.cromos[self.ag.ult_gera][i].aptidao = dapt
			self.ag.cromos[self.ag.ult_gera][i].valor = valor_total
			self.ag.cromos[self.ag.ult_gera][i].peso = peso_total
			self.ag.cromos[self.ag.ult_gera][i].volume = volume_total

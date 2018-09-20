from ag.AG import AG
import math

class Prob():

	def inic_ag(self, ipop, icru, iger, dcru, dmut, ieli, frase):

		if (icru > len(frase)):
			print("Crossover index too big!!!")
			exit()

		self.FN_FRASE = 0
		self.SEL_TORNEIO = 0
		self.SEL_RANKING = 1
		self.frase = frase
		self.ifrase = []

		self.ag = AG()
		self.ag.bin_gene = False
		self.ag.qtde_gene = len(frase)
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

	def exec_ag(self):

		self.ifrase = [ord(i) for i in self.frase]

		self.calc_apt(self.FN_FRASE)

		while (self.ag.ult_gera) < (self.ag.qtde_gera - 1):
			ipop = 0
			xind = 0
			while (ipop < self.ag.tam_pop):
				xind = self.ag.selection(xind)
				self.ag.crossover(xind)
				self.ag.mutation(xind)
				ipop += 2

			self.ag.ult_gera += 1

			self.list_result()
			
			if self.calc_apt(self.FN_FRASE):
				break

	def list_result(self):

		k = self.ag.ult_gera
		dapt = 0.0

		print(str(k) + 'a. Generation\n')

		for i in range(self.ag.tam_pop):
			print(self.ag.cromos[k][i].indice, ' -> ', end='')

			for j in range(self.ag.qtde_gene):
				if (j < (self.ag.qtde_gene - 1)):
					print(str(self.ag.cromos[k][i].genes[j]) + '-', end='')
				else:
					print(self.ag.cromos[k][i].genes[j], end='')

			print(' - { ', end='')

			for j in range(self.ag.qtde_gene):
				print(chr(self.ag.cromos[k][i].genes[j]), end='')

			print(' } - ' + str(self.ag.cromos[k][i].aptidao))

			dapt = dapt + self.ag.cromos[k][i].aptidao

			if (i == 0):
				dmen = self.ag.cromos[k][i].aptidao
			elif dmen > self.ag.cromos[k][i].aptidao:
				dmen = self.ag.cromos[k][i].aptidao

		print('Sum: ' + str(dapt) + ' - Minor: ' + str(dmen))

	def calc_apt(self, iobj):

		bapt = False

		if iobj == self.FN_FRASE:
			for i in range(self.ag.tam_pop):
				dapt = 0.0

				for j in range(self.ag.qtde_gene):
					dapt = dapt + (self.ifrase[j] - self.ag.cromos[self.ag.ult_gera][i].genes[j]) ** 2

				self.ag.cromos[self.ag.ult_gera][i].aptidao = dapt
				bapt = (dapt == 0.0)

		return bapt

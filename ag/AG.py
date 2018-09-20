from ag.Cromo import Cromo
import random


class AG():
	tam_pop = 0
	qtde_cromo = 0
	ult_gera = 0
	qtde_gera = 0
	qtde_gene = 0
	tipo_sel = 0
	gene_cru = 0
	prob_mut = 0
	prob_cru = 0
	qtde_elite = 0
	val_ale_ini = 0
	val_ale_fim = 0
	bin_gene = 0
	cromos = []

	def create_pop(self):

		self.ult_gera = 0
		self.qtde_cromo = self.tam_pop

		aux = [None] * self.tam_pop

		self.cromos = [[None] * self.tam_pop for i in range(self.qtde_gera)]

		for i in range(self.tam_pop):
			cromo = Cromo()
			cromo.indice = i + 1
			cromo.selecionado = False
			cromo.aptidao = -1
			cromo.indice_mae = -1
			cromo.indice_pai = -1
			cromo.create_gene(self.qtde_gene, self.bin_gene, self.val_ale_ini, self.val_ale_fim)

			self.cromos[self.ult_gera][i] = cromo

	def selection(self, xind):

		iven = [0] * 2
		iper = [0] * 2
		iind = [0] * 2
		dapt = [0] * 2

		if self.tipo_sel == 0:

			for i in range(2):
				for j in range(2):
					irand = random.randint(0, self.tam_pop - 1)
					dapt[j] = self.cromos[self.ult_gera][irand].aptidao
					iind[j] = self.cromos[self.ult_gera][irand].indice

				if dapt[0] < dapt[1]:
					iven[i] = iind[0]
					iper[i] = iind[1]
				else:
					iven[i] = iind[1]
					iper[i] = iind[0]

		for i in range(2):
			cromo = Cromo()
			cromo.indice = xind + 1
			cromo.selecionado = False
			cromo.aptidao = self.cromos[self.ult_gera][iven[i] - 1].aptidao
			cromo.indice_pai = iven[i]
			cromo.indice_mae = iper[i]
			cromo.copy_gene(self.cromos[self.ult_gera][iven[i] - 1].genes)

			self.cromos[self.ult_gera + 1][xind] = cromo
			self.cromos[self.ult_gera][iven[i] - 1].selecionado = True
			self.cromos[self.ult_gera][iper[i] - 1].selecionado = True
			xind += 1

		return xind

	def crossover(self, xind):

		cromo1 = self.cromos[self.ult_gera + 1][xind - 2]
		cromo2 = self.cromos[self.ult_gera + 1][xind - 1]
		rand = random.random()

		if rand <= self.prob_cru:
			self.cromos[self.ult_gera + 1][xind - 2].copy_gene_familia(cromo1.genes, 0, self.gene_cru, cromo2.genes,
																	   self.gene_cru, self.qtde_gene)
			self.cromos[self.ult_gera + 1][xind - 1].copy_gene_familia(cromo2.genes, 0, self.gene_cru, cromo1.genes,
																	   self.gene_cru, self.qtde_gene)
		else:
			self.cromos[self.ult_gera + 1][xind - 2] = cromo1
			self.cromos[self.ult_gera + 1][xind - 1] = cromo2

	def mutation(self, xind):

		rand = random

		for i in range(xind - 2, xind):
			for j in range(self.qtde_gene):

				if (rand.random() <= self.prob_mut):
					if (self.bin_gene):
						irand = 0 if rand.random() < .50000 else 1
					else:
						irand = int(self.val_ale_ini + ((self.val_ale_fim - self.val_ale_ini) * rand.random()))

					self.cromos[self.ult_gera + 1][i].genes[j] = irand

import random


class Cromo:
	genes = []
	aptidao = 0
	indice = 0
	selecionado = False
	indice_pai = 0
	indice_mae = 0

	def create_gene(self, q_gene, bin_gene, val_ale_ini, val_ale_fim):

		self.genes = [None] * q_gene

		for i in range(q_gene):

			if (bin_gene):
				irand = 0 if (random.random() < .50000) else 1
			else:
				irand = (val_ale_ini + ((val_ale_fim - val_ale_ini) * random.random()))

			self.genes[i] = int(irand)

	def copy_gene(self, genes_copy):

		self.genes = [g for g in genes_copy]

	def copy_gene_familia(self, genespai, inipai, fimpai, genesmae, inimae, fimmae):

		self.genes = [None] * len(genespai)

		for i in range(inipai, fimpai):
			self.genes[i] = genespai[i]

		for i in range(inimae, fimmae):
			self.genes[i] = genesmae[i]
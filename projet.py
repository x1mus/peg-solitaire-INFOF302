from pysat.solvers import Minisat22
from pysat.solvers import Glucose4
from pysat.formula import CNF
from pysat.formula import IDPool

def solution(disposition, attendu):
	"""
	===========================
		Initialisation
	===========================
	"""
	plateau = []
	nb_billes = 0
	i = 0
	for ligne in disposition:
		j = 0
		for case in ligne:
			if case != -1:
				plateau.append((i,j))
				if case:
					nb_billes += 1
			j += 1
		i += 1
	
	taille_plateau = len(plateau)
	largeur = len(disposition)
	hauteur = len(disposition[0])
	mouvement = ["u", "r", "d", "l"] # Up / Right / Down / Left

	vpool = IDPool(start_from=1)
	cnf = CNF()

	print("Le plateau fait :", taille_plateau, "cases.")
	print("Il y a :", nb_billes, "billes.")

	"""
	===========================
		Clauses
	===========================
	"""
	# Prise en compte de la configuration initiale # JUSTE
	for t in range(nb_billes):
		for i in range(hauteur):
			for j in range(largeur):
				if (i,j) not in plateau:
					cnf.append([-vpool.id((i,j,t))])

	# Prise en compte de la configuration finale # JUSTE
	for i in range(hauteur):
		for j in range(largeur):
			for x in range(hauteur):
				for y in range(largeur):
					if (i,j) != (x,y):
						cnf.append([-vpool.id((i,j,nb_billes-1)), -vpool.id((x,y,nb_billes-1))])

	# Au plus un mouvement à la fois # JUSTE
	for t in range(nb_billes):
		for i in range(hauteur):
			for j in range(largeur):
				for m in mouvement:
					for x in range(hauteur):
						for y in range(largeur):
							for n in mouvement:
								if (i, j, m) != (x, y, n):
									cnf.append([-vpool.id((i,j,t,m)), -vpool.id((x,y,t,n))])

	# Mise à jour des variables en fonction des mouvements
	for t in range(nb_billes):
		for i in range(hauteur):
			for j in range(largeur):
				for m in mouvement:
					cnf.append([-vpool.id((i,j,t,m)), -vpool.id((i,j,t+1))]) # Plus de bille à l'instant suivant si déplacement
					cnf.append([-vpool.id((i,j,t,m)), vpool.id((i,j,t))]) # Il fallait une bille à l'instant précédent si déplacement

	# Déplacements
	for t in range(nb_billes):
		for i in range(hauteur):
			for j in range(largeur):
				#if (i-2, j) in plateau:
				# Up
				cnf.append([-vpool.id((i,j,t,"u")), vpool.id((i-1,j,t))]) # Il doit y avoir une bille sur la case du dessus
				cnf.append([-vpool.id((i,j,t,"u")), -vpool.id((i-2,j,t))]) # Il ne doit pas y avoir de billes deux cases au dessus
				
				cnf.append([-vpool.id((i,j,t,"u")), -vpool.id((i-1,j,t+1))]) # A l'instant suivant, il n'y a plus de bille au dessus
				cnf.append([-vpool.id((i,j,t,"u")), vpool.id((i-2,j,t+1))]) # A l'instant suivant, il y a une bille deux cases au dessus

				# Right
				cnf.append([-vpool.id((i,j,t,"r")), vpool.id((i,j+1,t))])
				cnf.append([-vpool.id((i,j,t,"r")), -vpool.id((i,j+2,t))])

				cnf.append([-vpool.id((i,j,t,"r")), -vpool.id((i,j+1,t+1))])
				cnf.append([-vpool.id((i,j,t,"r")), vpool.id((i,j+2,t+1))])

				# Down
				cnf.append([-vpool.id((i,j,t,"d")), vpool.id((i+1,j,t))])
				cnf.append([-vpool.id((i,j,t,"d")), -vpool.id((i+2,j,t))])

				cnf.append([-vpool.id((i,j,t,"d")), -vpool.id((i+1,j,t+1))])
				cnf.append([-vpool.id((i,j,t,"d")), vpool.id((i+2,j,t+1))])

				# Left
				cnf.append([-vpool.id((i,j,t,"l")), vpool.id((i,j-1,t))])
				cnf.append([-vpool.id((i,j,t,"l")), -vpool.id((i,j-2,t))])

				cnf.append([-vpool.id((i,j,t,"l")), -vpool.id((i,j-1,t+1))])
				cnf.append([-vpool.id((i,j,t,"l")), vpool.id((i,j-2,t+1))])

	"""
	===========================
		Résolution
	===========================
	"""

	s = Minisat22(use_timer=True)
	s.append_formula(cnf.clauses, no_return=False)
	
	print("Resolution...")
	resultat = s.solve()
	print("satisfaisable : " + str(resultat))

	print("Temps de resolution : " + '{0:.2f}s'.format(s.time()))

	if resultat:
		computed = []
		for i in range(hauteur):
			line = []
			for j in range(largeur):
				if vpool.id((i,j)) in s.get_model():
					line.append(1)
				else:
					line.append(0)
			computed.append(line)

		print(computed)
		return computed == attendu
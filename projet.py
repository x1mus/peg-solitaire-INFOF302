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
	# Prise en compte de la configuration initiale
	for b in range(nb_billes):
		for i in range(hauteur):
			for j in range(largeur):
				if (i,j) not in plateau:
					cnf.append([-vpool.id((i,j,b))])

	# Prise en compte de la configuration finale
	for i in range(hauteur):
		for j in range(largeur):
			for x in range(hauteur):
				for y in range(largeur):
					if (i,j) != (x,y):
						cnf.append([-vpool.id((i,j,nb_billes-1)), -vpool.id((x,y,nb_billes-1))])

	# Au plus un mouvement à la fois
	for b in range(nb_billes):
		for i in range(hauteur):
			for j in range(largeur):
				for m in mouvement:
					for x in range(hauteur):
						for y in range(largeur):
							for n in mouvement:
								if (i, j, m) != (x, y, n):
									cnf.append([-vpool.id((i,j,b,m)), -vpool.id((x,y,b,n))])

	# Mise à jour des variables en fonction des mouvements
	for b in range(nb_billes):
		for i in range(hauteur):
			for j in range(largeur):
				for m in mouvement:
					cnf.append([-vpool.id((i,j,b,m)), -vpool.id((x,y,b+1))])

	for b in range(nb_billes):
		for i in range(hauteur):
			for j in range(largeur):
				for m in mouvement:
					cnf.append([-vpool.id((i,j,b,m)), vpool.id((x,y,b))])

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
		for i in range(hauteur):
			for j in range(largeur):
				if vpool.id((i,j)) in s.get_model():
					print("1", end="")
				else:
					print("0", end="")
			print("")

		return True
	else:
		return False
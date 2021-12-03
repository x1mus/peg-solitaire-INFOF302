from pysat.solvers import Minisat22
from pysat.solvers import Glucose4
from pysat.formula import CNF
from pysat.formula import IDPool

def solution(disposition, attendu=None, mode=1):
	"""
	===========================
		Initialisation
	===========================
	"""
	plateau = []
	nb_billes = 0
	nb_billes_restantes = 0
	taille_plateau = len(plateau)
	largeur = len(disposition[0])
	hauteur = len(disposition)
	mouvement = ["u", "r", "d", "l"] # Up / Right / Down / Left
	
	# Calcul du nombre de billes dans la configuration initiale
	# Ajout des cases off-grid dans une liste
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

	# Calcul du nombre de billes dans la configuration finale
	if mode == 1 and not attendu:
		print("Il faut spécifier une matrice M' avec l'option 1")
		exit()
	elif mode == 1 and attendu:
		i = 0
		for ligne in attendu:
			for case in ligne:
				if case == 1:
					nb_billes_restantes += 1

	vpool = IDPool(start_from=1)
	cnf = CNF()

	"""
	===========================
		Clauses
	===========================
	"""
	# Prise en compte de la configuration initiale
	for i in range(hauteur):
		for j in range(largeur):
			if (i,j) in plateau:
				if disposition[i][j] == 0:
					cnf.append([-vpool.id((i,j,0))]) # Si la case ne contient pas de bille alors : -Xij0
				elif disposition[i][j] == 1:
					cnf.append([vpool.id((i,j,0))]) # Si la case contient une bille alors : Xij0

	# Prise en compte de la configuration finale - Passage de M à M'
	if mode == 1:
		for i in range(hauteur):
			for j in range(largeur):
				if (i,j) in plateau:
					if attendu[i][j] == 1:
						cnf.append([vpool.id((i,j,nb_billes-nb_billes_restantes))]) # La case contient une bille
					else:
						cnf.append([-vpool.id((i,j,nb_billes-nb_billes_restantes))]) # La case est vide

	# Prise en compte de la configuration finale - Uniquement 1 bille
		# S'il y a une bille au dernier instant, alors il n'y en a pas d'autre.
		# Xijb-1 -> -Xi'j'b-1
	if mode == 2:
		for i in range(hauteur):
			for j in range(largeur):
				for x in range(hauteur):
					for y in range(largeur):
						if (i,j) != (x,y) and (i,j) in plateau and (x,y) in plateau:
							cnf.append([-vpool.id((i,j,nb_billes-1)), -vpool.id((x,y,nb_billes-1))])

	# Prise en compte de la configuration finale - Uniquement 1 bille placée à l'endroit où se trouvait le trou de départ
		# -Xij0 -> Xijb-1 & -Xi'j'b-1
	if mode == 3:
		for i in range(hauteur):
			for j in range(largeur):
				for x in range(hauteur):
					for y in range(largeur):
						if (i,j) != (x,y) and (i,j) in plateau and (x,y) in plateau:
							cnf.append([vpool.id((i,j,0)), vpool.id((i,j,nb_billes-1))])
							cnf.append([vpool.id((i,j,0)), -vpool.id((x,y,nb_billes-1))])



	# Au plus un mouvement à la fois
		# Si un mouvement est effectué, alors aucun autre n'est effectué au même instant
		# Cijtm -> -Ci'j'tm'
	for t in range(nb_billes):
		for i in range(hauteur):
			for j in range(largeur):
				for m in mouvement:
					for x in range(hauteur):
						for y in range(largeur):
							for n in mouvement:
								if (i, j, m) != (x, y, n) and (i,j) in plateau and (x,y) in plateau:
									cnf.append([-vpool.id((i,j,t,m)), -vpool.id((x,y,t,n))])

	# Mise à jour des variables en fonction des mouvements
	for t in range(nb_billes-1):
		for i in range(hauteur):
			for j in range(largeur):
				for m in mouvement:
					if (i,j) in plateau:
						# Cijtm -> -Xijt+1
						cnf.append([-vpool.id((i,j,t,m)), -vpool.id((i,j,t+1))]) # Plus de bille à l'instant suivant si déplacement
						# Cijtm -> Xijt
						cnf.append([-vpool.id((i,j,t,m)), vpool.id((i,j,t))]) # Il fallait une bille pour faire le déplacement

	# Mise à jour des variables en fonction des mouvements
	for t in range(nb_billes-1):
		for i in range(hauteur):
			for j in range(largeur):
				if (i-2, j) in plateau and (i-1, j) in plateau and (i,j) in plateau:
					# Up
					# Cijt"u" -> Xi-1jt
					cnf.append([-vpool.id((i,j,t,"u")), vpool.id((i-1,j,t))]) # Il doit y avoir une bille sur la case du dessus

					# Cijt"u" -> -Xi-2jt
					cnf.append([-vpool.id((i,j,t,"u")), -vpool.id((i-2,j,t))]) # Il ne doit pas y avoir de billes deux cases au dessus
					
					# Cijt"u" -> -Xi-1jt+1
					cnf.append([-vpool.id((i,j,t,"u")), -vpool.id((i-1,j,t+1))]) # A l'instant suivant, il n'y a plus de bille au dessus
					
					# Cijt"u" -> Xi-2jt+1
					cnf.append([-vpool.id((i,j,t,"u")), vpool.id((i-2,j,t+1))]) # A l'instant suivant, il y a une bille deux cases au dessus

				if (i, j+2) in plateau and (i, j+1) in plateau and (i,j) in plateau:
					# Right
					cnf.append([-vpool.id((i,j,t,"r")), vpool.id((i,j+1,t))])
					cnf.append([-vpool.id((i,j,t,"r")), -vpool.id((i,j+2,t))])

					cnf.append([-vpool.id((i,j,t,"r")), -vpool.id((i,j+1,t+1))])
					cnf.append([-vpool.id((i,j,t,"r")), vpool.id((i,j+2,t+1))])

				if (i+2, j) in plateau and (i+1, j) in plateau and (i,j) in plateau:
					# Down
					cnf.append([-vpool.id((i,j,t,"d")), vpool.id((i+1,j,t))])
					cnf.append([-vpool.id((i,j,t,"d")), -vpool.id((i+2,j,t))])

					cnf.append([-vpool.id((i,j,t,"d")), -vpool.id((i+1,j,t+1))])
					cnf.append([-vpool.id((i,j,t,"d")), vpool.id((i+2,j,t+1))])

				if (i, j-2) in plateau and (i, j-1) in plateau and (i,j) in plateau:
					# Left
					cnf.append([-vpool.id((i,j,t,"l")), vpool.id((i,j-1,t))])
					cnf.append([-vpool.id((i,j,t,"l")), -vpool.id((i,j-2,t))])

					cnf.append([-vpool.id((i,j,t,"l")), -vpool.id((i,j-1,t+1))])
					cnf.append([-vpool.id((i,j,t,"l")), vpool.id((i,j-2,t+1))])

	# Lorsqu'un mouvement est effectué sur 3 billes, les autres billes ne sont pas impactés
	for t in range(nb_billes-1):
		for i in range(hauteur):
			for j in range(largeur):
				for x in range(hauteur):
						for y in range(largeur):
							if (i-2, j) in plateau and (i-1, j) in plateau and (i,j) in plateau and (x,y) in plateau:
								# Up
								# Cijt"u" -> (Xi'j't <-> Xi'j't+1)
								if (y != j or (x != i and x != i-1 and x != i-2)):
									cnf.append([-vpool.id((i,j,t,"u")),-vpool.id((x,y,t)),vpool.id((x,y,t+1))])

									cnf.append([-vpool.id((i,j,t,"u")),-vpool.id((x,y,t+1)),vpool.id((x,y,t))])

							if (i, j+2) in plateau and (i, j+1) in plateau and (i,j) in plateau and (x,y) in plateau:
								# Right
								# Cijt"r" -> (Xi'j't <-> Xi'j't+1)
								if (x != i or (y != j and y != j+1 and y != j+2)):
									cnf.append([-vpool.id((i,j,t,"r")),-vpool.id((x,y,t)),vpool.id((x,y,t+1))])

									cnf.append([-vpool.id((i,j,t,"r")),-vpool.id((x,y,t+1)),vpool.id((x,y,t))])

							if (i+2, j) in plateau and (i+1, j) in plateau and (i,j) in plateau and (x,y) in plateau:
								# Down
								# Cijt"d" -> (Xi'j't <-> Xi'j't+1)
								if (y != j or (x != i and x != i+1 and x != i+2)):
									cnf.append([-vpool.id((i,j,t,"d")),-vpool.id((x,y,t)),vpool.id((x,y,t+1))])

									cnf.append([-vpool.id((i,j,t,"d")),-vpool.id((x,y,t+1)),vpool.id((x,y,t))])

							if (i, j-2) in plateau and (i, j-1) in plateau and (i,j) in plateau and (x,y) in plateau:
								# Left
								# Cijt"l" -> (Xi'j't <-> Xi'j't+1)
								if (x != i or (y != j and y != j-1 and y != j-2)):
									cnf.append([-vpool.id((i,j,t,"l")),-vpool.id((x,y,t)),vpool.id((x,y,t+1))])

									cnf.append([-vpool.id((i,j,t,"l")),-vpool.id((x,y,t+1)),vpool.id((x,y,t))])

	# On ne peut pas sortir du plateau avec un mouvement
	# Si la case d'arrivée ou la case intermédiaire est hors du plateau, alors le mouvement ne peut pas être effectué
	for t in range(nb_billes):
		for i in range(hauteur):
			for j in range(largeur):
				if (i,j) in plateau:
					if (i-2, j) not in plateau or (i-1, j) not in plateau:
						cnf.append([-vpool.id((i,j,t,"u"))]) # -Cijt"u" pour (i,j),(i-1),(1-2) pas dans le plateau
					if (i, j+2) not in plateau or (i, j+1) not in plateau:
						cnf.append([-vpool.id((i,j,t,"r"))])
					if (i+2, j) not in plateau or (i+1, j) not in plateau:
						cnf.append([-vpool.id((i,j,t,"d"))])
					if (i, j-2) not in plateau or (i, j-1) not in plateau:
						cnf.append([-vpool.id((i,j,t,"l"))])
	
	# Si une case a changé d'état, alors un mouvement l'a affecté
	for t in range(nb_billes-1):
		for i in range(hauteur):
			for j in range(largeur):
				if (i,j) in plateau:
					# Si une case disparait d'un instant à l'autre, alors c'est qu'elle est la source ou l'intermédiaire d'un mouvement
					# (Xijt & -Xijt+1) -> (Cijt"u" v Ci+1jt"u" v Cijt"r" v Cij-1t"r" v Cijt"d" v Ci-1jt"d" v Cijt"l" v Cij+1t"l")
					mylist = [-vpool.id((i,j,t)), vpool.id((i,j,t+1))]
					if (i, j-2) in plateau and (i, j-1) in plateau:
						mylist.append(vpool.id((i,j,t,"l")))
					if (i, j-1) in plateau and (i, j+1) in plateau:
						mylist.append(vpool.id((i,j+1,t,"l")))
					if (i-2, j) in plateau and (i-1, j) in plateau:
						mylist.append(vpool.id((i,j,t,"u")))
					if (i-1, j) in plateau and (i+1, j) in plateau:
						mylist.append(vpool.id((i+1,j,t,"u")))
					if (i, j+2) in plateau and (i, j+1) in plateau:
						mylist.append(vpool.id((i,j,t,"r")))
					if (i, j+1) in plateau and (i, j-1) in plateau:
						mylist.append(vpool.id((i,j-1,t,"r")))
					if (i+2, j) in plateau and (i+1, j) in plateau:
						mylist.append(vpool.id((i,j,t,"d")))
					if (i+1, j) in plateau and (i-1, j) in plateau:
						mylist.append(vpool.id((i-1,j,t,"d")))
					cnf.append(mylist)

					# Si une case apparait d'un instant à l'autre, alors c'est qu'elle est la destination d'un mouvement
					# (-Xijt & Xijt+1) -> (Ci+2jt"u" v Cij-2t"r" v Ci-2jt"d" v Cij+2t"l")
					mylist = [vpool.id((i,j,t)), -vpool.id((i,j,t+1))]
					if (i, j+2) in plateau and (i, j+1) in plateau:
						mylist.append(vpool.id((i,j+2,t,"l")))
					if (i+2, j) in plateau and (i+1, j) in plateau:
						mylist.append(vpool.id((i+2,j,t,"u")))
					if (i, j-2) in plateau and (i, j-1) in plateau:
						mylist.append(vpool.id((i,j-2,t,"r")))
					if (i-2, j) in plateau and (i-1, j) in plateau:
						mylist.append(vpool.id((i-2,j,t,"d")))
					cnf.append(mylist)


	"""
	===========================
		Résolution
	===========================
	"""

	s = Minisat22(use_timer=True)
	s.append_formula(cnf.clauses, no_return=False)

	print()
	print("=====================================")
	print("Resolution...")
	resultat = s.solve()
	print("Satisfaisable : " + str(resultat))
	print("Temps de resolution : " + '{0:.2f}s'.format(s.time()))

	if not resultat :
		print("-------------------------------------")
		return False
	else:
		for i in range(hauteur):
			for j in range(largeur):
				if (i,j) not in plateau:
					print("*",end="")
				else:
					if mode == 1:
						if vpool.id((i,j,nb_billes-nb_billes_restantes)) in s.get_model():
							print(1, end="")
						else:
							print(0, end="")
					elif mode == 2 or mode == 3:
						if vpool.id((i,j,nb_billes-1)) in s.get_model():
							print(1, end="")
						else:
							print(0, end="")
					else:
						print("Wrong mode provided")
			print()

		print("-------------------------------------")
		return True
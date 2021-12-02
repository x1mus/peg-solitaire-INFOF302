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
	nb_billes_restantes = 0
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

	i = 0
	for ligne in attendu:
		for case in ligne:
			if case == 1:
				nb_billes_restantes += 1

	
	taille_plateau = len(plateau)
	largeur = len(disposition[0])
	hauteur = len(disposition)
	mouvement = ["u", "r", "d", "l"] # Up / Right / Down / Left

	vpool = IDPool(start_from=1)
	cnf = CNF()

	"""
	print("Voici les coordonnées du plateau :", plateau)
	print("Le plateau fait :", taille_plateau, "cases.")
	print("Il y a :", nb_billes, "billes.")"""

	"""
	===========================
		Clauses
	===========================
	"""
	# Prise en compte de la configuration initiale
	#print("Configuration initiale :")
	#print("========================")
	for i in range(hauteur):
		for j in range(largeur):
			if (i,j) in plateau:
				if disposition[i][j] == 0:
					#print("-X" + str(i) + str(j) + str(0))
					cnf.append([-vpool.id((i,j,0))]) # Si la case ne contient pas de bille alors : -Xij0
				elif disposition[i][j] == 1:
					#print("X" + str(i) + str(j) + str(0))
					cnf.append([vpool.id((i,j,0))]) # Si la case contient une bille alors : Xij0


	# Prise en compte de la configuration finale (il ne reste plus qu'une seule bille)
		# Xijb-1 -> -Xi'j'b-1
	#print("Configuration finale :")
	#print("======================")
	"""for i in range(hauteur):
		for j in range(largeur):
			for x in range(hauteur):
				for y in range(largeur):
					if (i,j) != (x,y) and (i,j) in plateau and (x,y) in plateau:
						#print("X" + str(i) + str(j) + str(nb_billes-1) + " --> -X" + str(x) + str(y) + str(nb_billes-1))
						cnf.append([-vpool.id((i,j,nb_billes-1)), -vpool.id((x,y,nb_billes-1))])"""

	# Prise en compte config finale 2
	for i in range(hauteur):
		for j in range(largeur):
			if (i,j) in plateau:
				if attendu[i][j] == 1:
					cnf.append([vpool.id((i,j,nb_billes-nb_billes_restantes))])
				else:
					cnf.append([-vpool.id((i,j,nb_billes-nb_billes_restantes))])

	# Au plus un mouvement à la fois
		# Cijtm -> -Ci'j'tm'
	#print("Au + un mouvement à la fois :")
	#print("=============================")
	for t in range(nb_billes):
		for i in range(hauteur):
			for j in range(largeur):
				for m in mouvement:
					for x in range(hauteur):
						for y in range(largeur):
							for n in mouvement:
								if (i, j, m) != (x, y, n) and (i,j) in plateau and (x,y) in plateau:
									#print("C" + str(i) + str(j) + str(t) + str(m) + " --> -C" + str(x) + str(y) + str(t) + str(n))
									cnf.append([-vpool.id((i,j,t,m)), -vpool.id((x,y,t,n))])

	# Mise à jour des variables en fonction des mouvements
	#print("Mise à jour des variables en fonction des mouvements :")
	#print("======================================================")
	for t in range(nb_billes-1):
		for i in range(hauteur):
			for j in range(largeur):
				for m in mouvement:
					if (i,j) in plateau:
						# Cijtm -> -Xijt+1
						#print("C" + str(i) + str(j) + str(t) + str(m) + " --> -X" + str(i) + str(j) + str(t+1))
						cnf.append([-vpool.id((i,j,t,m)), -vpool.id((i,j,t+1))]) # Plus de bille à l'instant suivant si déplacement
						# Cijtm -> Xijt
						#print("C" + str(i) + str(j) + str(t) + str(m) + " --> X" + str(i) + str(j) + str(t))
						cnf.append([-vpool.id((i,j,t,m)), vpool.id((i,j,t))]) # Il fallait une bille pour faire le déplacement

	# Déplacements
	for t in range(nb_billes-1):
		for i in range(hauteur):
			for j in range(largeur):
				if (i-2, j) in plateau and (i-1, j) in plateau and (i,j) in plateau:
					# Up
					# Cijt"u" -> Xi-1jt
					#print("C" + str(i) + str(j) + str(t) + str("u") + " --> X" + str(i-1) + str(j) + str(t))
					cnf.append([-vpool.id((i,j,t,"u")), vpool.id((i-1,j,t))]) # Il doit y avoir une bille sur la case du dessus

					# Cijt"u" -> -Xi-2jt
					#print("C" + str(i) + str(j) + str(t) + str("u") + " --> -X" + str(i-2) + str(j) + str(t))
					cnf.append([-vpool.id((i,j,t,"u")), -vpool.id((i-2,j,t))]) # Il ne doit pas y avoir de billes deux cases au dessus
					
					# Cijt"u" -> -Xi-1jt+1
					#print("C" + str(i) + str(j) + str(t) + str("u") + " --> -X" + str(i-1) + str(j) + str(t+1))
					cnf.append([-vpool.id((i,j,t,"u")), -vpool.id((i-1,j,t+1))]) # A l'instant suivant, il n'y a plus de bille au dessus
					
					# Cijt"u" -> Xi-2jt+1
					#print("C" + str(i) + str(j) + str(t) + str("u") + " --> X" + str(i-2) + str(j) + str(t+1))
					cnf.append([-vpool.id((i,j,t,"u")), vpool.id((i-2,j,t+1))]) # A l'instant suivant, il y a une bille deux cases au dessus

				if (i, j+2) in plateau and (i, j+1) in plateau and (i,j) in plateau:
					# Right
					#print("C" + str(i) + str(j) + str(t) + str("r") + " --> X" + str(i) + str(j+1) + str(t))
					cnf.append([-vpool.id((i,j,t,"r")), vpool.id((i,j+1,t))])
					#print("C" + str(i) + str(j) + str(t) + str("r") + " --> -X" + str(i) + str(j+2) + str(t))
					cnf.append([-vpool.id((i,j,t,"r")), -vpool.id((i,j+2,t))])

					#print("C" + str(i) + str(j) + str(t) + str("r") + " --> -X" + str(i) + str(j+1) + str(t+1))
					cnf.append([-vpool.id((i,j,t,"r")), -vpool.id((i,j+1,t+1))])
					#print("C" + str(i) + str(j) + str(t) + str("r") + " --> X" + str(i) + str(j+2) + str(t+1))
					cnf.append([-vpool.id((i,j,t,"r")), vpool.id((i,j+2,t+1))])

				if (i+2, j) in plateau and (i+1, j) in plateau and (i,j) in plateau:
					# Down
					#print("C" + str(i) + str(j) + str(t) + str("d") + " --> X" + str(i+1) + str(j) + str(t))
					cnf.append([-vpool.id((i,j,t,"d")), vpool.id((i+1,j,t))])
					#print("C" + str(i) + str(j) + str(t) + str("d") + " --> -X" + str(i+2) + str(j) + str(t))
					cnf.append([-vpool.id((i,j,t,"d")), -vpool.id((i+2,j,t))])

					#print("C" + str(i) + str(j) + str(t) + str("d") + " --> -X" + str(i+1) + str(j) + str(t+1))
					cnf.append([-vpool.id((i,j,t,"d")), -vpool.id((i+1,j,t+1))])
					#print("C" + str(i) + str(j) + str(t) + str("d") + " --> X" + str(i+2) + str(j) + str(t+1))
					cnf.append([-vpool.id((i,j,t,"d")), vpool.id((i+2,j,t+1))])

				if (i, j-2) in plateau and (i, j-1) in plateau and (i,j) in plateau:
					# Left
					#print("C" + str(i) + str(j) + str(t) + str("l") + " --> X" + str(i) + str(j-1) + str(t))
					cnf.append([-vpool.id((i,j,t,"l")), vpool.id((i,j-1,t))])
					#print("C" + str(i) + str(j) + str(t) + str("l") + " --> -X" + str(i) + str(j-2) + str(t))
					cnf.append([-vpool.id((i,j,t,"l")), -vpool.id((i,j-2,t))])

					#print("C" + str(i) + str(j) + str(t) + str("l") + " --> -X" + str(i) + str(j-1) + str(t+1))
					cnf.append([-vpool.id((i,j,t,"l")), -vpool.id((i,j-1,t+1))])
					#print("C" + str(i) + str(j) + str(t) + str("l") + " --> X" + str(i) + str(j-2) + str(t+1))
					cnf.append([-vpool.id((i,j,t,"l")), vpool.id((i,j-2,t+1))])

	# Lorsqu'un mouvement est effectué sur 3 billes, les autres billes ne sont pas impactés
	#print("Les autres billes ne sont pas impactées :")
	#print("=========================================")
	for t in range(nb_billes-1):
		for i in range(hauteur):
			for j in range(largeur):
				for x in range(hauteur):
						for y in range(largeur):
							if (i-2, j) in plateau and (i-1, j) in plateau and (i,j) in plateau and (x,y) in plateau:
								# Up
								# Cijt"u" -> (Xi'j't <-> Xi'j't+1)
								if (y != j or (x != i and x != i-1 and x != i-2)):
									#print("C" + str(i) + str(j) + str(t) + str("u") + " --> (X" + str(x) + str(y) + str(t) + " <-> X" + str(x) + str(y) + str(t+1) + ")")
									cnf.append([-vpool.id((i,j,t,"u")),-vpool.id((x,y,t)),vpool.id((x,y,t+1))])

									cnf.append([-vpool.id((i,j,t,"u")),-vpool.id((x,y,t+1)),vpool.id((x,y,t))])

							if (i, j+2) in plateau and (i, j+1) in plateau and (i,j) in plateau and (x,y) in plateau:
								# Right
								if (x != i or (y != j and y != j+1 and y != j+2)):
									#print("C" + str(i) + str(j) + str(t) + str("r") + " --> (X" + str(x) + str(y) + str(t) + " <-> X" + str(x) + str(y) + str(t+1) + ")")
									cnf.append([-vpool.id((i,j,t,"r")),-vpool.id((x,y,t)),vpool.id((x,y,t+1))])

									cnf.append([-vpool.id((i,j,t,"r")),-vpool.id((x,y,t+1)),vpool.id((x,y,t))])

							if (i+2, j) in plateau and (i+1, j) in plateau and (i,j) in plateau and (x,y) in plateau:
								# Down
								if (y != j or (x != i and x != i+1 and x != i+2)):
									#print("C" + str(i) + str(j) + str(t) + str("d") + " --> (X" + str(x) + str(y) + str(t) + " <-> X" + str(x) + str(y) + str(t+1) + ")")
									cnf.append([-vpool.id((i,j,t,"d")),-vpool.id((x,y,t)),vpool.id((x,y,t+1))])

									cnf.append([-vpool.id((i,j,t,"d")),-vpool.id((x,y,t+1)),vpool.id((x,y,t))])

							if (i, j-2) in plateau and (i, j-1) in plateau and (i,j) in plateau and (x,y) in plateau:
								# Left
								if (x != i or (y != j and y != j-1 and y != j-2)):
									#print("C" + str(i) + str(j) + str(t) + str("l") + " --> (X" + str(x) + str(y) + str(t) + " <-> X" + str(x) + str(y) + str(t+1) + ")")
									cnf.append([-vpool.id((i,j,t,"l")),-vpool.id((x,y,t)),vpool.id((x,y,t+1))])

									cnf.append([-vpool.id((i,j,t,"l")),-vpool.id((x,y,t+1)),vpool.id((x,y,t))])

	# On ne peut pas sortir du plateau avec un mouvement
	# Si la case d'arrivée est hors du plateau, le mouvement ne peut pas être effectué
	#print("Désactivation des mouvements illégaux :")
	#print("=======================================")
	for t in range(nb_billes):
		for i in range(hauteur):
			for j in range(largeur):
				if (i,j) in plateau:
					if (i-2, j) not in plateau or (i-1, j) not in plateau:
						#print("-C" + str(i) + str(j) + str(t) + "u")
						cnf.append([-vpool.id((i,j,t,"u"))])
					if (i, j+2) not in plateau or (i, j+1) not in plateau:
						#print("-C" + str(i) + str(j) + str(t) + "r")
						cnf.append([-vpool.id((i,j,t,"r"))])
					if (i+2, j) not in plateau or (i+1, j) not in plateau:
						#print("-C" + str(i) + str(j) + str(t) + "d")
						cnf.append([-vpool.id((i,j,t,"d"))])
					if (i, j-2) not in plateau or (i, j-1) not in plateau:
						#print("-C" + str(i) + str(j) + str(t) + "l")
						cnf.append([-vpool.id((i,j,t,"l"))])
	
	# Si une case a changé d'état, alors un mouvement l'a affecté
	# ((Xijt & -Xijt+1) v (-Xijt & Xijt+1)) -> (
		# Cijt"u" v Ci+1jt"u" v Ci+2jt"u"
		# v Cijt"r" v Cij-1t"r" v Cij-2t"r"
		# v Cijt"d" v Ci-1jt"d" v Ci-2jt"d"
		# v Cijt"l" v Cij+1t"l" v Cij+2t"l"
	#)
	#print("Si une case a changé, alors un mouvement l'a affectée :")
	#print("=======================================================")
	for t in range(nb_billes-1):
		for i in range(hauteur):
			for j in range(largeur):
				if (i,j) in plateau:
					mylist = [-vpool.id((i,j,t)), vpool.id((i,j,t+1))]
					myprint = "((X" + str(i) + str(j) + str(t) + " & -X" + str(i) + str(j) + str(t+1) + ") v (-X" + str(i) + str(j) + str(t) + " & X" + str(i) + str(j) + str(t+1) + ")) --> ("
					if (i, j-2) in plateau:
						mylist.append(vpool.id((i,j,t,"l")))
						myprint += "C" + str(i) + str(j) + str(t) + "l v "
					if (i, j-1) in plateau and (i, j+1) in plateau:
						mylist.append(vpool.id((i,j+1,t,"l")))
						myprint += "C" + str(i) + str(j+1) + str(t) + "l v "
					if (i-2, j) in plateau:
						mylist.append(vpool.id((i,j,t,"u")))
						myprint += "C" + str(i) + str(j) + str(t) + "u v "
					if (i-1, j) in plateau and (i+1, j) in plateau:
						mylist.append(vpool.id((i+1,j,t,"u")))
						myprint += "C" + str(i+1) + str(j) + str(t) + "u v "
					if (i, j+2) in plateau:
						mylist.append(vpool.id((i,j,t,"r")))
						myprint += "C" + str(i) + str(j) + str(t) + "r v "
					if (i, j+1) in plateau and (i, j-1) in plateau:
						mylist.append(vpool.id((i,j-1,t,"r")))
						myprint += "C" + str(i) + str(j-1) + str(t) + "r v "
					if (i+2, j) in plateau:
						mylist.append(vpool.id((i,j,t,"d")))
						myprint += "C" + str(i) + str(j) + str(t) + "d v "
					if (i+1, j) in plateau and (i-1, j) in plateau:
						mylist.append(vpool.id((i-1,j,t,"d")))
						myprint += "C" + str(i-1) + str(j) + str(t) + "d v "
					cnf.append(mylist)

					mylist = [vpool.id((i,j,t)), -vpool.id((i,j,t+1))]
					if (i, j) in plateau:
						mylist.append(vpool.id((i,j+2,t,"l")))
						myprint += "C" + str(i) + str(j+2) + str(t) + "l v "
					if (i, j) in plateau:
						mylist.append(vpool.id((i+2,j,t,"u")))
						myprint += "C" + str(i+2) + str(j) + str(t) + "u v "
					if (i, j) in plateau:
						mylist.append(vpool.id((i,j-2,t,"r")))
						myprint += "C" + str(i) + str(j-2) + str(t) + "r v "
					if (i, j) in plateau:
						mylist.append(vpool.id((i-2,j,t,"d")))
						myprint += "C" + str(i-2) + str(j) + str(t) + "d"
					cnf.append(mylist)
					myprint += ")"

					#print(myprint)


	"""
	===========================
		Résolution
	===========================
	"""

	s = Minisat22(use_timer=True)
	s.append_formula(cnf.clauses, no_return=False)
	#print(cnf.clauses)
	#print(s.get_model())
	
	print("====================")
	print("Resolution...")
	resultat = s.solve()
	print("satisfaisable : " + str(resultat))

	print("Temps de resolution : " + '{0:.2f}s'.format(s.time()))

	if resultat:
		computed = []
		"""for t in range(nb_billes):
			print("Instant:", t)"""
		for i in range(hauteur):
			line = []
			for j in range(largeur):
				if (i,j) not in plateau:
					print("*",end="")
					line.append(-1)
				else:
					if vpool.id((i,j,nb_billes-nb_billes_restantes)) in s.get_model():
						print(1, end="")
						line.append(1)
					else:
						print(0, end="")
						line.append(0)
			computed.append(line)
			print()

		#print(computed)
		print("--------------------")
		return computed == attendu
from projet import solution

def display_matrix(m):
	i = 0
	while i < len(m):
		j = 0
		while j < len(m[0]):
			if m[i][j] == -1:
				print("*", end="")
			else:
				print(m[i][j], end="")
			j += 1

		print()
		i += 1

def display_matrixes(disposition, attendu):
	"""Cette fonction affiche les deux matrices l'une à côté de l'autre dans un format lisible.
	"""
	i = 0
	while i < len(disposition):
		j = 0
		while j < len(disposition[0]):
			if disposition[i][j] == -1:
				print("*", end="")
			else:
				print(disposition[i][j], end="")
			j += 1

		print(" ", end="")

		j = 0
		while j < len(attendu[0]):
			if attendu[i][j] == -1:
				print("*", end="")
			else:
				print(attendu[i][j], end="")
			j += 1

		print()
		i += 1


def question12():
	print()
	print("##############################")
	print("         QUESTION 1/2         ")
	print("##############################")
	print()

	l = [[[[1,0,0],[1,0,0],[0,1,0]],[[0,0,0],[0,0,0],[0,0,1]]],[[[-1,1,-1],[-1,1,-1],[-1,0,-1]],[[-1,0,-1],[-1,0,-1],[-1,1,-1]]],[[[0,1,0,-1],[1,1,1,1],[0,-1,1,1]],[[0,0,0,-1],[0,1,0,1],[1,-1,0,1]]],[[[-1,-1,-1,1,-1,-1,-1],[-1,-1,0,1,0,-1,-1],[-1,0,0,0,1,0,-1],[1,1,0,0,0,1,0],[0,0,1,0,1,0,0],[-1,1,0,0,0,0,-1],[-1,-1,0,0,0,-1,-1],[-1,-1,-1,0,-1,-1,-1]],[[-1,-1,-1,0,-1,-1,-1],[-1,-1,0,0,0,-1,-1],[-1,0,0,0,0,0,-1],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[-1,0,0,0,0,0,-1],[-1,-1,0,0,0,-1,-1],[-1,-1,-1,0,-1,-1,-1],]],[[[-1,-1,0,0,0,-1,-1],[-1,0,0,1,0,0,-1],[0,0,1,0,1,0,0],[1,1,0,1,0,0,0],[0,0,1,0,0,1,1],[-1,1,1,0,0,0,-1],[-1,-1,0,0,0,-1,-1],],[[-1,-1,0,0,0,-1,-1],[-1,0,0,1,0,0,-1],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[-1,0,1,1,0,0,-1],[-1,-1,0,0,0,-1,-1]]]]
	s = [[[[1,0],[1,0]],[[0,1],[0,0]]],[[[1,1,0],[1,1,0],[0,0,1]],[[0,0,0],[0,1,0],[1,0,1]]],[[[1,0,-1,1],[1,-1,0,1],[1,1,0,0],[1,0,-1,1]],[[1,0,-1,0],[1,-1,0,1],[0,0,0,0],[0,0,-1,0]]],[[[-1,1,1,-1],[1,0,1,1],[1,1,1,1],[-1,1,1,-1]],[[-1,0,0,-1],[0,1,0,0],[0,0,0,0],[-1,0,0,-1]]]]
	m1=[[[-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,1,1,1,1],[-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1]],[[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1]]]
	m2=[[[-1,1,1,1,-1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1],[-1,1,1,1,-1]],[[-1,0,0,0,-1],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[-1,0,0,0,-1]]]

	for m in l:
		if not solution(m[0], m[1]):
			print("Votre programme échoue sur le couple :")
		else:
			print("Votre programme marche sur le couple :")
		display_matrixes(m[0],m[1])
	
	for m in s:
		if solution(m[0], m[1]):
			print("Votre programme échoue sur le couple :")
		else:
			print("Votre programme marche sur le couple :")
		display_matrixes(m[0],m[1])
	
	if not solution(m1[0], m1[1]):
		print("Votre programme échoue sur le couple :")
	else:
		print("Votre programme marche sur le couple :")
	display_matrixes(m1[0],m1[1])
	
	if solution(m2[0], m2[1]):
		print("Votre programme échoue sur le couple :")
	else:
		print("Votre programme marche sur le couple :")
	display_matrixes(m2[0],m2[1])


def question3(mlist):
	print()
	print("##############################")
	print("          QUESTION 3          ")
	print("##############################")
	print()

	for m in mlist:
		if solution(m, mode=3):
			print("Votre programme marche sur la matrice :")
		else:
			print("Votre programme échoue sur la matrice :")
		display_matrix(m)


def question4(mlist):
	print()
	print("##############################")
	print("          QUESTION 4          ")
	print("##############################")
	print()

	for m in mlist:
		if solution(m, mode=2):
			print("Votre programme marche sur la matrice :")
		else:
			print("Votre programme échoue sur la matrice :")
		display_matrix(m)


def question5(m):
	print()
	print("##############################")
	print("          QUESTION 5          ")
	print("##############################")
	print()

	new = []
	i = 0
	for ligne in m:
		j = 0
		new.append([])
		for case in ligne:
			if case == -1:
				new[i].append(case)
			else:
				m[i][j] = 0 # On assigne le trou au premier emplacement possible
				if solution(m, mode=3): # On vérifie que cela est SAT
					new[i].append(1) # Si oui, on ajoute 1 dans la nouvelle matrice
				else:
					new[i].append(0)
				m[i][j] = 1
			j += 1
		i += 1

	print()
	print("Voici les endroits où les trous peuvent être positionnés")
	display_matrix(new) # On affiche la matrice regroupant les coups possibles


def main():
	generalized_cross_boards = [
		[
			[-1,-1,1,1,1,-1,-1],
			[1,1,1,1,1,1,1],
			[1,1,1,0,1,1,1],
			[1,1,1,1,1,1,1],
			[-1,-1,1,1,1,-1,-1]
		],[
			[-1,-1,1,1,1,-1,-1],
			[1,1,1,1,1,1,1],
			[1,1,1,0,1,1,1],
			[1,1,1,1,1,1,1]
		],[
			[-1,1,1,1,-1,-1],
			[-1,1,1,1,-1,-1],
			[1,1,1,1,1,1],
			[0,1,1,1,1,1],
			[1,1,1,1,1,1],
			[-1,1,1,1,-1,-1]
		],[
			[1,1,1,-1,-1],
			[1,1,1,-1,-1],
			[1,1,1,1,1],
			[1,1,1,1,1],
			[1,1,0,1,1],
			[1,1,1,-1,-1]
		]
	]

	figure1 = [
		[
			[-1,-1,1,1,1,-1,-1], # 1.1 Plateau européen
			[-1,1,1,1,1,1,-1],
			[1,1,1,0,1,1,1],
			[1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1],
			[-1,1,1,1,1,1,-1],
			[-1,-1,1,1,1,-1,-1]
		],[
			[-1,-1,-1,1,1,1,-1,-1,-1], # 1.2 Plateau allemand
			[-1,-1,-1,1,1,1,-1,-1,-1],
			[-1,-1,-1,1,1,1,-1,-1,-1],
			[1,1,1,1,1,1,1,1,1],
			[1,1,1,1,0,1,1,1,1],
			[1,1,1,1,1,1,1,1,1],
			[-1,-1,-1,1,1,1,-1,-1,-1],
			[-1,-1,-1,1,1,1,-1,-1,-1],
			[-1,-1,-1,1,1,1,-1,-1,-1]
		],[
			[-1,-1,1,1,1,-1,-1,-1], # 1.3 Plateau asymétrique
			[-1,-1,1,1,1,-1,-1,-1],
			[-1,-1,1,1,1,-1,-1,-1],
			[1,1,1,1,1,1,1,1],
			[1,1,1,0,1,1,1,1],
			[1,1,1,1,1,1,1,1],
			[-1,-1,1,1,1,-1,-1,-1],
			[-1,-1,1,1,1,-1,-1,-1]
		],[
			[-1,-1,1,1,1,-1,-1], # 1.4 Plateau anglais
			[-1,-1,1,1,1,-1,-1],
			[1,1,1,1,1,1,1],
			[1,1,1,0,1,1,1],
			[1,1,1,1,1,1,1],
			[-1,-1,1,1,1,-1,-1],
			[-1,-1,1,1,1,-1,-1]
		],[
			[-1,-1,-1,-1,1,-1,-1,-1,-1], # 1.5 Plateau en diamant
			[-1,-1,-1,1,1,1,-1,-1,-1],
			[-1,-1,1,1,1,1,1,-1,-1],
			[-1,1,1,1,1,1,1,1,-1],
			[1,1,1,1,0,1,1,1,1],
			[-1,1,1,1,1,1,1,1,-1],
			[-1,-1,1,1,1,1,1,-1,-1],
			[-1,-1,-1,1,1,1,-1,-1,-1],
			[-1,-1,-1,-1,1,-1,-1,-1,-1]
		]
	]

	q5_m = [
		[1,1,1,1,1],
		[1,1,1,1,1],
		[1,1,1,1,1],
		[1,1,1,-1,-1]
	]

	"""question12()

	question3(generalized_cross_boards)
	question3([figure1[2], figure1[3]]) # Temps raisonnable pour 1.3 et 1.4

	question4(generalized_cross_boards)
	question4([figure1[0], figure1[2]]) # Temps raisonnable pour 1.1 et 1.3"""

	question5(q5_m) # Obligation de fournir une matrice ne contenant que des billes afin de tester les différentes positions de trou initial

if __name__ == "__main__":
	main()
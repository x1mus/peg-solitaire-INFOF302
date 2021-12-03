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
	print("##############################")
	print("         QUESTION 1/2         ")
	print("##############################")

	l = [[[[1,0,0],[1,0,0],[0,1,0]],[[0,0,0],[0,0,0],[0,0,1]]],[[[-1,1,-1],[-1,1,-1],[-1,0,-1]],[[-1,0,-1],[-1,0,-1],[-1,1,-1]]],[[[0,1,0,-1],[1,1,1,1],[0,-1,1,1]],[[0,0,0,-1],[0,1,0,1],[1,-1,0,1]]],[[[-1,-1,-1,1,-1,-1,-1],[-1,-1,0,1,0,-1,-1],[-1,0,0,0,1,0,-1],[1,1,0,0,0,1,0],[0,0,1,0,1,0,0],[-1,1,0,0,0,0,-1],[-1,-1,0,0,0,-1,-1],[-1,-1,-1,0,-1,-1,-1]],[[-1,-1,-1,0,-1,-1,-1],[-1,-1,0,0,0,-1,-1],[-1,0,0,0,0,0,-1],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[-1,0,0,0,0,0,-1],[-1,-1,0,0,0,-1,-1],[-1,-1,-1,0,-1,-1,-1],]],[[[-1,-1,0,0,0,-1,-1],[-1,0,0,1,0,0,-1],[0,0,1,0,1,0,0],[1,1,0,1,0,0,0],[0,0,1,0,0,1,1],[-1,1,1,0,0,0,-1],[-1,-1,0,0,0,-1,-1],],[[-1,-1,0,0,0,-1,-1],[-1,0,0,1,0,0,-1],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[-1,0,1,1,0,0,-1],[-1,-1,0,0,0,-1,-1]]]]
	s = [[[[1,0],[1,0]],[[0,1],[0,0]]],[[[1,1,0],[1,1,0],[0,0,1]],[[0,0,0],[0,1,0],[1,0,1]]],[[[1,0,-1,1],[1,-1,0,1],[1,1,0,0],[1,0,-1,1]],[[1,0,-1,0],[1,-1,0,1],[0,0,0,0],[0,0,-1,0]]],[[[-1,1,1,-1],[1,0,1,1],[1,1,1,1],[-1,1,1,-1]],[[-1,0,0,-1],[0,1,0,0],[0,0,0,0],[-1,0,0,-1]]]]
	m1=[[[-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,1,1,1,1],[-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1]],[[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1]]]
	m2=[[[-1,1,1,1,-1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1],[-1,1,1,1,-1]],[[-1,0,0,0,-1],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[-1,0,0,0,-1]]]

	for m in l:
		if not solution(m[0], m[1], 1):
			print("Votre programme échoue sur le couple :")
		else:
			print("Votre programme marche sur le couple :")
		display_matrixes(m[0],m[1])
	
	for m in s:
		if solution(m[0], m[1], 1):
			print("Votre programme échoue sur le couple :")
		else:
			print("Votre programme marche sur le couple :")
		display_matrixes(m[0],m[1])
	
	if not solution(m1[0], m1[1], 1):
		print("Votre programme échoue sur le couple :")
	else:
		print("Votre programme marche sur le couple :")
	display_matrixes(m1[0],m1[1])
	
	if solution(m2[0], m2[1], 1):
		print("Votre programme échoue sur le couple :")
	else:
		print("Votre programme marche sur le couple :")
	display_matrixes(m2[0],m2[1])


def question3(mlist):
	print("##############################")
	print("          QUESTION 3          ")
	print("##############################")

	for m in mlist:
		if solution(m, mode=3):
			print("Votre programme marche sur la matrice :")
		else:
			print("Votre programme échoue sur la matrice :")
		display_matrix(m)


def question4(mlist):
	print("##############################")
	print("          QUESTION 4          ")
	print("##############################")

	for m in mlist:
		if solution(m, mode=2):
			print("Votre programme marche sur la matrice :")
		else:
			print("Votre programme échoue sur la matrice :")
		display_matrix(m)


def main():
	#question12()

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

	#question3(generalized_cross_boards)
	question3([figure1[3]]) # Temps raisonnable pour 1.3

	#question4(generalized_cross_boards)
	#question4([figure1[0], figure1[2]]) # Temps raisonnable pour 1.1 et 1.3


if __name__ == "__main__":
	main()
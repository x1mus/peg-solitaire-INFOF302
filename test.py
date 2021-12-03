from projet import solution


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


def main():
	print("##############################")
	print("         QUESTION 1/2         ")
	print("##############################")

	"""l = [[[[1,0,0],[1,0,0],[0,1,0]],[[0,0,0],[0,0,0],[0,0,1]]],[[[-1,1,-1],[-1,1,-1],[-1,0,-1]],[[-1,0,-1],[-1,0,-1],[-1,1,-1]]],[[[0,1,0,-1],[1,1,1,1],[0,-1,1,1]],[[0,0,0,-1],[0,1,0,1],[1,-1,0,1]]],[[[-1,-1,-1,1,-1,-1,-1],[-1,-1,0,1,0,-1,-1],[-1,0,0,0,1,0,-1],[1,1,0,0,0,1,0],[0,0,1,0,1,0,0],[-1,1,0,0,0,0,-1],[-1,-1,0,0,0,-1,-1],[-1,-1,-1,0,-1,-1,-1]],[[-1,-1,-1,0,-1,-1,-1],[-1,-1,0,0,0,-1,-1],[-1,0,0,0,0,0,-1],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[-1,0,0,0,0,0,-1],[-1,-1,0,0,0,-1,-1],[-1,-1,-1,0,-1,-1,-1],]],[[[-1,-1,0,0,0,-1,-1],[-1,0,0,1,0,0,-1],[0,0,1,0,1,0,0],[1,1,0,1,0,0,0],[0,0,1,0,0,1,1],[-1,1,1,0,0,0,-1],[-1,-1,0,0,0,-1,-1],],[[-1,-1,0,0,0,-1,-1],[-1,0,0,1,0,0,-1],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[-1,0,1,1,0,0,-1],[-1,-1,0,0,0,-1,-1]]]]
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
	display_matrixes(m2[0],m2[1])"""


	print()
	print("##############################")
	print("          QUESTION 3          ")
	print("##############################")

	generalized_cross_boards = [
		[
			[-1, 1, 1, 1, -1,-1],
			[-1, 1, 1, 1, -1,-1],
			[1, 1, 1, 1, 1,1],
			[0, 1, 1, 1, 1,1],
			[1, 1, 1, 1, 1,1],
			[-1, 1, 1, 1, -1,-1]
		],
	]

	for m in generalized_cross_boards:
		solution(m)

	figure1 = [
		[
			[-1,-1,1,1,1,-1,-1], # Figure 1.1 (Plateau européen)
			[-1,1,1,1,1,1,-1],
			[1,1,1,0,1,1,1],
			[1,1,1,1,1,1,1],
			[1,1,1,1,1,1,1],
			[-1,1,1,1,1,1,-1],
			[-1,-1,1,1,1,-1,-1]
		],
		[
			[-1,-1,-1,1,1,1,-1,-1,-1], # Figure 1.2 (Plateau allemand)
			[-1,-1,-1,1,1,1,-1,-1,-1],
			[-1,-1,-1,1,1,1,-1,-1,-1],
			[1,1,1,1,1,1,1,1,1],
			[1,1,1,1,0,1,1,1,1],
			[1,1,1,1,1,1,1,1,1],
			[-1,-1,-1,1,1,1,-1,-1,-1],
			[-1,-1,-1,1,1,1,-1,-1,-1],
			[-1,-1,-1,1,1,1,-1,-1,-1]
		],
		[
			[-1,-1,1,1,1,-1,-1,-1], # Figure 1.3 (Plateau asymétrique)
			[-1,-1,1,1,1,-1,-1,-1],
			[-1,-1,1,1,1,-1,-1,-1],
			[1,1,1,1,1,1,1,1],
			[1,1,1,0,1,1,1,1],
			[1,1,1,1,1,1,1,1],
			[-1,-1,1,1,1,-1,-1,-1],
			[-1,-1,1,1,1,-1,-1,-1],
		],
		[
			[-1,-1,1,1,1,-1,-1], # Figure 1.4 (Plateau anglais)
			[-1,-1,1,1,1,-1,-1],
			[1,1,1,1,1,1,1],
			[1,1,1,0,1,1,1],
			[1,1,1,1,1,1,1],
			[-1,-1,1,1,1,-1,-1],
			[-1,-1,1,1,1,-1,-1]
		],
		[
			[-1,-1,-1,-1,1,-1,-1,-1,-1], # Figure 1.5 (Plateau en diamant)
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

	"""if solution(figure1[0], mode=3):
		print("Votre programme marche sur le plateau européen (Figure 1.1)")
	else:
		print("Votre programme échoue sur le plateau européen (Figure 1.1)")

	if solution(figure1[1], mode=3):
		print("Votre programme marche sur le plateau allemand (Figure 1.2)")
	else:
		print("Votre programme échoue sur le plateau allemand (Figure 1.2)")
	
	if solution(figure1[2], mode=3):
		print("Votre programme marche sur le plateau asymétrique (Figure 1.3)")
	else:
		print("Votre programme échoue sur le plateau asymétrique (Figure 1.3)")

	if solution(figure1[3], mode=3):
		print("Votre programme marche sur le plateau anglais (Figure 1.4)")
	else:
		print("Votre programme échoue sur le plateau anglais (Figure 1.4)")

	if solution(figure1[4], mode=3):
		print("Votre programme marche sur le plateau en diamant (Figure 1.5)")
	else:
		print("Votre programme échoue sur le plateau en diamant (Figure 1.5)")"""


	print()
	print("##############################")
	print("          QUESTION 4          ")
	print("##############################")


	"""if solution(figure1[0], 2):
		print("Votre programme marche sur le plateau européen (Figure 1.1)")
	else:
		print("Votre programme échoue sur le plateau européen (Figure 1.1)")

	if solution(figure1[1], 2):
		print("Votre programme marche sur le plateau allemand (Figure 1.2)")
	else:
		print("Votre programme échoue sur le plateau allemand (Figure 1.2)")
	
	if solution(figure1[2], 2):
		print("Votre programme marche sur le plateau asymétrique (Figure 1.3)")
	else:
		print("Votre programme échoue sur le plateau asymétrique (Figure 1.3)")

	if solution(figure1[3], 2):
		print("Votre programme marche sur le plateau anglais (Figure 1.4)")
	else:
		print("Votre programme échoue sur le plateau anglais (Figure 1.4)")

	if solution(figure1[4], 2):
		print("Votre programme marche sur le plateau en diamant (Figure 1.5)")
	else:
		print("Votre programme échoue sur le plateau en diamant (Figure 1.5)")"""


if __name__ == "__main__":
	main()
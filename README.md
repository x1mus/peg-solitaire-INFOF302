# PEG Solitaire
## Introduction
Ce projet a été réalisé dans le cadre du cours d'informatique fondamentale 2021-2022. Celui-ci a pour objectif la modélisation du jeu du peg solitaire via des formules de logiques sous FNC ainsi que sa résolution grâce à un solveur SAT.

## Pré-requis
Seul le paquet PySAT ainsi que ses dépendances sont nécessaires. Ces différents paquets peuvent être installé via la commande :
```bash
pip3 install -r requirements.txt
```

## Utilisation
Notre programme fonctionne selon les différentes questions imposées dans les consignes.
Les questions implémentées sont au nombre de 4 :
1. Passage d'une matrice M à une matrice M'
2. Résolution d'une matrice M avec une bille de fin peu importe son emplacement
3. Résolution d'une matrice M avec la bille de fin où se trouvait le trou du début
4. TO-DO (4)
```py
solution(m1, m2, mode=1)
solution(m, mode=2)
solution(m, mode=3)
```

### Résolution de la question 1 & 2
Cette partie de l'implémentation peu être exécutée totalement sans problème de temps car les différentes matrices sont fournies par le professeur.
Celle-ci est lancée grâce à la fonction :
```py
question12()
```

### Résolution de la question 3 & 4
Afin d'obtenir des résultats dans une limite de temps correcte, il n'est pas possible de fournir toutes les matrices à notre implémentation. C'est pourquoi celle-ci ne contient que certaines des matrices fournies ainsi que d'autres matrices ayant comme particularité d'être solvable avec le trou de départ à n'importe quel endroit.

Ces matrices ont été trouvées sur le site internet de [George I. Bell](http://www.gibell.net/pegsolitaire/GenCross/GenCrossBoards0.html)
Afin d'exécuter ces questions, il faut utiliser ces fonctions :
```py
question3([m1, m2, m3, m4, ...])
question4([m1, m2, m3, m4, ...])
```

## Exécution complète
L'exécution complète peut être lancée via la commande
```bash
python3 test.py
```

## Contributeurs
- **Laenen Maximilien**
- **Pembe Lemlin Nathan**
- **Perez Axelle**
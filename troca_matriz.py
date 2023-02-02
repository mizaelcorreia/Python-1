
"""
Escreva uma função que troca um elemento por outro numa matriz
"""
matriz = []
m = int(input("Digite o número de linhas da matriz: "))
n = int(input("Digite o número de colunas da matriz: "))

def constróiMatriz(m, n, matriz):
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            x = int(input("Digite o elemento %i%i da matriz: "%(i,j)))
            linha.append(x)

        matriz.append(linha)

def TrocaElemento(pos1, pos2, matriz):
    elemento1 = matriz[pos1//10 -1][pos1%10 -1]
    elemento2 = matriz[pos2//10 -1][pos2%10-1]
    matriz[pos1//10-1][pos1%10-1] = elemento2
    matriz[pos2//10-1][pos2%10-1] = elemento1

constróiMatriz(m, n, matriz)
print(matriz)
pos1 = int(input("Digite a posição do elemento 1: "))
pos2 = int(input("Digite a posição do elemento 2: "))
TrocaElemento(pos1, pos2, matriz)
print(matriz)

"""
matriz=[]

m=2
n=2

for i=1 até 2:
	linha=[]
	for j=1 até 2:

		x = [3,

		linha=[3,

	for j=2 até 2:

		x = [13,

		linha=[3,13]

	matriz= [[3,13]]

for i=2 até 2:
	linha=[]
	for j=2 até 2:

		x = [22

		linha=[22,

	for j=2 até 2:

		x = [56

		linha=[22,56]

	matriz=[[3,13],[22,56]]


****************2ª Parte***************

pos1 = 11
pos2 = 22

TrocaElemento(11,22,matriz)


****************2ª Função***************

elemento1 = matriz[0][0]= 3
elemento2 = matriz[1][1] = 56

matriz[0][0] = 56
matriz[1][1] = 3

matriz=[[3,13],[22,56]]"""
"""
Escreva uma função que recebe um inteiro m e outro n e com isso
constrói uma matriz mxn
"""

matriz = []
m = int(input("Digite o número de linhas da matriz: "))
n = int(input("Digite o número de colunas da matriz: "))

def constróiMatriz(m, n, matriz):
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            x = int(input("Digite o elemento [%i][%i] da matriz: "%(i,j)))
            linha.append(x)

        matriz.append(linha)

constróiMatriz(m, n, matriz)

print(matriz)

"""
****resolução****

m= 2
n=2

for i=1 até 2:
	linha=[]
	for 1 até 2:

		x[1][1]=4

		linha=[4, 
	for 2 até 2:

		x[1][2]=13

		linha=[4, 13]

	matriz=[4,13]

for i=2 até 2:
	linha=[]
	
	for 1 até 2:

		x[2][1]=40

		linha=[40

	for 2 até 2:

		x[2][2]=22

		linha=[40,22]

	matriz=[[4,13],[40,22]]

"""


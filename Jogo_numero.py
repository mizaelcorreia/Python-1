"""
Escreva o jogo dos números como descrito na aula. Utilize as funções escritas
em aula e mais três feitas agora:
    1 - VerificaSeVenceu: Recebe uma matriz 4x4 e verifica se os números estão
    ordenados de forma que o jogador venceu
    2 - VerificaJogada: Verifica se a jogada escolhida pelo usuário é válida
    3 - ImprimeJogo: Função que imprime o jogo na tela do usuário
Você pode fazer quantas funções adcionais quanto quiser

Organize o seu jogo dentro da função main. Dê para o usuário a toda rodada
a opção de desistir(0) ou de inserir uma posição(1), a posição inserida
será feita colocando a linha e coluna da matriz, por exemplo 11 significa que
estamos nos referenciando ao elemento da linha 1 coluna 1, 32 se referencia ao
elemento da linha 3 coluna 2
"""

import random

#############################################################
#   Funções Feitas em Aula                                  #
#############################################################

def TrocaElemento(pos1, pos2, matriz):
    elemento1 = matriz[pos1//10 -1][pos1%10 -1]
    elemento2 = matriz[pos2//10 -1][pos2%10-1]
    matriz[pos1//10-1][pos1%10-1] = elemento2
    matriz[pos2//10-1][pos2%10-1] = elemento1


def geraMatriz(matriz):
    lista = list(range(16))
    for j in range(4):
        linha = []
        for i in range(4):
            x = random.choice(lista)
            linha.append(x)
            lista.remove(x)
        matriz.append(linha)

#############################################################
#   Funções Propostas                                       #
#############################################################

def VerificaSeVenceu(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if ((4*i + j + 1) != matriz[i][j] and i != 3 and j != 3) or (i == 3 and j == 3 and matriz[i][j] != 0):
                return False

    return True

def VerificaJogada(pos, zero_pos):
    linha = pos//10
    coluna = pos%10

    linha_zero = zero_pos//10
    coluna_zero = zero_pos%10

    if linha < 1 or linha > 4 or coluna < 1 or coluna > 4:
        return False
    else:
        if (linha == linha_zero -1 and coluna == coluna_zero) or (linha == linha_zero and (coluna == coluna_zero-1 or coluna == coluna_zero+1)) or (linha == linha_zero+1 and coluna == coluna_zero):
            return True
        else:
            return False


def imprimeJogo(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

#############################################################
#   Funções Pessoais                                        #
#############################################################

def AchaPosZero(matriz):
    #Função que procura e devolve a posição do zero da matriz(espaço vazio)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 0:
                return (i+1)*10 + j+1

def fazJogada(jogo):
    #Imprime o jogo na tela e pergunta se o usuário quer continuar
    imprimeJogo(jogo)
    dec = bool(int(input("Deseja continuar(1) ou desistir(0): ")))
    return dec

#############################################################
#   Função Main                                             #
#############################################################

def main():
    jogo = []
    geraMatriz(jogo)

    venceu =False

    zero_pos = AchaPosZero(jogo)

    jogando = fazJogada(jogo)


    while jogando:
        pos = int(input("Digite a posição do elemento que você deseja trocar: "))

        while not VerificaJogada(pos, zero_pos):
            print("Entrada inválida. Digite novamente")
            pos = int(input("Digite a posição do elemento que você deseja trocar: "))

        TrocaElemento(pos, zero_pos, jogo)

        zero_pos = pos

        venceu = VerificaSeVenceu(jogo)
        jogando = not venceu

        if jogando:
            jogando = fazJogada(jogo)

    if venceu:
        print("Parabens, você venceu!!!")
    else:
        print("Obrigado por jogar.")

main()



"""

1 - Matriz 4x4, ordenar vencedor

2 - Jogada válida vencedor?

3 - função imprimir jogo

---------------------------------------------

Cada Rodada: 

0 - Desistir             1 - inserir posição, ex: 11,12,24

--------------------------------------------------------------

jogo = []
geraMatriz(jogo)
-------------------------------------------------------------
1ª função geraMatriz()

lista=[15 nº aleatórios]

for j=0 até 3:
	linha = []
	for i=0 até 3:
		x = [3,
		linha=[3,
		lista= [1,2,4...15]
	for i=1 até 3:
		x = [3,22
		linha=[3,
		lista= [1,2,4...15]

jogo = [preenchida]

---------------------------------------------------------------
2ª função zero_pos = AchaPosZero(jogo):

for i=0 até 15:
	for j=0 até 3:
		if matriz[0][0] == 0:
			return 11
	for j=1 até 3:
		if matriz[0][1] == 0:
			return 12
	for j=2 até 3:
		if matriz[0][2] == 0:
			return 13
	for j=3 até 3:
		if matriz[0][3] == 0:
			return 14
for i=1 até 15:
	for j=0 até 3:
		if matriz[1][0] == 0:
			return 21
	for j=1 até 3:
		if matriz[1][1] == 0:
			return 22
	for j=2 até 3:
		if matriz[1][2] == 0:
			return 23
	for j=3 até 3:
		if matriz[1][3] == 0:
			return 24
-------------------------------------------------------------
3ª função jogando = fazJogada(jogo)

imprimir = matriz inicial
dec = bool deseja continuar[1] ou desistir[0]?
--------------------------------------------------------------


while jogando=(True):
	pos = escrever um número ao lado do zero, ex:11

	while 
	4ª função VerificaJogada(pos, zero_pos)
		linha = 11//10 = 1
		coluna= 11%10=1

		linha_zero = 21//10=2
		coluna_zero = 21%10=1

		if (1<1 ou 1>4 ou 1<1 ou 1>4):
			return False
		else:
			if(1==1 e 1==1) ou (1==2 e 1==0.........

	
***trocaElemento = o elemento vai receber a posição do zero***

***zero_pos = receber a nova posição do elemento***

---------------------------------------------------------------
5ª função TrocaElemento(pos1, pos2, matriz):

pos = elemento1 = matriz[0][0], pois verificar TrocaElemento(pos, zero_pos, jogo)*
zero_pos = elemento2 = matriz[1][0]
	
matriz --> inverte as posições

----------------------------------------------------------------

***zero_pos é a posição que o zero vai se deslocar***

venceu = 6ª função VerificaSeVenceu(matriz):

for i=0 até 3:
		for j=0 até 3:
			if((1 != 1 e 0 != 3 e 0!= 3)(False) ou (0 ==3 e 0 ==3 e 3 != 0)(False):

		for j=1 até 3:
			if((2 != 2 e 0 != 3 e 1 != 3)(False) ou (0 ==3 e 1 ==3 e 2 != 0)(False):

		for j=2 até 3:
			if((3 != 3 e 0 != 3 e 2 != 3)(False) ou (0 ==3 e 2 ==3 e 3 != 0)(False):

		for j=3 até 3:
			if((4 != 4 e 0 != 3 e 3 != 3)(False) ou (0 ==3 e 3 ==3 e 4 != 0)(False):

for i=1 até 3:
		for j=0 até 3:
			if((5 != 5 e 1 != 3 e 0!= 3)(False) ou (1 ==3 e 0 ==3 e 5 != 0)(False):
		

		for j=1 até 3:
			if((6 != 6 e 1 != 3 e 1 != 3)(False) ou (1 ==3 e 1 ==3 e 6 != 0)(False):

		for j=2 até 3:
			if((7 != 7 e 1 != 3 e 2 != 3)(False) ou (1 ==3 e 2 ==3 e 7 != 0)(False):

		for j=3 até 3:
			if((8 != 8 e 1 != 3 e 3 != 3)(False) ou (1 ==3 e 3 ==3 e 8 != 0)(False):

for i=2 até 3:
		for j=0 até 3:
			if((9 != 9 e 2 != 3 e 0!= 3)(False) ou (2 ==3 e 0 ==3 e 9 != 0)(False):
		

		for j=1 até 3:
			if((10 != 10 e 2 != 3 e 1 != 3)(False) ou (2 ==3 e 1 ==3 e 10 != 0)(False):

		for j=2 até 3:
			if((11 != 11 e 2 != 3 e 2 != 3)(False) ou (2 ==3 e 2 ==3 e 11 != 0)(False):

		for j=3 até 3:
			if((12 != 12 e 2 != 3 e 3 != 3)(False) ou (2 ==3 e 3 ==3 e 12 != 0)(False):

for i=3 até 3:
		for j=0 até 3:
			if((13 != 13 e 3 != 3 e 0!= 3)(False) ou (3 ==3 e 0 ==3 e 13 != 0)(False):
		

		for j=1 até 3:
			if((14 != 14 e 3 != 3 e 1 != 3)(False) ou (3 ==3 e 1 ==3 e 14 != 0)(False):

		for j=2 até 3:
			if((15 != 15 e 3 != 3 e 2 != 3)(False) ou (3 ==3 e 2 ==3 e 15 != 0)(False):

		for j=3 até 3:
			if((16 != 0 e 3 != 3 e 3 != 3)(False) ou (3 == 3 e 3 == 3 e 0 != 0)(False):

"""
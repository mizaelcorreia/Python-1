"""
No site da megasena está escrito que a chance de um jogador ganhar
é de 1 em 50.063.860. Escreva um programa usando o módulo random e os conceitos
utilizados em aula para testar essa probabilidade.
"""

import random

meu = [6, 13, 25, 33, 42, 50]

megasena = list(range(1,61))

n = int(input("Número de testes: "))

soma = 0

for i in range(n):
    sorteado = []

    cont = 0

    while meu != sorteado:
        mega_sort = megasena.copy()

        sorteado = []

        for j in range(6):
            num_sorteado = random.choice(mega_sort)
            sorteado.append(num_sorteado)
            mega_sort.remove(num_sorteado)

        sorteado.sort()

        cont += 1

    soma += cont

    print("Resultado do teste %i: %i tentativas"%(i+1, cont))

soma /= n

print("Média dos resultados:", soma)

import random

meu = [6, 13, 25, 33, 42, 50]

megasena = list(range(1,61))

n = int(input("Número de testes: "))

soma = 0

for i in range(n):
    sorteado = []

    cont = 0

    while meu != sorteado:
        mega_sort = megasena.copy()

        sorteado = []

        for j in range(6):
            num_sorteado = random.choice(mega_sort)
            sorteado.append(num_sorteado)
            mega_sort.remove(num_sorteado)

        sorteado.sort()

        cont += 1

    soma += cont

    print("Resultado do teste %i: %i tentativas"%(i+1, cont))

soma /= n

print("Média dos resultados:", soma)

                                    """Resolução Questão"""
"""
n = 2
soma=0

for (i=0 e n=2)

	sorteado = []
	cont=0

	while (True)

		mega_sort = list(1,61)

		sorteado=[]

		{for j=0 vai até 5
			num_sorteado = 36
			sorteado=[36,
			mega_sort = não tem 36}

		{for j=1 vai até 5
			num_sorteado =  12
			sorteado=[36,12
			mega_sort = não tem 36,12}

		{for j=2 vai até 5
			num_sorteado =  4
			sorteado=[36,12, 4
			mega_sort = não tem 36,12,4}

		{for j=3 vai até 5
			num_sorteado =  5
			sorteado=[36,12,4,5
			mega_sort = não tem 36,12,4,5}

		{for j=4 vai até 5
			num_sorteado =  19
			sorteado=[36,12,4,5,19
			mega_sort = não tem 36,12,4,5,19}

		{for j=5 vai até 5
			num_sorteado =  22
			sorteado=[36,12,4,5,19,22
			mega_sort = não tem [36,12,4,5,19,22]

		sorteado.sort = [4,5,12,19,22,36]

		cont=0+1=1

	while [6,13,25,33,42,50] != [4,5,12,19,22,36] (True)

		mega_sort = list(1,61)

		sorteado=[]

		{for j=0 vai até 5
			num_sorteado = 33
			sorteado=[33,
			mega_sort = não tem 33}

		{for j=1 vai até 5
			num_sorteado = 50
			sorteado=[33,50
			mega_sort = não tem 33,50}

		{for j=2 vai até 5
			num_sorteado =  6
			sorteado=[33,50,6
			mega_sort = não tem 33,50,6}

		{for j=3 vai até 5
			num_sorteado =  13
			sorteado=[33,50,6,13
			mega_sort = não tem 33,50,6,13}

		{for j=4 vai até 5
			num_sorteado =  25
			sorteado=[33,50,6,13,25
			mega_sort = não tem 33,50,6,13,25}

		{for j=5 vai até 5
			num_sorteado =  42
			sorteado=[33,50,6,13,25,42
			mega_sort = não tem [33,50,6,13,25,42]

		sorteado.sort = [6,13,25,33,42,50]

		cont=1+1=2

	while [6,13,25,33,42,50] != [6,13,25,33,42,50] (False)

	soma = 0+2=2
i=0

	print("Resultado do teste [1]: 2 tentativas"%(0+1, 2))

i=1
	soma = 2+523=526

	print("Resultado do teste [2]: 524 tentativas"%(0+1, 2))

soma= soma/2=526/2=263  """
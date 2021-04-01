'''
Autor: Epifânio Francisco           ||  ACEDE
Data: 01/04/2021  -------     18:40 ||
Função: Script para jogar Pedra, Papel, ou Tesoura
'''

import random

palavras = ('PEDRA', 'PAPEL', 'TESOURA')

while True:
    computador = random.choice(palavras)

    while True:
        jogador = str(input('Jogador: ')).upper()
        if jogador not in palavras:
            print('\033[31mERRO. DIGITE APENAS PEDRA, PAPEL OU TESOURA\033[m')
        break

    if jogador == computador:
        print('EMPATE')
        print("{} vs {}.".format(jogador, computador))

    # -> PERDENDO
    elif jogador == 'PEDRA' and computador == 'PAPEL':
        print('VOCÊ PERDEU. {} EMBRULHA {}.'.format(computador, jogador))
        print(jogador, computador)
    elif jogador == 'PAPEL' and computador == 'TESOURA':
        print('VOCÊ PERDEU. {} CORTA O {}.'.format(computador, jogador))
        print(jogador, computador)
    elif jogador == 'TESOURA' and computador == 'PEDRA':
        print('VOCÊ PERDEU. {} ESMAGA A {}.'.format(computador, jogador))

    # -> GANHANDO
    elif jogador == 'PAPEL' and computador == 'PEDRA':
        print('VOCÊ GANHOU. {} EMBRULHA {}.'.format(jogador, computador))
        print(jogador, computador)
    elif jogador == 'TESOURA' and computador == 'PAPEL':
        print('VOCÊ GANHOU. {} CORTA {}'.format(jogador, computador))
        print(jogador, computador)
    elif jogador == 'PEDRA' and computador == 'TESOURA':
        print('VOCÊ GANHOU. {} ESMAGA A {}.'.format(jogador, computador))

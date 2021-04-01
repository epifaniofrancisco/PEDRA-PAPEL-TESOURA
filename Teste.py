'''
 ** Autor: Epifânio Francisco           ||  A C E D E
 ** Data: 01/04/2021  -------     18:40 ||
 ** Função: Script para jogar Pedra, Papel, ou Tesoura
'''

import random

from Voz.TTS import fala

palavras = ('PEDRA', 'PAPEL', 'TESOURA')

fala("PEDRA PAPEL TESOURA")

while True:
    computador = random.choice(palavras)

    while True:
        jogador = str(input('Jogador: ')).upper()
        if jogador not in palavras:
            print('\033[31mERRO. DIGITE APENAS PEDRA, PAPEL OU TESOURA\033[m')
        break

    if jogador == computador:
        fala('EMPATE')
        fala("{} contra {}.".format(jogador, computador))

    # -> PERDENDO
    elif jogador == 'PEDRA' and computador == 'PAPEL':
        fala('VOCÊ PERDEU. {} EMBRULHA {}.'.format(computador, jogador))

    elif jogador == 'PAPEL' and computador == 'TESOURA':
        fala('VOCÊ PERDEU. {} CORTA O {}.'.format(computador, jogador))

    elif jogador == 'TESOURA' and computador == 'PEDRA':
        fala('VOCÊ PERDEU. {} ESMAGA A {}.'.format(computador, jogador))

    # -> GANHANDO
    elif jogador == 'PAPEL' and computador == 'PEDRA':
        fala('VOCÊ GANHOU. {} EMBRULHA {}.'.format(jogador, computador))

    elif jogador == 'TESOURA' and computador == 'PAPEL':
        'VOCÊ GANHOU. {} CORTA {}'.format(jogador, computador)

    elif jogador == 'PEDRA' and computador == 'TESOURA':
        fala('VOCÊ GANHOU. {} ESMAGA A {}.'.format(jogador, computador))
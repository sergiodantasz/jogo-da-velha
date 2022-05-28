from os import name, system
from random import sample, choice

from jogador import *
from tabuleiro import *


def limpar_tela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def escolher_simbolo(j1, j2):
    jogadores = [j1, j2]
    primeiro_jogador, segundo_jogador = sample(jogadores, 2)
    print(f'{primeiro_jogador} começa!')
    while True:
        try:
            if primeiro_jogador.__class__ == Bot:
                simbolos = ['X', 'O']
                s1 = choice(simbolos)
                print(f'{primeiro_jogador} escolheu {s1}!')
                try:
                    input('Pressione ENTER para continuar.')
                    print('=' * 70)
                except:
                    print('=' * 70)
                    limpar_tela()
                    exit()
            else:
                s1 = input(f'{primeiro_jogador}, escolha X ou O: ').upper()
                print('=' * 70)
            if s1 == 'X':
                primeiro_jogador.simbolo = 'X'
                segundo_jogador.simbolo = 'O'
                return [primeiro_jogador, segundo_jogador]
            elif s1 == 'O':
                primeiro_jogador.simbolo = 'O'
                segundo_jogador.simbolo = 'X'
                return [primeiro_jogador, segundo_jogador]
            else:
                print('Escolha inválida.')
                print('=' * 70)
        except:
            print('=' * 70)
            limpar_tela()
            exit()


def escolher_modo_jogo():
    limpar_tela()
    print('=' * 70)
    while True:
        try:
            print('MENU PRINCIPAL'.center(70))
            print('=' * 70)
            print('1 – Jogar VS Amigo')
            print('2 – Jogar VS Computador')
            print('3 – Sair')
            print('=' * 70)
            opcao = input('Escolha uma opção: ')
            if opcao == '1':
                return True
            elif opcao == '2':
                return False
            elif opcao == '3':
                limpar_tela()
                exit()
            else:
                print('=' * 70)
                print('Opção inválida.')
                print('=' * 70)
        except:
            print('=' * 70)
            limpar_tela()
            exit()


def imprimir_placar(primeiro_jogador, segundo_jogador):
    print(f'Placar: {primeiro_jogador} {primeiro_jogador.placar} x {segundo_jogador.placar} {segundo_jogador}')


def jogar(tabuleiro, primeiro_jogador, segundo_jogador):
    tabuleiro.posicoes = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    primeiro_jogador.posicoes = []
    segundo_jogador.posicoes = []

    if tabuleiro.vencedor is not None and tabuleiro.perdedor is not None:
        primeiro_jogador = tabuleiro.vencedor
        segundo_jogador = tabuleiro.perdedor
    while True:
        print('=' * 70)
        imprimir_placar(primeiro_jogador, segundo_jogador)
        print('=' * 70)
        print(f'Símbolo de {primeiro_jogador}: {primeiro_jogador.simbolo}')
        print(f'Símbolo de {segundo_jogador}: {segundo_jogador.simbolo}')
        print('=' * 70, '\n', sep='')

        tabuleiro.imprimir_tabuleiro()
        print('\n', '=' * 70, sep='')
        if segundo_jogador.verificar_vitoria():
            print(f'{segundo_jogador} venceu!')
            print('=' * 70)
            tabuleiro.vencedor = segundo_jogador
            tabuleiro.perdedor = primeiro_jogador
            segundo_jogador.placar += 1
            break
        elif tabuleiro.verificar_velha():
            print('Que pena, deu velha!')
            print('=' * 70)
            tabuleiro.vencedor = primeiro_jogador
            tabuleiro.perdedor = segundo_jogador
            break
        primeiro_jogador.jogar(tabuleiro)
        print('=' * 70)
        limpar_tela()

        print('=' * 70)
        imprimir_placar(primeiro_jogador, segundo_jogador)
        print('=' * 70)
        print(f'Símbolo de {primeiro_jogador}: {primeiro_jogador.simbolo}')
        print(f'Símbolo de {segundo_jogador}: {segundo_jogador.simbolo}')
        print('=' * 70, '\n', sep='')

        tabuleiro.imprimir_tabuleiro()
        print('\n', '=' * 70, sep='')
        if primeiro_jogador.verificar_vitoria():
            print(f'{primeiro_jogador} venceu!')
            print('=' * 70)
            tabuleiro.vencedor = primeiro_jogador
            tabuleiro.perdedor = segundo_jogador
            primeiro_jogador.placar += 1
            break
        elif tabuleiro.verificar_velha():
            print('Que pena, deu velha!')
            print('=' * 70)
            tabuleiro.vencedor = segundo_jogador
            tabuleiro.perdedor = primeiro_jogador
            break
        tabuleiro.verificar_velha()
        segundo_jogador.jogar(tabuleiro)
        print('=' * 70)
        limpar_tela()


def main():
    while True:
        m = escolher_modo_jogo()

        print('=' * 70)

        while True:
            try:
                n_j1 = input('Digite o nome do Jogador 1: ')
                if len(n_j1) < 1:
                    print('=' * 70)
                    print('Digite um nome válido.')
                    print('=' * 70)
                else:
                    j1 = Jogador(n_j1)
                    break
            except:
                print('=' * 70)
                limpar_tela()
                exit()

        if m:
            while True:
                try:
                    n_j2 = input('Digite o nome do Jogador 2: ')
                    if len(n_j2) < 1:
                        print('=' * 70)
                        print('Digite um nome válido.')
                        print('=' * 70)
                    else:
                        j2 = Jogador(n_j2)
                        break
                except:
                    print('=' * 70)
                    limpar_tela()
                    exit()
        else:
            while True:
                try:
                    n_j2 = input('Digite o nome do Jogador 2 (Computador): ')
                    if len(n_j2) < 1:
                        print('=' * 70)
                        print('Digite um nome válido.')
                        print('=' * 70)
                    else:
                        j2 = Bot(n_j2)
                        break
                except:
                    print('=' * 70)
                    limpar_tela()
                    exit()

        print('=' * 70)

        primeiro, segundo = escolher_simbolo(j1, j2)

        t = Tabuleiro(j1, j2)

        limpar_tela()

        jogando = True
        while jogando:
            jogar(t, primeiro, segundo)
            try:
                while True:
                    escolha = input('Deseja jogar de novo? (S/N): ').upper()
                    if escolha == 'S':
                        print('=' * 70)
                        limpar_tela()
                        break
                    elif escolha == 'N':
                        print('=' * 70)
                        limpar_tela()
                        jogando = False
                        break
                    else:
                        print('=' * 70)
                        print('Escolha inválida.')
                        print('=' * 70)
            except:
                print('=' * 70)
                limpar_tela()
                exit()


if __name__ == '__main__':
    main()

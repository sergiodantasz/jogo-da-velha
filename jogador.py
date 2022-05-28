from main import limpar_tela, choice


class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.simbolo = None
        self.posicoes = []
        self.placar = 0

    def __str__(self):
        return self.nome

    def jogar(self, tabuleiro):
        while True:
            try:
                print(f'Vez de {self}!')
                p = int(input(f'{self}, escolha uma posição: '))
                if tabuleiro.posicoes[p - 1] != 'X' and tabuleiro.posicoes[p - 1] != 'O':
                    tabuleiro.posicoes[p - 1] = self.simbolo
                    self.posicoes.append(p)
                    break
                else:
                    print('=' * 70)
                    print('Esta posição já foi preenchida.')
                    print('=' * 70)
            except ValueError:
                print('=' * 70)
                print('Digite somente números inteiros.')
                print('=' * 70)
            except IndexError:
                print('=' * 70)
                print('Posição inexistente.')
                print('=' * 70)
            except:
                print('=' * 70)
                limpar_tela()
                exit()

    def verificar_vitoria(self):
        p = self.posicoes
        if 1 in p and 2 in p and 3 in p:
            return True
        elif 4 in p and 5 in p and 6 in p:
            return True
        elif 7 in p and 8 in p and 9 in p:
            return True
        elif 1 in p and 4 in p and 7 in p:
            return True
        elif 2 in p and 5 in p and 8 in p:
            return True
        elif 3 in p and 6 in p and 9 in p:
            return True
        elif 1 in p and 5 in p and 9 in p:
            return True
        elif 3 in p and 5 in p and 7 in p:
            return True


class Bot(Jogador):
    def jogar(self, tabuleiro):
        print(f'Vez de {self}!')
        posicoes_disponiveis = [p for p in tabuleiro.posicoes if p != 'X' and p != 'O']
        p = int(choice(posicoes_disponiveis))
        print(f'{self} escolheu a posição {p}!')
        tabuleiro.posicoes[p - 1] = self.simbolo
        self.posicoes.append(p)
        try:
            input('Pressione ENTER para continuar.')
        except:
            print('=' * 70)
            limpar_tela()
            exit()

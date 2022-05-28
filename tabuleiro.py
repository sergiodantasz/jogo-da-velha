class Tabuleiro:
    def __init__(self, jogador_1, jogador_2):
        self.posicoes = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.simbolos = {jogador_1.simbolo: jogador_1, jogador_2.simbolo: jogador_2}
        self.vencedor = None
        self.perdedor = None

    def imprimir_tabuleiro(self):
        posicoes = self.mudar_cor_simbolos(self.posicoes.copy())
        print(' {} | {} | {} '.format(*posicoes[0:3]))
        print('-' * 11)
        print(' {} | {} | {} '.format(*posicoes[3:6]))
        print('-' * 11)
        print(' {} | {} | {} '.format(*posicoes[6:9]))

    @staticmethod
    def mudar_cor_simbolos(posicoes):
        for i, p in enumerate(posicoes):
            if p == 'X':
                posicoes[i] = '\033[0;32m' + 'X' + '\033[0;0m'
            elif p == 'O':
                posicoes[i] = '\033[0;31m' + 'O' + '\033[0;0m'
        return posicoes

    def verificar_velha(self):
        posicoes = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        validacoes = []
        for p1 in posicoes:
            for p2 in self.posicoes:
                if p1 != p2:
                    validacoes.append(True)
                else:
                    validacoes.append(False)
        if False not in validacoes:
            return True

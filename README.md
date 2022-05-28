# Jogo da Velha ❌⭕
Um simples — mas interessante — jogo da velha estruturado para terminal. Este projeto foi desenvolvido utilizando a linguagem [Python (3.10.4)](https://www.python.org/downloads/release/python-3104/). Foi gasto cerca de 1 mês até a conclusão.

# Sobre o Projeto 🤔
O jogo conta com três arquivos principais, que são os responsáveis pelo seu funcionamento:
- `jogador.py`
- `tabuleiro.py`
- `main.py`

Em `jogador.py`, estão presente duas classes encarregadas de dar vida e funcionalidades aos jogadores: **Jogador** e **Bot**. Esta, é capaz de jogar e fazer as escolhas por si só. Aquela, age de acordo com as escolhas do usuário. As duas classes possuem métodos que realizam as ações do jogador no jogo da velha.

Já `tabuleiro.py`, compreende uma classe: **Tabuleiro**. Ela possui métodos responsáveis pela visualização e estilização do tabuleiro que o usuário enxerga durante o jogo.

Em suma, o arquivo `main.py`, que, pelo nome, subentende-se que é o arquivo principal do jogo. Nele, está contido as funções que realizam a execução do jogo, como por exemplo a impressão do menu e a decisão do modo de jogo (versus amigo ou versus computador).

# Requisitos ⚠️
Para o funcionamento do jogo é necessário que o usuário possua um ambiente apto a rodar arquivos Python e, é claro, o próprio interpretador [Python, preferencialmente na versão 3.10.4](https://www.python.org/downloads/release/python-3104/).

# Como Jogar 🕹️
Para jogar, é preciso ter os arquivos em sua máquina, e há 2 alternativas para isso:
1. Baixando o arquivo diretamente, no formato zip, e depois descompactá-lo.
2. Utilizando o `git clone` (para isso, é necessário ter o [git](https://git-scm.com/downloads) instalado):
   1. Abra o terminal, na pasta em que deseja baixar os arquivos.
   2. Digite o comando `git clone https://github.com/sergiodantasz/jogo-da-velha.git`.

Depois de ter feito isso, abra o terminal na pasta em que estão localizados os arquivos e execute o arquivo principal do jogo, utilizando o seguinte comando: `python main.py`.
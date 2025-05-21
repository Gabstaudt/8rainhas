N = 8

def posicaoSegura(tabuleiro, linha, coluna):
    for i in range(linha):
        if tabuleiro[i] == coluna or \
           tabuleiro[i] - i == coluna - linha or \
           tabuleiro[i] + i == coluna + linha:
            return False
    return True

def imprimirTabuleiro(tabuleiro):
    for linha in range(N):
        linha_str = ""
        for coluna in range(N):
            if tabuleiro[linha] == coluna:
                linha_str += " 1"
            else:
                linha_str += " 0 "
        print(linha_str)
    print("\n")

def resolver(tabuleiro, linha):
    if linha == N:
        imprimirTabuleiro(tabuleiro)
        return
    for coluna in range(N):
        if posicaoSegura(tabuleiro, linha, coluna):
            tabuleiro[linha] = coluna
            resolver(tabuleiro, linha + 1)

tabuleiro = [-1] * N
resolver(tabuleiro, 0)

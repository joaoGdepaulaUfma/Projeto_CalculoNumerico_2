from utils import fatorial

def lagrange(x, y, valor):

    n = len(x)
    resultado = 0

    for i in range(n):
        termo = y[i]
        for j in range(n):
            if i != j:
                termo *= (valor - x[j]) / (x[i] - x[j])
        resultado += termo
    return resultado

def tabela_diferencas(x, y):
    n = len(x)
    tabela = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        tabela[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = (
                tabela[i + 1][j - 1] - tabela[i][j - 1]
            ) / (x[i + j] - x[i])
    return tabela

def newton(x, y, valor):
    tabela = tabela_diferencas(x, y)
    n = len(x)
    resultado = tabela[0][0]
    produto = 1

    for i in range(1, n):
        produto *= (valor - x[i - 1])
        resultado += tabela[0][i] * produto
    return resultado

def tabela_progressiva(y):
    tabela = [y[:]]

    while len(tabela[-1]) > 1:
        atual = tabela[-1]
        nova = []
        for i in range(len(atual) - 1):
            nova.append(atual[i + 1] - atual[i])
        tabela.append(nova)
    return tabela

def gregory_newton(x, y, valor):
    tabela = tabela_progressiva(y)
    h = x[1] - x[0]
    s = (valor - x[0]) / h
    resultado = tabela[0][0]
    produto = 1

    for i in range(1, len(y)):
        produto *= (s - (i - 1))
        resultado += produto * tabela[i][0] / fatorial(i)

    return resultado
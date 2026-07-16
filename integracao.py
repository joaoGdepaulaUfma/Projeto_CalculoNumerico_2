import math
def trapezios(x, y):
    n = len(x)
    h = x[1] - x[0]
    soma = y[0] + y[n - 1]

    for i in range(1, n - 1):
        soma += 2 * y[i]
    return (h / 2) * soma

def simpson_13(x, y):
    n = len(x) - 1

    if n % 2 != 0:
        raise Exception("Número de intervalos deve ser par.")
    h = x[1] - x[0]
    soma = y[0] + y[n]

    for i in range(1, n):
        if i % 2 == 0:
            soma += 2 * y[i]
        else:
            soma += 4 * y[i]
    return (h / 3) * soma

def simpson_38(x, y):
    n = len(x) - 1

    if n != 3:
        raise Exception("A regra 3/8 utiliza exatamente 3 intervalos.")

    h = x[1] - x[0]
    return (3 * h / 8) * (
        y[0]
        + 3 * y[1]
        + 3 * y[2]
        + y[3]
    )

def quadratura_gauss(funcao, a, b):
    raiz = 1 / math.sqrt(3)
    t = [-raiz, raiz]
    pesos = [1, 1]
    soma = 0

    for i in range(2):
        x = ((b - a) / 2) * t[i] + ((a + b) / 2)
        soma += pesos[i] * funcao(x)
    return ((b - a) / 2) * soma
def fatorial(n):
    resultado = 1

    for i in range(2, n + 1):
        resultado *= i
    return resultado

def imprimir_vetor(vetor):

    for valor in vetor:
        print(f"{valor:.6f}")

def imprimir_matriz(matriz):

    for linha in matriz:
        print(linha)
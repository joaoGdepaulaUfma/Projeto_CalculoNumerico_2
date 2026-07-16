from interpolacao import lagrange, newton, gregory_newton
from splines import spline_linear, spline_cubica_natural
from mmq import ajuste_linear, prever
from integracao import trapezios, simpson_13, simpson_38, quadratura_gauss
from exemplos import *
import math

def funcao_gauss(x):
    return 5 * x**3 + x**2 - 12 * x + 4

def menu():

    print("1  - Interpolação de Lagrange")
    print("2  - Interpolação de Newton")
    print("3  - Gregory-Newton")
    print("4  - Spline Linear")
    print("5  - Spline Cúbica Natural")
    print("6  - Ajuste Linear (MMQ)")
    print("7  - Regra dos Trapézios")
    print("8  - Regra de Simpson 1/3")
    print("9  - Regra de Simpson 3/8")
    print("10 - Quadratura de Gauss")
    print("0  - Sair")

    return int(input("Escolha uma opção: "))


while True:
    opcao = menu()

    if opcao == 0:
        print("\nPrograma encerrado.")
        break


    elif opcao == 1:
        resultado = lagrange(
            LAGRANGE_X,
            LAGRANGE_Y,
            LAGRANGE_VALOR
        )

        print("\nInterpolação de Lagrange")
        print(f"x = {LAGRANGE_VALOR}")
        print(f"Resultado = {resultado:.6f}")


    elif opcao == 2:

        resultado = newton(
            LAGRANGE_X,
            LAGRANGE_Y,
            LAGRANGE_VALOR
        )

        print("\nInterpolação de Newton")
        print(f"x = {LAGRANGE_VALOR}")
        print(f"Resultado = {resultado:.6f}")

    elif opcao == 3:
        resultado = gregory_newton(
            GREGORY_X,
            GREGORY_Y,
            GREGORY_VALOR
        )

        print("\nGregory-Newton")
        print(f"x = {GREGORY_VALOR}")
        print(f"Resultado = {resultado:.6f}")

    elif opcao == 4:
        resultado = spline_linear(
            SPLINE_X,
            SPLINE_Y,
            SPLINE_VALOR
        )

        print("\nSpline Linear")
        print(f"x = {SPLINE_VALOR}")
        print(f"Resultado = {resultado:.6f}")


    elif opcao == 5:
        resultado = spline_cubica_natural(
            SPLINE_X,
            SPLINE_Y,
            SPLINE_VALOR
        )

        print("\nSpline Cúbica Natural")
        print(f"x = {SPLINE_VALOR}")
        print(f"Resultado = {resultado:.6f}")

    elif opcao == 6:
        a, b = ajuste_linear(
            MMQ_X,
            MMQ_Y
        )

        previsao = prever(
            a,
            b,
            MMQ_PREVER
        )

        print("\nAjuste Linear (MMQ)")
        print(f"Reta: y = {a:.6f}x + {b:.6f}")
        print(f"Previsão para x = {MMQ_PREVER}: {previsao:.6f}")

    elif opcao == 7:
        resultado = trapezios(
            TRAP_X,
            TRAP_Y
        )

        print("\nRegra dos Trapézios")
        print(f"Integral = {resultado:.6f}")

    elif opcao == 8:
        resultado = simpson_13(
            TRAP_X,
            TRAP_Y
        )

        print("\nRegra de Simpson 1/3")
        print(f"Integral = {resultado:.6f}")

    elif opcao == 9:
        resultado = simpson_38(
            NC_X,
            NC_Y
        )

        print("\nRegra de Simpson 3/8")
        print(f"Integral = {resultado:.6f}")

    elif opcao == 10:
        resultado = quadratura_gauss(
            funcao_gauss,
            -1,
            1
        )

        print("\nQuadratura de Gauss")
        print(f"Integral = {resultado:.6f}")

    else:

        print("\nOpção inválida.")
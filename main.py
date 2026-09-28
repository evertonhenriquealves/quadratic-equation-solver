import os
import sys


def raizes(a: float, b: float, c: float) -> list[float]:
    # Garante que 'a' nao seja zero antes do calculo
    if a == 0:
        raise ValueError("O coeficiente 'a' nao pode ser zero em uma equacao do 2º grau.")

    # Calculo do discriminante (delta)
    d = (b**2 - 4 * a * c)

    # Valida se as raizes sao reais
    if d < 0:
        raise ArithmeticError("A equacao nao possui raizes reais (delta negativo).")

    x1 = (-b + d**(1 / 2)) / (2 * a)
    x2 = (-b - d**(1 / 2)) / (2 * a)

    print(f"\nValor de x1: {x1:.2f}")
    print(f"Valor de x2: {x2:.2f}\n")

    # Retorna os valores em uma lista
    valores = [x1, x2]
    return valores


if __name__ == "__main__":
    while True:
        print("\nCalcular as raízes de uma equação do segundo grau")
        print("Equação no formato ax² + bx + c = 0\n")

        try:
            a = float(input("Entre com o valor de a: "))
            b = float(input("Entre com o valor de b: "))
            c = float(input("Entre com o valor de c: "))

            # Executa a funcao e armazena o retorno
            res = raizes(a, b, c)
            print(f"Lista de resultados: {res}")

        except ValueError as erro:
            # Captura erro de digitacao ou a == 0
            print(f"Erro de entrada: {erro}")
        except ArithmeticError as erro:
            # Captura o caso de delta negativo lançado pelo raise
            print(f"Erro de cálculo: {erro}")

        # Controle de continuidade do programa
        while True:
            continua = input("\n'q' para sair\n'n' para novo cálculo: ").strip().lower()
            if continua == "q":
                sys.exit()
            elif continua == "n":
                # Limpa a tela no Windows e Linux/Mac
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print("Entrada inválida.")
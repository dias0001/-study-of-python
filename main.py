print("Trabalhando com números")

numero1 = input("Entre com o 1° número: ")
numero2 = input("Entre com o 2° número: ")

try:
    numero1 = int(numero1)
    numero2 = int(numero2)

    soma          = numero1 + numero2
    subtracao     = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao       = numero1 / numero2

    print(soma)
    print(subtracao)
    print(multiplicacao)
    print(divisao)
except ValueError:
    print('Não pode deixar o campo em branco')
print("Calculadora Básica - Feita em Python!!!")
print("Desenvolvida por Diogo Da Silva Almeida.\n")

numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite um outro numero: "))

opcao = 0
while opcao !=7:
    print("\n[1 - Soma];\n[2 - Subtração];\n[3 - Multiplicação];\n[4 - Divisão];\n[5 - Exponenciação];\n[6 - Resto de divisão];\n[7 - Sair do programa];\n") #Opções - Menu

    opcao = int(input("Digite o número referente a operação desejada: "))

    if opcao == 1:
        soma = numero1 + numero2 #Função de soma
        print("\nAdição:", numero1, "+", numero2, "=", soma)
    elif opcao == 2:
        subtracao = numero1 - numero2 #Função de subtração
        print("\nSubtração:", numero1, "-", numero2, "=", subtracao)
    elif opcao == 3:
        multiplicacao = numero1 * numero2 #Função de multiplicação
        print("\nMultiplicação:", numero1, "*", numero2, "=", multiplicacao)
    elif opcao == 4:
        divisao = numero1 / numero2 #Função de divisão
        print("\nDivisão:", numero1, "/", numero2, "=", divisao)
    elif opcao == 5:
        exponenciacao = numero1 ** numero2 #Função de exponenciação
        print("\nExponenciação:", numero1, "^", numero2, "=", exponenciacao)
    elif opcao == 6:
        resto = numero1 % numero2 #Função de exponenciação
        print("\nResto de divisão:", numero1, "%", numero2, "=", resto)
    elif opcao == 7:
        print("\nFim do programa!")
    else:
        print("\nOpção inválida, por gentileza, selecione uma opção dentre as opções válidas e tente novamente!")
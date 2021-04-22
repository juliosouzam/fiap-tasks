import calc
# from calc import somar


def main():
    opt = -1
    print('Hello, Boss.\n')
    while opt != 5:
        opt = int(input(
            'Digite uma opção para realizar a operação.\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n5 - Sair\nOpção: '))
        swicher = {
            1: calc.somar,
            2: calc.sub,
            3: calc.mult,
            4: calc.div,
        }
        runner = swicher.get(opt)
        if opt == 5:
            print('See ya!')
            exit()
        elif (runner == None):
            print('Opção inválida\n')
        else:
            a = float(input('Digite o primeiro número: '))
            b = float(input('Agora, digite o segundo número: '))

            print(runner(a, b))


main()

# def somar():
#     a = float(input('Digite um valor: '))
#     b = float(input('Digite outro um valor: '))

#     soma = a + b

#     print(soma)


# print('Hello, Boss')

def somar(a, b):
    return a + b


def sub():
    print('Subtrair')


def mult():
    print('Multiplicar')


def div():
    print('Dividir')


def main():
    opt = -1
    print('Hello, Boss.\n')
    while opt != 5:
        opt = int(input(
            'Digite uma opção para realizar a operação.\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n5 - Sair\nOpção: '))
        swicher = {
            1: somar,
            2: sub,
            3: mult,
            4: div,
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

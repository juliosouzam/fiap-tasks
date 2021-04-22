notas = []

opt = -1

while opt != 4:
    print('1 - Informar notas \n2 - Exibir notas\n3 - Média \n4 - Sair')
    opt = int(input('Escolha uma opção: '))
    if opt == 1:
        notas.append(float(input('Digite a nota: ')))
    elif opt == 2:
        for x in notas:
            print(x)
    elif opt == 3:
        print('Média é: {0:.2f}'.format(sum(notas) / len(notas)))

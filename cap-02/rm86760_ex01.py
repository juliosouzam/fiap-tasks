weight = float(input('Por favor, informe seu peso: '))
height = float(input('Agora, informe sua altura: '))

imc = weight / pow(height, 2)

if imc < 0.00:
    # Possívelmente nunca irá entrar dentro desse IF
    # mas nunca se sabe como os usuários vão usar nossos programas rsrs
    print("Ops, algo de errado não está certo. :'(")
elif imc < 16.00:
    print('Baixo peso Grau III')
elif imc >= 16.00 and imc <= 16.99:
    print('Baixo peso Grau II')
elif imc >= 17.00 and imc <= 18.49:
    print('Baixo peso Grau I')
elif imc >= 18.50 and imc <= 24.99:
    print('Peso ideal')
elif imc >= 25.00 and imc <= 29.99:
    print('Sobrepeso')
elif imc >= 30.00 and imc <= 34.99:
    print('Obesidade Grau I')
elif imc >= 35.00 and imc <= 39.99:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III')

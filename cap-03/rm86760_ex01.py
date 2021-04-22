qnt_foods = int(input('Quantos alimentos você consumiu hoje? '))

count = 1
total = 0.0
while count <= qnt_foods:
    total = total + float(input('Quantidade de calorias do alimento {}: '.format(count)).replace(',', '.'))
    count = count + 1

print('O total de calorias consumido hoje é de: {0:.2f}'.format(total))

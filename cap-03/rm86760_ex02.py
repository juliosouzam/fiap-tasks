qnt_transactions = int(input('Quantas transações você realizou hoje? '))

count = 1
total = 0.0
while count <= qnt_transactions:
    total = total + float(input('Valor da transação {}: '.format(count)).replace(',', '.'))
    count = count + 1

print('O total gasto hoje foi de: R$ {0:.2f}'.format(total))
print('A média gasto hoje é de: R$ {0:.2f}'.format(total/qnt_transactions))

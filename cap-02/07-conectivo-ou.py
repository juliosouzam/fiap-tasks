value_c = float(input('Digite o valor da compra: '))
payment_t = int(input('1 - Dinheiro / 2 - Cartão: '))

if value_c > 100 or payment_t == 1:
    value_c = value_c * 0.9
    print('Você tem direito a um desconto!')

print('O valor a pagar é {0:.2f}'.format(value_c))

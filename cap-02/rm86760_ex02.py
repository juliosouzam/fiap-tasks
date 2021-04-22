print('Por favor, informe o tipo de sua assinatura.')
subscription_type = int(
    input('1 - Basic / 2 - Silver / 3 - Gold / 4 - Platinum: '))
amount = float(
    input('Agora, informe o valor de seu faturamento anual: R$ ').replace(',', '.'))

if subscription_type == 1:
    amount = amount * 0.3
elif subscription_type == 2:
    amount = amount * 0.2
elif subscription_type == 3:
    amount = amount * 0.1
elif subscription_type == 4:
    amount = amount * 0.05
else:
    print('Ops, opção de assinatura invalida, por favor, tente novamente.')
    exit(0)

print('Pronto, o valor que deverá ser pago é: R$ {0:.2f}'.format(amount))

point = int(input('Digite sua pontuação: '))

if point > 1000:
    print('Você ganhou 3GB de bônus')
elif point > 500:
    print('Você ganhou 1.5GB de bônus')
elif point > 200:
    print('Você ganhou 500MB de bônus')
else:
    print("Hum, continue usando para ganhar bônus :'(")

print('Por favor, informe as informações necessárias.')
monday = int(input('Digite o total de votos de segunda-feira: '))
tuesday = int(input('Agora os de terça-feira: '))
wednesday = int(input('Quarta-feira: '))
thursday = int(input('Agora os de quinta-feita: '))
friday = int(input('E por ultimo, sexta-feira: '))

if monday > tuesday and monday > wednesday and monday > thursday and monday > friday:
    print('Olha, de acordo com meus calculos, segunda-feira foi o dia escolhido.')
elif tuesday > wednesday and tuesday > thursday and tuesday > friday:
    print('Olha, parece que terça-feira é o melhor dia pra realizar as lives.')
elif wednesday > thursday and wednesday > friday:
    print('Quarta-feira, eu escolho você.')
elif thursday > friday:
    print('Não tem dia melhor do que uma quinta-feira para assistir umas lives <3.')
else:
    print('É pra acabar a semana com chave de ouro, sexta-feira é o melhor dia.')

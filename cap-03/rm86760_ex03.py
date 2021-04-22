value = int(
    input('Digite um número e descubra se ele está na sequencia de Fibonacci: '))

i = 0  # old
j = 1  # current
match = False
a = 0
while a <= value and match == False:
    a = i + j
    i = j
    j = a
    match = a == value

if match:
    print('Uhuu, u got it. Ação bem sucedida!')
else:
    print('Ops, algo de errado num está certo. A ação falhou... :(')

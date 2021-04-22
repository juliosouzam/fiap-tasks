name = input('Digite o nome do funcionario: ')
salary = float(input('Digite o salário do funcionário: '))

if salary < 0:
    salary = salary * -1
    print('O salário é negativo')

print('O salário do funcionário {} é {}'.format(name, salary))

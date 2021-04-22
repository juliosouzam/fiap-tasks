n = int(input('De qual número você quer a tabuada: '))
count = 1

while count <= 10:
    print('{} x {} = {}'.format(n, count, n * count))
    count = count + 1

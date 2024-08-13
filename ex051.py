pt = int(input('Qual o primeiro termo? '))
ra = int(input('Qual a razão? '))
de = pt + (10-1) * ra
for c in range(pt, de +ra, ra):
    print('{}'. format(c), end= ' → ')
print('ACABOU')
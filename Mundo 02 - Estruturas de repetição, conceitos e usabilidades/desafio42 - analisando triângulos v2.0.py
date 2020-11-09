r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1<r2 + r3 and r2 <r1 + r3 and r3 <r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIANGULO. ', end='')
    if r1 == r2 == r3:
        print('O triangulo é Equilátero! Todos os lados {}, {} e {} são iguais.'.format(r1, r2, r3))
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triangulo é Isósceles! Dois dos lados {}, {} e {}, são iguais.'.format(r1, r2, r3))
    else:
        print('O triangulo é Escaleno! Todos os lados {}, {} e {} são diferentes.'.format(r1, r2, r3))
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO')

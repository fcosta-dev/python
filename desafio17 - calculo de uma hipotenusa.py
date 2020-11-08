import math
c_oposto = float(input('Digite o comprimento do cateto oposto: '))
c_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
print('O comprimento da hipotenusa é: {:.2f}!'.format(math.hypot(c_oposto, c_adjacente)))


import math
angulo = float(input('Digite o angulo: '))
angulo = math.radians(angulo)
print('O valor do seno do angulo {}, é: {:.2f}'.format(angulo, math.sin(angulo)))
print('O valor do cosseno do angulo {}, é: {:.2f}'.format(angulo, math.cos(angulo)))
print('O valor da tangente do angulo {}, é: {:.2f}'.format(angulo, math.tan(angulo)))


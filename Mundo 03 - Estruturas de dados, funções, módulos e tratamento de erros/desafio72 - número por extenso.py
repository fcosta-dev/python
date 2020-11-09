porextenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco',
              'seis', 'sete', 'oito','nove','dez','onze',
              'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
              'dezessete', 'dezoito','dezenove','vinte')

print('='*40)
print('LENDO UM NÚMERO POR EXTENSO')
print('='*40)
numero = 0
while True:
    numero = int(input('Digite um número de 0 e 20: '))
    if numero <= 20 and numero >=0:
        print(f'O número {numero} por extenso é: {porextenso[numero]}')
        break
    elif numero > 20 or numero < 0:
        print('Número incorreto! Número entre 0 e 20!')

analise2 = ""
fraseoriginal = str(input('Digite a frase: ')).strip().upper()
frase = fraseoriginal.replace(' ', '')
analise1 = frase
qtd = (len(frase))
for c in range(qtd,0,-1):
    analise2 = analise2 + frase[c-1:c:1]
if analise1 == analise2:
    print('A frase: "', fraseoriginal, '" é um políndromo!')
else:
    print('A frase: "', fraseoriginal, '" não é um políndromo!')

#SEGUNDA OPÇÃO DE RESOLUÇÃO
frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print('O iverso de {} é {}'.format(junto, inverso))
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')

#TERCEIRA OPÇÃO DE RESOLUÇÃO
frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = 'junto[::-1]'
print('O iverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo')

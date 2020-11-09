n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('A média das notas {:.1f} e {:.1f} é: {:.1f}'.format(n1, n2, media))
if media < 5.0:
    print('Aluno reprovado!')
elif media <= 6.9 and media >= 5.0:
    print('Aluno em recuperação!')
else:
    print('Aluno aprovado! Parabens!')
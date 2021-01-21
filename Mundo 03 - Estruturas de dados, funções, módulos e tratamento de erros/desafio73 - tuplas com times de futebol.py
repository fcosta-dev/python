tabela = ('São Paulo','Chapecoense', 'Corinthians', 'Atlético', 'Cruzeiro', 'Palmeiras',
              'Fluminense', 'Flamengo', 'Gremio','Avaí','Atlético-GO','Vasco',
              'Ponte Preta', 'Santos', 'Coritiba', 'Bahia', 'Atlético-PR',
              'Sport Recife', 'Botafogo','EC Vitória')

print('Primeiros 5 colocados: {}'.format(tabela[:5]))
print('='*40)
print('Últimos 4 colocados:{}'.format(tabela[-4:]))
print('='*40)
print('Times em ordem alfabética: {}'.format(sorted(tabela)))
print('='*40)
for c in range(0,len(tabela)):
    if (tabela[c]) == 'Chapecoense':
            print('O time Chapecoense está em: {}º lugar!'.format(c+1))

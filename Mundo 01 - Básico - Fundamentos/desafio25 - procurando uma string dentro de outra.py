nome = str(input('Digite o nome da Pessoa: ')).strip()
ok = nome.upper().find('SILVA')
print('A pessoa possui SILVA na ordem: {}'.format(ok))
print('Seu nome tem silva? {}'.format('SILVA' in nome.upper()))

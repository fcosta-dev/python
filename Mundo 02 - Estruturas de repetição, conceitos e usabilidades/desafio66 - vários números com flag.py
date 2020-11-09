n = s = c =0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foi digitado {c} números!')
print(f'A soma deles é {s}!')

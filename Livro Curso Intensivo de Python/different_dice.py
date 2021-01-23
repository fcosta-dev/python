
import pygal
from die import Die

#Cria um D6 e um D10
die_1 = Die()
die_2 = Die(10) #Para criar o D10 passamos o argumento 10 na criação da segunda instancia de Die

#Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(50000): #mudamos o primeiro laço para simular 50.000 lançamentos em vez de 1.000.
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analisa os resultados
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
#print(frequencies)

#Visualiza os resultados
hist = pygal.Bar() #Geramos um gráfico de barras que armazenamos em hist

hist.title = "Results of rolling a D6 and a D10 50.000 times." #Definimos o título do gráfico
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'] #Jogo de um dado com 6 lados e um dado com 10 lados, o menor resultado possível ainda é 2 e o maior é 16
hist.x_title = "Result" #Adicionamos um título para o eixo x
hist.y_title = "Frequency of Result" #Adicionamos um título para o eixo y

hist.add('D6 + D10', frequencies) #Usamos o add para acrescentar uma série de valores ao gráfico
hist.render_to_file('die_visualD6D10.svg') #Renderizamos o gráfico em um arquivo .SVG

#Esse gráfico mostrará os resultados aproximados que você provavelmente obterá quando lançar um par de dados D6.
#Como podemos ver, é menos provavel que você obtenha um 2 ou 12, e mais provável que tire um 7, pois há seis
# maneiras de obter esse valor: 1 e 6, 2 e 5, 3 e 4, 4 e 3, 5 e 2 ou 6 e 1.
import pygal
from die import Die

#Cria dois dados D6
die_1 = Die()
die_2 = Die()

#Faz alguns lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(1000): #como usamos o pygal para analisar e não para exibir resultados, podemos aumentar os lançamentos para 1000.
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

hist.title = "Results of rolling two D6 dice 1000 times." #Definimos o título do gráfico
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'] #usamos os resultados possíveis do lançamento de um D6 como rótulos do eixo x
hist.x_title = "Result" #Adicionamos um título para o eixo x
hist.y_title = "Frequency of Result" #Adicionamos um título para o eixo y

hist.add('D6 + D6', frequencies) #Usamos o add para acrescentar uma série de valores ao gráfico
hist.render_to_file('die_visual.svg') #Renderizamos o gráfico em um arquivo .SVG

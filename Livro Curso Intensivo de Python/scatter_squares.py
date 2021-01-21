#Para plotar um único ponto, utilize a função scatter()
import matplotlib.pyplot as plt

#x_values = [1, 2, 3, 4, 5]
#y_values = [1, 4, 9, 16, 25]

#Essas são as listas de entrada e saída para scatter()
x_values = list(range(1, 1001)) #Lista de valores de x contendo os números de 1 a 1000
y_values = [x**2 for x in x_values] #elevam cada número de x ao quadrado (x**2)

plt.scatter(x_values, y_values, s=40)
#plt.scatter(x_values, y_values, s=100)
#plt.scatter(2, 4, s=200)

#Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of Value", fontsize=14)

#Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)

#Define o intervalo para cada eixo
#neste caso o eixo x varia de 0 a 1.100 e o eixo y de 0 a 1.100.000
plt.axis([0, 1100, 0, 1100000]) #usamos a função axis() para especificar o intervalo de cada eixo

plt.show()

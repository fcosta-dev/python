import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Continua criando novos passeios enquanto o programa estiver ativo
while True:
    #Cria um passeio aleatório e plota os pontos
    rw = RandomWalk(50000) # cria um passeio aleatório com 50.000pontos(para espelhar dados do mundo real)
    rw.fill_walk()

    #Define o tamanho da janela de plotagem
    plt.figure(dpi=128, figsize=(10, 6)) #função figure controla a largura, a altura, a resolução e a cor de fundo do gráfico. O figsize aceita tupla para as dimensões.

    #Plota os pontos e mostra o gráfico
    point_numbers = list(range(rw.num_points)) #usamos a range para gerar uma lista de numeros igual ao numeros de pontos do passeio
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1) #plota cada ponto com tamanho s=1
    # armazenamos esses numeros do range na point_numbers que usaremos para definir a cor de cada ponto do passeio
    # passamos edgecolor=none para eliminar contorno preto de cada ponto
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15)

    # Enfatiza o primeiro e o último ponto
    plt.scatter(0,0, c='green', edgecolors='none', s=100) #plotamos o ponto (0,0) em verde com um tamanho maior s=100
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100) #plotamos o último valor de x e y do passeio em vermelho

    #Remove os eixos
    plt.axes().get_xaxis().set_visible(False) #oculta eixo x
    plt.axes().get_yaxis().set_visible(False) #oculta eixo y

    #plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
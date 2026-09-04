import matplotlib.pyplot as plt

plt.title("Gráfico pro mario")
x = [0, -4, -2,  0,  2,  4, 0]
y = [0,  4,  5, 3.5, 5,  4, 0]


plt.fill(x, y, color="red")
plt.xlabel("x")                 # rótulo do eixo horizontal
plt.ylabel("y")                 # rótulo do eixo vertical
plt.grid(True)   # desenha algo
plt.show()                        # mostra a janela com o gráfico
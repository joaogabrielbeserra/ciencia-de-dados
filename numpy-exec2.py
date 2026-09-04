import numpy as np

notas = np.array([7.5, 8.0, 6.0, 9.5, 5.5])

print("Notas:", notas)
print("Média:", notas.mean())      # média
print("Maior nota:", notas.max())  # maior valor
print("Menor nota:", notas.min())  # menor valor
print("Soma:", notas.sum())        # soma de tudo
print("Notas + 1:", notas + 1)     # soma 1 em cada nota (bônus pra todo mundo)

print("x"*50)

# arange: vai de X até Y pulando de Z em Z (não inclui o Y final)
a = np.arange(0, 10, 3)
print("arange:", a)   # [0 2 4 6 8]

# linspace: X números igualmente espaçados entre início e fim (inclui o fim)
b = np.linspace(0, 10, 5)
print("linspace:", b)  # [ 0.   2.5  5.   7.5 10. ]
import torch

# dados: entrada x e a resposta certa y (que é o dobro de x)
x = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# modelo: uma camada linear (basicamente uma reta y = a*x + b)
modelo = torch.nn.Linear(1, 1)

# ferramentas de treino
perda_fn = torch.nn.MSELoss()                          # mede o erro
otimizador = torch.optim.SGD(modelo.parameters(), lr=0.01)  # ajusta os números

# loop de treino: repete 200 vezes
for epoca in range(200):
    previsao = modelo(x)              # o modelo chuta
    perda = perda_fn(previsao, y)     # quão errado foi?
    otimizador.zero_grad()            # limpa cálculos antigos
    perda.backward()                  # calcula pra onde ajustar
    otimizador.step()                 # ajusta

# testando: quanto dá pra x = 5? (resposta certa seria 10)
print(modelo(torch.tensor([[5.0]])))
import pandas as pd

# criando uma tabela: cada chave do dicionário vira uma coluna
dados = {
    "nome": ["Ana", "Bruno", "Carla", "Diego"],
    "idade": [23, 35, 28, 41],
    "salario": [3000, 5000, 4200, 7000]
}

df = pd.DataFrame(dados)   # df = nome padrão pra "DataFrame"

print(df)              # mostra a tabela inteira
print(df.head(2))      # mostra só as 2 primeiras linhas
print(df["idade"])     # mostra só a coluna idade
print(df["idade"].mean())  # média das idades
print(df.describe())   # resumo estatístico de todas as colunas numéricas
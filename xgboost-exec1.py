import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

# 1. carrega o arquivo (o pandas em ação!)
df = pd.read_csv("deteccao_fauna.csv")
print(df.head())   # espia as primeiras linhas

# 2. separa entradas (X) da resposta (y)
X = df.drop("animal_detectado", axis=1)   # tudo menos a resposta
y = df["animal_detectado"]                # só a resposta

# 3. divide em treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3)

# 4. treina o XGBoost
modelo = XGBClassifier()
modelo.fit(X_treino, y_treino)

# 5. avalia
print("Acurácia:", modelo.score(X_teste, y_teste))
import statsmodels.api as sm
import numpy as np

# X = tamanho da casa | y = preço
X = np.array([50, 80, 100, 120, 150])
y = np.array([200, 320, 400, 480, 600])

X = sm.add_constant(X)   # adiciona o intercepto (o "b" da reta y = a*x + b)

modelo = sm.OLS(y, X).fit()   # OLS = mínimos quadrados (a regressão clássica)
print(modelo.summary())       # o relatorio completo
import numpy as np
from scipy import stats

notas = np.array([7.5, 8.0, 6.0, 9.5, 5.5, 7.0, 8.5, 6.5])

print("Média:", np.mean(notas))
print("Mediana:", np.median(notas))
print("Moda:", stats.mode(notas, keepdims=True).mode)  # valor mais frequente
print("Desvio padrão:", np.std(notas))

# z-score: quantos desvios cada nota está da média
print("Z-scores:", stats.zscore(notas))
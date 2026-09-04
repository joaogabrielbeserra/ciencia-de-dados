import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "produto": ["A", "B", "C", "D"],
    "vendas": [120, 90, 150, 60]
})

sns.barplot(data=df, x="produto", y="vendas")
plt.title("Vendas por produto")
plt.show()
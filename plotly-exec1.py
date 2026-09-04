import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "produto": ["A", "B", "C", "D"],
    "vendas": [120, 90, 150, 60]
})

fig = px.bar(df, x="produto", y="vendas", title="Vendas por produto",
             color="produto")   # cada barra de uma cor
fig.show()
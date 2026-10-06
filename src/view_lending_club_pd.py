import pandas as pd
from IPython.display import display

caminho = "dataset/lending-club-dataset/accepted_2007_to_2018Q4.csv"

amostra = pd.read_csv(caminho, nrows=10)

display(amostra)
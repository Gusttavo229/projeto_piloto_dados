# IMPORTAMTO AS BIBLIOTECAS
import pandas as pd 

#----------------------------------# 

# CRIANDO MEU DF 

caminho = r"dados\tab_imdb.csv"

df = pd.read_csv(caminho, sep=",")

# ----------------------------------# 

# IMPRIMINDO AS 5 PRIMEIRAS LINHAS DO DF

print(df.head())

# IMPORTAMTO AS BIBLIOTECAS
import pandas as pd
from pathlib import Path

# ---------------------------------- #

# CRIANDO MEU DF
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
path = BASE_DIR / "dados" / "dados" / "tab_imdb.csv"

df = pd.read_csv(path, sep=",")

# ---------------------------------- #

# IMPRIMINDO MEU DF
print(df)

from limpieza_bank import eliminar_duplicados, imputar_nulos, detectar_outliers_iqr
import pandas as pd

df = pd.read_csv("data/bank-full.csv", sep=';')

df = eliminar_duplicados(df)

df = imputar_nulos(
    df,
    ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous'],
    estrategia='mediana'
)

outliers = detectar_outliers_iqr(df, 'balance')

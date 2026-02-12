from typing import Literal
import pandas as pd

# Definimos tipos
EstadoDato = Literal['valido', 'outlier_severo', 'outlier_leve', 'error']


def clasificar_observacion(obs: dict) -> EstadoDato:
    """Clasifica una observación estadística usando pattern matching."""
    match obs:
        # Caso: Outlier severo (> 3 desviaciones estándar)
        case {'z_score': z} if abs(z) > 3:
            return 'outlier_severo'

        # Caso: Outlier leve (> 2 desviaciones estándar)
        case {'z_score': z} if abs(z) > 2:
            return 'outlier_leve'

        # Caso por defecto (Catch-all)
        case _:
            return 'valido'


# ──────────────────────────────────────────────────────────


df = pd.read_csv("data/bank-full.csv", sep=';')

# Seleccionamos una variable numérica (ejemplo: balance)
media = df['balance'].mean()
std = df['balance'].std()

# Construimos las observaciones esperadas por la función
df['estado_balance'] = df['balance'].apply(
    lambda x: clasificar_observacion({
        'valor': x,
        'z_score': (x - media) / std if std != 0 else 0
    })
)

print(df['estado_balance'].value_counts())

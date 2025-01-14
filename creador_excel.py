import pandas as pd

data = {
    'Piezas': ['Pata', 'Tablero', 'Estante', 'Panel Lateral'],
    'Centimetros': [40, 120, 100, 180]
    }

df = pd.DataFrame(data)
df.to_excel ('muebles_medidas.xlsx', index=False)

print(df)
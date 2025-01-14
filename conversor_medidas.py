import pandas as pd

def centimetros_a_pulgadas (centimetros):
    pulgadas = centimetros * 0.393701
    return pulgadas
# Ejemplo de uso
 
df =pd.read_excel ('muebles_medidas.xlsx')
df['Pulgadas'] = df['Centimetros'].apply(centimetros_a_pulgadas)
df.to_excel ('muebles_medidas_convertidas.xlsx', index=False)
print(df)
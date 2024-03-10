"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #COLOCAR EN MINUSCULA TODO
    df['sexo'] = df['sexo'].str.lower()
    df['tipo_de_emprendimiento'] = df["tipo_de_emprendimiento"].str.lower()
    df['idea_negocio'] = df["idea_negocio"].str.lower()
    df['línea_credito'] = df['línea_credito'].str.lower()

    #cambiar fecha
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'],format="mixed",dayfirst=True)
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].dt.strftime('%d/%m/%Y')

    # Eliminar los signos de dólar y las comas, y convertir a entero
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('$', '').str.replace(',', '').astype(float).astype(int)


    return df


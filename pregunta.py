"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)
    df = df.dropna()

    df['sexo'] = df['sexo'].str.strip()
    df['sexo'] = df['sexo'].str.lower()
    df["sexo"] = df["sexo"].str.translate(
        str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    )

    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.strip()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.translate(
        str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    )

    df['idea_negocio'] = (df['idea_negocio'].str.lower()
                             .str.capitalize()
                             .str.replace('_',' ')
                             .str.replace('-',' ')
                             .str.replace('.',''))

    df['barrio'] = (df['barrio'].str.lower()
                            .str.capitalize()
                            .str.replace('_',' ')
                            .str.replace('-',' ')
                            .str.replace('.',''))

    df['estrato'] = df['estrato'].astype(int)

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)

    #cambiar fecha
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'],format="mixed",dayfirst=True)
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].dt.strftime('%d/%m/%Y')

    # Eliminar los signos de peso y las comas, y convertir a entero
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('$', '').str.replace(',', '').astype(float).astype(int)

    df['línea_credito'] = df['línea_credito'].str.strip()
    df['línea_credito'] = df['línea_credito'].str.lower()
    df["línea_credito"] = df["línea_credito"].str.translate(
        str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    )

    df = df.drop_duplicates()

    return df

clean_data()
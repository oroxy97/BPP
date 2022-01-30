import pandas as pd

# PARTE 2
# Creamos un try-except que abarque toda la PARTE2
try:
    try:
        datos = pd.read_csv("finanzas2020[1].csv", sep='\t')
        df = pd.DataFrame(datos)
        # Comprobamos que el fichero existe y tiene 12 columnas
        VAR1 = ('Enero' and 'Febrero' and 'Marzo' and 'Abril' and 'Mayo' and 'Junio'
                and 'Julio' and 'Agosto' and 'Septiembre' and 'Octubre' and 'Noviembre'
                and 'Diciembre') in df.columns
        # Comprobamos que cada mes tiene contenido
        VAR2 = df.Enero.empty and df.Febrero.empty and df.Marzo.empty and df.Abril.empty and df.Mayo.empty and df.Junio.empty and df.Julio.empty and df.Septiembre.empty and df.Octubre.empty and df.Noviembre.empty and df.Diciembre.empty
        # Definimos las condiciones
        if(VAR1==True and VAR2==False):
            print("Se ha leído correctamente el archivo finanzas[1].csv")

    except:
        print("No se ha leido correctamente el archivo finanzas[1].csv")
    # Comprobamos mediante excepciones que todos los datos son correctos y si no lo son los convertimos en correctos
    try:
        for i in range(len(df.index)):
            for z in range(len(df.columns)):
                if type(df.iloc[i, z]) == str:
                    try:
                        df.iloc[i, z] = float(df.iloc[i, z])
                    except:
                        df.iloc[i, z] = 0
        print("Los datos no válidos han sido corregidos")
    except:
        print("Hay datos no válidos que no se pueden corregir")
except:
    print("Error al realizar un proceso de la PARTE2")
# PARTE 1
# Creamos un try-except para toda la parte 1
# ¿Qué mes se ha gastado más?
# Definimos las variables para saber el gasto de cada mes
try:
    asignacion = pd.DataFrame({"Pos": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], "Columna": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]})

    m1 = float(df.loc[df['Enero'] < 0, ['Enero']].sum())
    m2 = float(df.loc[df['Febrero'] < 0, ['Febrero']].sum())
    m3 = float(df.loc[df['Marzo'] < 0, ['Marzo']].sum())
    m4 = float(df.loc[df['Abril'] < 0, ['Abril']].sum())
    m5 = float(df.loc[df['Mayo'] < 0, ['Mayo']].sum())
    m6 = float(df.loc[df['Junio'] < 0, ['Junio']].sum())
    m7 = float(df.loc[df['Julio'] < 0, ['Julio']].sum())
    m8 = float(df.loc[df['Agosto'] < 0, ['Agosto']].sum())
    m9 = float(df.loc[df['Septiembre'] < 0, ['Septiembre']].sum())
    m10 = float(df.loc[df['Octubre'] < 0, ['Octubre']].sum())
    m11 = float(df.loc[df['Noviembre'] < 0, ['Noviembre']].sum())
    m12 = float(df.loc[df['Diciembre'] < 0, ['Diciembre']].sum())

    gastos = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12]
    mes_mas = min(gastos)
    for i in range(len(gastos)):
        if mes_mas == gastos[i]:
            print(f'El mes con mayor número de gastos es: {asignacion.iloc[i]["Columna"]}')


    # ¿Qué mes se ha ahorrado más?
    # Definimos las variables para saber el ahorro de cada mes
    a1 = float(df['Enero'].sum())
    a2 = float(df['Febrero'].sum())
    a3 = float(df['Marzo'].sum())
    a4 = float(df['Abril'].sum())
    a5 = float(df['Mayo'].sum())
    a6 = float(df['Junio'].sum())
    a7 = float(df['Julio'].sum())
    a8 = float(df['Agosto'].sum())
    a9 = float(df['Septiembre'].sum())
    a10 = float(df['Octubre'].sum())
    a11 = float(df['Noviembre'].sum())
    a12 = float(df['Diciembre'].sum())

    mes_ahorrador = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
    mes_masahorrado = max(mes_ahorrador)
    for i in range(len(mes_ahorrador)):
        if mes_masahorrado == mes_ahorrador[i]:
            print(f"El mes que más ahorro ha logrado es: {asignacion.iloc[i]['Columna']}")

 # ¿Cuál es la media de gastos al año?

    contador = 0
    for i in range(len(df.index)):
        for z in range(len(df.columns)):
            if df.iloc[i, z] < 0:
                contador += 1
 # Para saber la media de gastos debemos determinar los gastos totales anuales
 # Mostramos por pantalla los gastos totales y la media
    gasto_anual = 0
    for i in range(len(gastos)):
        gasto_anual += gastos[i]
    print(f"Los gastos totales anuales son: {gasto_anual}\nLa media de gastos al año es: {gasto_anual/contador}")


    # ¿Cuáles han sido los ingresos totales a lo largo del año?
    # Primero definimos variables para saber el ingreso de cada mes
    k1 = float(df.loc[df['Enero'] > 0, ['Enero']].sum())
    k2 = float(df.loc[df['Febrero'] > 0, ['Febrero']].sum())
    k3 = float(df.loc[df['Marzo'] > 0, ['Marzo']].sum())
    k4 = float(df.loc[df['Abril'] > 0, ['Abril']].sum())
    k5 = float(df.loc[df['Mayo'] > 0, ['Mayo']].sum())
    k6 = float(df.loc[df['Junio'] > 0, ['Junio']].sum())
    k7 = float(df.loc[df['Julio'] > 0, ['Julio']].sum())
    k8 = float(df.loc[df['Agosto'] > 0, ['Agosto']].sum())
    k9 = float(df.loc[df['Septiembre'] > 0, ['Septiembre']].sum())
    k10 = float(df.loc[df['Octubre'] > 0, ['Octubre']].sum())
    k11 = float(df.loc[df['Noviembre'] > 0, ['Noviembre']].sum())
    k12 = float(df.loc[df['Diciembre'] > 0, ['Diciembre']].sum())

    ingresos = [k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12]
    ingresos_totales = 0
    for i in range(len(ingresos)):
        ingresos_totales += ingresos[i]

    print(f"El ingreso anual ha sido: {ingresos_totales} ")
except:
    print("Error al realizar un cálculo de la PARTE 1")

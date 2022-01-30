import pandas as pd

# PARTE 2
# Creamos un try-except que abarque toda la PARTE2

datos = pd.read_csv("finanzas2020[1].csv", sep='\t')
df = pd.DataFrame(datos)
try:
    def existe_archivo_12(df):
        try:
            assert(len(datos.columns)==12)
            return("El archivo existe y tiene 12 columnas")
        except:
            return("No hay fichero o no puede ser leido")
    print(existe_archivo_12(df))


    def contenido(df):
        for i in datos:
            if len(datos[i]) != 0:
                return("Hay contenido")
    print(contenido(df))


    try:
        def datos_validos(df):
            for i in range(len(df.index)):
                for z in range(len(df.columns)):
                    if type(df.iloc[i, z]) == str:
                        try:
                            df.iloc[i, z] = float(df.iloc[i, z])
                        except:
                            df.iloc[i, z] = 0
            return("Los datos no válidos han sido corregidos")

    except:
        print("Los datos no validos no han sido corregidos")
    print(datos_validos(df))
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
    def mayor_gastomensual(gastos):
        mes_mas = min(gastos)
        for i in range(len(gastos)):
            if mes_mas == gastos[i]:
                return asignacion.iloc[i]["Columna"]
    print("El mes con mayor gasto es:", mayor_gastomensual(gastos))

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
    def ahorro_mensual(mes_ahorrador):
        mes_masahorrado = max(mes_ahorrador)
        for i in range(len(mes_ahorrador)):
            if mes_masahorrado == mes_ahorrador[i]:
                return asignacion.iloc[i]['Columna']

    print(f"El mes que más ahorro ha logrado es:", ahorro_mensual(mes_ahorrador))

# Mostramos por pantalla los gastos totales y la media
    def gastos_totales(df):
        gasto_anual = 0
        for i in range(len(df.index)):
            for z in range(len(df.columns)):
                if df.iloc[i, z] < 0:
                    gasto_anual += df.iloc[i, z]
        return gasto_anual
    print("Los gastos totales son: ", gastos_totales(df))
 # ¿Cuál es la media de gastos al año?
    def media(df):
        contador = 0
        for i in range(len(df.index)):
            for z in range(len(df.columns)):
                if df.iloc[i, z] < 0:
                    contador += 1
        return gastos_totales(df)/contador
    print("La media es:", media(df))
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
    def ingreso(ingresos):
        ingresos_totales = 0
        for i in range(len(ingresos)):
            if ingresos[i] > 0:
                ingresos_totales += ingresos[i]
        return ingresos_totales

    print("El ingreso anual ha sido: ", ingreso(ingresos))
except:
    print("Error al realizar un cálculo de la PARTE 1")

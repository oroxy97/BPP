import pytest
import pandas as pd
import Practica2_SergioRomero

Lista_gastomensual = [-9, -16, -90, -70]
Lista_mes_ahorro = [-4, 89, -7, 78]
Lista_ingresos = [54, 6, 21, 40]
datos_inventados = pd.DataFrame([[1, -2, 3, -4], [5, 6, -7, 8], [9, 10, -11, 12]], columns=['Enero', 'Febrero', 'Marzo', 'Abril'])


def test_existe_archivo_12():
    dato = pd.read_csv('new.csv')
    assert Practica2_SergioRomero.existe_archivo_12(datos_inventados) == "El archivo existe y tiene 12 columnas"


def test_contenido():
    assert Practica2_SergioRomero.contenido(datos_inventados) == 'Hay contenido'


def test_datos_validos():
    assert Practica2_SergioRomero.datos_validos(datos_inventados) == 'Los datos no válidos han sido corregidos'

def test_mayor_gastomensual():
    assert Practica2_SergioRomero.mayor_gastomensual(Lista_gastomensual) == 'Marzo'


def test_ingreso():
    assert Practica2_SergioRomero.ingreso(Lista_ingresos) == 121


def test_ahorromensual():
    assert Practica2_SergioRomero.ahorro_mensual(Lista_mes_ahorro) == 'Febrero'


def test_gastostotales():
    assert Practica2_SergioRomero.gastos_totales(datos_inventados) == -24


def test_media():
    assert Practica2_SergioRomero.media(datos_inventados)  == -6

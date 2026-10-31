import json
from funciones_base import obtener_posicion
from satelite import Satelite


def cargar_registros(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        return json.load(archivo)


def crear_catalogo(registros):
    catalogo = []
    for reg in registros:
        nombre = reg["OBJECT_NAME"]
        cat_id = reg["NORAD_CAT_ID"]
        lat, lon, alt = obtener_posicion(reg)
        sat = Satelite(nombre, cat_id, lat, lon, alt)
        catalogo.append(sat)
    return catalogo


def resumir_por_orbita(catalogo):
    grupos = {"LEO": [], "MEO": [], "GEO": [], "HEO": []}

    for sat in catalogo:
        tipo = sat.obtener_tipo_orbita()
        grupos[tipo].append(sat.altitud)

    resumen = {}
    for tipo, altitudes in grupos.items():
        if altitudes:
            resumen[tipo] = {
                "cantidad": len(altitudes),
                "minima": min(altitudes),
                "maxima": max(altitudes),
                "promedio": round(sum(altitudes) / len(altitudes), 2)
            }
        else:
            resumen[tipo] = {
                "cantidad": 0,
                "minima": None,
                "maxima": None,
                "promedio": None
            }

    return resumen


def obtener_satelites_en_zona(catalogo, lon_min, lat_min, lon_max, lat_max):
    satelites_en_zona = []
    for sat in catalogo:
        if sat.esta_en_zona(lon_min, lat_min, lon_max, lat_max):
            satelites_en_zona.append(sat)
    return satelites_en_zona
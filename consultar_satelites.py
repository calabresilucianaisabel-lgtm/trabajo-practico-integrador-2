import sys
from catalogo import (
    cargar_registros,
    crear_catalogo,
    resumir_por_orbita,
    obtener_satelites_en_zona
)


def main():
    if len(sys.argv) < 3:
        print("Uso:")
        print("  python consultar_satelites.py <ruta_json> resumen")
        print("  python consultar_satelites.py <ruta_json> zona <lon_min> <lat_min> <lon_max> <lat_max>")
        return

    ruta_json = sys.argv[1]
    comando = sys.argv[2].lower()

    registros = cargar_registros(ruta_json)
    catalogo = crear_catalogo(registros)

    if comando == "resumen":
        resumen = resumir_por_orbita(catalogo)
        print("Resumen por tipo de órbita:")
        for tipo, datos in resumen.items():
            cant = datos["cantidad"]
            if cant > 0:
                print(f"  {tipo}: {cant} satélites | Altitud min: {datos['minima']} km, max: {datos['maxima']} km, promedio: {datos['promedio']} km")
            else:
                print(f"  {tipo}: 0 satélites")

    elif comando == "zona":
        lon_min = float(sys.argv[3])
        lat_min = float(sys.argv[4])
        lon_max = float(sys.argv[5])
        lat_max = float(sys.argv[6])

        satelites_zona = obtener_satelites_en_zona(catalogo, lon_min, lat_min, lon_max, lat_max)
        print(f"Satélites encontrados en la zona: {len(satelites_zona)}")
        for sat in satelites_zona:
            print(sat)

    else:
        print(f"Consulta no válida: '{comando}'")


if __name__ == "__main__":
    main()
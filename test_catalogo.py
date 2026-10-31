import pytest
from satelite import Satelite
from catalogo import (
    cargar_registros,
    crear_catalogo,
    resumir_por_orbita,
    obtener_satelites_en_zona
)


def test_cargar_registros_archivo_inexistente():
    with pytest.raises(FileNotFoundError):
        cargar_registros("no_existe.json")


def test_resumir_por_orbita():
    catalogo = [
        Satelite("Sat 1", 1, 0, 0, 400.0),
        Satelite("Sat 2", 2, 0, 0, 600.0),
        Satelite("Sat 3", 3, 0, 0, 20000.0)
    ]

    resumen = resumir_por_orbita(catalogo)

    assert resumen["LEO"]["cantidad"] == 2
    assert resumen["LEO"]["minima"] == 400.0
    assert resumen["LEO"]["maxima"] == 600.0
    assert resumen["LEO"]["promedio"] == 500.0

    assert resumen["MEO"]["cantidad"] == 1
    assert resumen["MEO"]["minima"] == 20000.0

    assert resumen["GEO"]["cantidad"] == 0
    assert resumen["GEO"]["minima"] is None


def test_obtener_satelites_en_zona():
    sat1 = Satelite("Sat Bariloche", 1, -41.1, -71.3, 400.0)
    sat2 = Satelite("Sat Lejano", 2, 10.0, 10.0, 800.0)
    catalogo = [sat1, sat2]

    zona = obtener_satelites_en_zona(catalogo, -76.30, -46.13, -66.30, -36.13)

    assert len(zona) == 1
    assert zona[0].nombre == "Sat Bariloche"


def test_crear_catalogo(monkeypatch):
    monkeypatch.setattr("catalogo.obtener_posicion", lambda reg: (-41.1, -71.3, 400.0))

    registros = [{
        "OBJECT_NAME": "CALSPHERE 1",
        "NORAD_CAT_ID": 900
    }]

    cat = crear_catalogo(registros)

    assert len(cat) == 1
    assert isinstance(cat[0], Satelite)
    assert cat[0].nombre == "CALSPHERE 1"
    assert cat[0].altitud == 400.0
import pytest
from satelite import Satelite


def test_creacion_satelite_valido():
    sat = Satelite("ISS (ZARYA)", 25544, -40.5, -70.2, 419.7)
    assert sat.nombre == "ISS (ZARYA)"
    assert sat.numero_catalogo == 25544
    assert sat.latitud == -40.5
    assert sat.longitud == -70.2
    assert sat.altitud == 419.7


def test_tipos_de_orbita():
    leo = Satelite("Sat LEO", 1, 0, 0, 500)
    meo = Satelite("Sat MEO", 2, 0, 0, 20000)
    geo = Satelite("Sat GEO", 3, 0, 0, 35786)
    heo = Satelite("Sat HEO", 4, 0, 0, 40000)

    assert leo.obtener_tipo_orbita() == "LEO"
    assert meo.obtener_tipo_orbita() == "MEO"
    assert geo.obtener_tipo_orbita() == "GEO"
    assert heo.obtener_tipo_orbita() == "HEO"


def test_descripcion():
    sat = Satelite("ISS (ZARYA)", 25544, -40.5, -70.2, 419.7)
    assert sat.descripcion() == "ISS (ZARYA) | 25544 | LEO | 419.7 km"
    assert str(sat) == "ISS (ZARYA) | 25544 | LEO | 419.7 km"


def test_esta_en_zona():
    sat = Satelite("Test Sat", 100, -40.0, -70.0, 500.0)

    assert sat.esta_en_zona(-75.0, -45.0, -65.0, -35.0) is True
    assert sat.esta_en_zona(-60.0, -45.0, -50.0, -35.0) is False
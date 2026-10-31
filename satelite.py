class Satelite:
    def __init__(self, nombre, numero_catalogo, latitud, longitud, altitud):
        self.nombre = str(nombre).strip()
        self.numero_catalogo = int(numero_catalogo)
        self.latitud = float(latitud)
        self.longitud = float(longitud)
        self.altitud = float(altitud)

    def obtener_tipo_orbita(self):
        if self.altitud < 2000:
            return "LEO"
        elif self.altitud < 34000:
            return "MEO"
        elif self.altitud <= 37000:
            return "GEO"
        return "HEO"

    def descripcion(self):
        tipo = self.obtener_tipo_orbita()
        return f"{self.nombre} | {self.numero_catalogo} | {tipo} | {self.altitud} km"

    def esta_en_zona(self, lon_min, lat_min, lon_max, lat_max):
        return (lon_min <= self.longitud <= lon_max) and (lat_min <= self.latitud <= lat_max)

    def __str__(self):
        return self.descripcion()
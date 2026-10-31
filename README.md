# Seguimiento de Satélites - TPI 2

Materia: Programación I - UNRN - Comisión 3 - Ingeniería en Telecomunicaciones

Docente: Linquiman Ventura, Lautaro Yamil

Estudiante: Calabresi, Luciana Isabel

## Descripción
Este proyecto implementa una aplicación de línea de comandos en Python para procesar el catálogo de satélites activos de CelesTrak. Permite calcular la posición orbital actual de cada satélite, clasificarlo por tipo de órbita y consultar satélites dentro de una zona geográfica específica.

## Requisitos e Instalación

Comandos para crear un entorno virtual e instalar las dependencias:
```bash
python -m venv .venv

pip install -r requirements.txt
```

Resumen de satélites por órbita:

```Bash
python consultar_satelites.py datos/satelites.json resumen
```

Satélites en una zona geográfica (ej: cuadro en Bariloche):

```Bash
python consultar_satelites.py datos/satelites.json zona -76.30 -46.13 -66.30 -36.13
```

Ejecución de Pruebas y Cobertura:

```Bash
pytest --cov=. --cov-report=html
```

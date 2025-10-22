"""
Archivo integrador generado automaticamente
Directorio: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion
Fecha: 2025-10-22 09:43:42
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: constantes.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/constantes.py
# ================================================================================

"""
Constantes centralizadas del sistema PythonForestal.

Todas las constantes del sistema se definen aqui para evitar magic numbers
y facilitar el mantenimiento.
"""

# ============================================================================
# CONSTANTES DE CULTIVOS
# ============================================================================

# Pino
SUPERFICIE_PINO = 2.0  # metros cuadrados
AGUA_INICIAL_PINO = 2  # litros
VARIEDAD_PINO_DEFAULT = "Parana"

# Olivo
SUPERFICIE_OLIVO = 3.0  # metros cuadrados
AGUA_INICIAL_OLIVO = 5  # litros

# Lechuga
SUPERFICIE_LECHUGA = 0.10  # metros cuadrados
AGUA_INICIAL_LECHUGA = 1  # litros
VARIEDAD_LECHUGA_DEFAULT = "Crespa"

# Zanahoria
SUPERFICIE_ZANAHORIA = 0.15  # metros cuadrados
AGUA_INICIAL_ZANAHORIA = 0  # litros (sin agua inicial)

# Arboles - General
ALTURA_INICIAL_ARBOL = 1.0  # metros
CRECIMIENTO_PINO = 0.10  # metros por riego
CRECIMIENTO_OLIVO = 0.01  # metros por riego

# ============================================================================
# CONSTANTES DE AGUA Y RIEGO
# ============================================================================

# Agua
AGUA_MINIMA = 10  # litros minimos para regar
AGUA_INICIAL_PLANTACION = 500  # litros

# Absorcion de agua
ABSORCION_SEASONAL_VERANO = 5  # litros (arboles en verano)
ABSORCION_SEASONAL_INVIERNO = 2  # litros (arboles en invierno)
ABSORCION_LECHUGA = 1  # litros (constante)
ABSORCION_ZANAHORIA = 2  # litros (constante)

# Estaciones (meses)
MES_INICIO_VERANO = 3  # Marzo (hemisferio sur)
MES_FIN_VERANO = 8  # Agosto (hemisferio sur)

# Condiciones de riego
TEMP_MIN_RIEGO = 8  # grados Celsius
TEMP_MAX_RIEGO = 15  # grados Celsius
HUMEDAD_MAX_RIEGO = 50  # porcentaje

# ============================================================================
# CONSTANTES DE SENSORES
# ============================================================================

# Intervalos de sensores (segundos)
INTERVALO_SENSOR_TEMPERATURA = 2.0
INTERVALO_SENSOR_HUMEDAD = 3.0
INTERVALO_CONTROL_RIEGO = 2.5

# Rangos de sensores
SENSOR_TEMP_MIN = -25  # grados Celsius
SENSOR_TEMP_MAX = 50  # grados Celsius
SENSOR_HUMEDAD_MIN = 0  # porcentaje
SENSOR_HUMEDAD_MAX = 100  # porcentaje

# ============================================================================
# CONSTANTES DE THREADING
# ============================================================================

THREAD_JOIN_TIMEOUT = 2.0  # segundos

# ============================================================================
# CONSTANTES DE PERSISTENCIA
# ============================================================================

DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

# ============================================================================
# CONSTANTES DE SUPERFICIE
# ============================================================================

SUPERFICIE_MINIMA_TERRENO = 0.01  # metros cuadrados


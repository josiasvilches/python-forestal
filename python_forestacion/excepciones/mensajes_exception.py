"""
Mensajes de excepcion centralizados.

Este modulo contiene todos los mensajes de error del sistema,
separados en mensajes para usuario y mensajes tecnicos.
"""

# ============================================================================
# MENSAJES DE SUPERFICIE INSUFICIENTE
# ============================================================================

MSG_SUPERFICIE_INSUFICIENTE_USER = "No hay suficiente superficie disponible para plantar"
MSG_SUPERFICIE_INSUFICIENTE_TECH = "Superficie requerida: {requerida} m2, Disponible: {disponible} m2"

# ============================================================================
# MENSAJES DE AGUA AGOTADA
# ============================================================================

MSG_AGUA_AGOTADA_USER = "No hay suficiente agua disponible para regar"
MSG_AGUA_AGOTADA_TECH = "Agua requerida: {requerida} L, Disponible: {disponible} L"

# ============================================================================
# MENSAJES DE PERSISTENCIA
# ============================================================================

MSG_PERSISTENCIA_ERROR_ESCRITURA_USER = "Error al guardar el archivo"
MSG_PERSISTENCIA_ERROR_ESCRITURA_TECH = "Error de escritura en archivo: {archivo}"

MSG_PERSISTENCIA_ERROR_LECTURA_USER = "Error al leer el archivo"
MSG_PERSISTENCIA_ERROR_LECTURA_TECH = "Error de lectura en archivo: {archivo}"

MSG_PERSISTENCIA_ARCHIVO_NO_ENCONTRADO_USER = "El archivo no existe"
MSG_PERSISTENCIA_ARCHIVO_NO_ENCONTRADO_TECH = "Archivo no encontrado: {archivo}"

# ============================================================================
# MENSAJES DE VALIDACION
# ============================================================================

MSG_SUPERFICIE_INVALIDA = "La superficie debe ser mayor a cero"
MSG_AGUA_INVALIDA = "El agua no puede ser negativa"
MSG_PROPIETARIO_VACIO = "El nombre del propietario no puede ser nulo o vacio"
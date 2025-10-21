"""
Archivo integrador generado automaticamente
Directorio: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\excepciones
Fecha: 2025-10-21 18:36:35
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\excepciones\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\excepciones\agua_agotada_exception.py
# ================================================================================

"""
Excepcion para agua agotada en plantacion.
"""

# Local application
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MSG_AGUA_AGOTADA_USER,
    MSG_AGUA_AGOTADA_TECH
)


class AguaAgotadaException(ForestacionException):
    """
    Excepcion lanzada cuando no hay suficiente agua para regar.

    Args:
        agua_requerida: Agua necesaria en litros
        agua_disponible: Agua disponible en litros
    """

    def __init__(self, agua_requerida: int, agua_disponible: int):
        """
        Inicializa la excepcion con detalles de agua.

        Args:
            agua_requerida: Agua que se necesita
            agua_disponible: Agua que hay disponible
        """
        self._agua_requerida = agua_requerida
        self._agua_disponible = agua_disponible

        user_msg = MSG_AGUA_AGOTADA_USER
        tech_msg = MSG_AGUA_AGOTADA_TECH.format(
            requerida=agua_requerida,
            disponible=agua_disponible
        )

        super().__init__(user_msg, tech_msg)

    def get_agua_requerida(self) -> int:
        """
        Obtiene el agua requerida.

        Returns:
            Agua requerida en litros
        """
        return self._agua_requerida

    def get_agua_disponible(self) -> int:
        """
        Obtiene el agua disponible.

        Returns:
            Agua disponible en litros
        """
        return self._agua_disponible

# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\excepciones\forestacion_exception.py
# ================================================================================

"""
Excepcion base del sistema de gestion forestal.

Todas las excepciones personalizadas del sistema heredan de esta clase.
"""


class ForestacionException(Exception):
    """
    Excepcion base para el sistema de gestion forestal.

    Proporciona mensajes separados para usuario y tecnico, permitiendo
    diferentes niveles de detalle segun el publico.

    Args:
        user_message: Mensaje amigable para el usuario final
        technical_message: Mensaje tecnico con detalles del error
    """

    def __init__(self, user_message: str, technical_message: str):
        """
        Inicializa la excepcion con mensajes separados.

        Args:
            user_message: Mensaje para mostrar al usuario
            technical_message: Mensaje tecnico para logs/debugging
        """
        self._user_message = user_message
        self._technical_message = technical_message
        super().__init__(self._get_full_message())

    def get_user_message(self) -> str:
        """
        Obtiene el mensaje amigable para el usuario.

        Returns:
            Mensaje de error para usuario final
        """
        return self._user_message

    def get_technical_message(self) -> str:
        """
        Obtiene el mensaje tecnico con detalles.

        Returns:
            Mensaje tecnico con informacion de debugging
        """
        return self._technical_message

    def _get_full_message(self) -> str:
        """
        Genera mensaje completo combinando ambos mensajes.

        Returns:
            Mensaje completo formateado
        """
        return f"{self._user_message}\nDetalle tecnico: {self._technical_message}"

    def get_full_message(self) -> str:
        """
        Obtiene mensaje completo (usuario + tecnico).

        Returns:
            Mensaje completo con ambos niveles de detalle
        """
        return self._get_full_message()

# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\excepciones\mensajes_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\excepciones\persistencia_exception.py
# ================================================================================

"""
Excepcion para errores de persistencia.
"""

# Standard library
from enum import Enum

# Local application
from python_forestacion.excepciones.forestacion_exception import ForestacionException


class TipoOperacionPersistencia(Enum):
    """
    Tipos de operaciones de persistencia.
    """
    ESCRITURA = "escritura"
    LECTURA = "lectura"


class PersistenciaException(ForestacionException):
    """
    Excepcion lanzada cuando ocurren errores de persistencia.

    Args:
        user_message: Mensaje para el usuario
        technical_message: Mensaje tecnico
        nombre_archivo: Nombre del archivo involucrado
        tipo_operacion: Tipo de operacion (lectura/escritura)
    """

    def __init__(
        self,
        user_message: str,
        technical_message: str,
        nombre_archivo: str,
        tipo_operacion: TipoOperacionPersistencia
    ):
        """
        Inicializa la excepcion con detalles de persistencia.

        Args:
            user_message: Mensaje amigable para usuario
            technical_message: Mensaje tecnico detallado
            nombre_archivo: Nombre del archivo
            tipo_operacion: Tipo de operacion de persistencia
        """
        self._nombre_archivo = nombre_archivo
        self._tipo_operacion = tipo_operacion
        super().__init__(user_message, technical_message)

    def get_nombre_archivo(self) -> str:
        """
        Obtiene el nombre del archivo involucrado.

        Returns:
            Nombre del archivo
        """
        return self._nombre_archivo

    def get_tipo_operacion(self) -> TipoOperacionPersistencia:
        """
        Obtiene el tipo de operacion.

        Returns:
            Tipo de operacion de persistencia
        """
        return self._tipo_operacion

# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\excepciones\superficie_insuficiente_exception.py
# ================================================================================

"""
Excepcion para superficie insuficiente en plantacion.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MSG_SUPERFICIE_INSUFICIENTE_USER,
    MSG_SUPERFICIE_INSUFICIENTE_TECH
)


class SuperficieInsuficienteException(ForestacionException):
    """
    Excepcion lanzada cuando no hay suficiente superficie para plantar.

    Args:
        superficie_requerida: Superficie necesaria en m2
        superficie_disponible: Superficie disponible en m2
    """

    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        """
        Inicializa la excepcion con detalles de superficie.

        Args:
            superficie_requerida: Superficie que se necesita
            superficie_disponible: Superficie que hay disponible
        """
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible

        user_msg = MSG_SUPERFICIE_INSUFICIENTE_USER
        tech_msg = MSG_SUPERFICIE_INSUFICIENTE_TECH.format(
            requerida=superficie_requerida,
            disponible=superficie_disponible
        )

        super().__init__(user_msg, tech_msg)

    def get_superficie_requerida(self) -> float:
        """
        Obtiene la superficie requerida.

        Returns:
            Superficie requerida en m2
        """
        return self._superficie_requerida

    def get_superficie_disponible(self) -> float:
        """
        Obtiene la superficie disponible.

        Returns:
            Superficie disponible en m2
        """
        return self._superficie_disponible


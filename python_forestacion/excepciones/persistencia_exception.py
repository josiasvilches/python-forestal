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
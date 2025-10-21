"""
Entidad Tarea.

Tarea asignada a un trabajador.
"""

# Standard library
from datetime import date


class Tarea:
    """
    Tarea agricola asignada.

    Representa una tarea con ID, fecha y descripcion.
    """

    def __init__(self, id_tarea: int, fecha: date, descripcion: str):
        """
        Inicializa una tarea.

        Args:
            id_tarea: ID unico de la tarea
            fecha: Fecha programada
            descripcion: Descripcion de la tarea
        """
        self._id_tarea = id_tarea
        self._fecha = fecha
        self._descripcion = descripcion

    def get_id_tarea(self) -> int:
        """
        Obtiene el ID de la tarea.

        Returns:
            ID de la tarea
        """
        return self._id_tarea

    def set_id_tarea(self, id_tarea: int) -> None:
        """
        Establece el ID de la tarea.

        Args:
            id_tarea: Nuevo ID
        """
        self._id_tarea = id_tarea

    def get_fecha(self) -> date:
        """
        Obtiene la fecha programada.

        Returns:
            Fecha de la tarea
        """
        return self._fecha

    def set_fecha(self, fecha: date) -> None:
        """
        Establece la fecha programada.

        Args:
            fecha: Nueva fecha
        """
        self._fecha = fecha

    def get_descripcion(self) -> str:
        """
        Obtiene la descripcion de la tarea.

        Returns:
            Descripcion de la tarea
        """
        return self._descripcion

    def set_descripcion(self, descripcion: str) -> None:
        """
        Establece la descripcion de la tarea.

        Args:
            descripcion: Nueva descripcion
        """
        self._descripcion = descripcion
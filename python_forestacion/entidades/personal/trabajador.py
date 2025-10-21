"""
Entidad Trabajador.

Trabajador agricola con tareas y apto medico.
"""

# Standard library
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.tarea import Tarea
    from python_forestacion.entidades.personal.apto_medico import AptoMedico


class Trabajador:
    """
    Trabajador agricola.

    Contiene informacion personal, tareas asignadas y apto medico.
    """

    def __init__(self, dni: int, nombre: str, tareas: List['Tarea']):
        """
        Inicializa un trabajador.

        Args:
            dni: DNI del trabajador
            nombre: Nombre completo
            tareas: Lista de tareas asignadas
        """
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas.copy()
        self._apto_medico: Optional['AptoMedico'] = None

    def get_dni(self) -> int:
        """
        Obtiene el DNI del trabajador.

        Returns:
            DNI
        """
        return self._dni

    def set_dni(self, dni: int) -> None:
        """
        Establece el DNI del trabajador.

        Args:
            dni: Nuevo DNI
        """
        self._dni = dni

    def get_nombre(self) -> str:
        """
        Obtiene el nombre del trabajador.

        Returns:
            Nombre completo
        """
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre del trabajador.

        Args:
            nombre: Nuevo nombre
        """
        self._nombre = nombre

    def get_tareas(self) -> List['Tarea']:
        """
        Obtiene la lista de tareas (defensive copy).

        Returns:
            Copia de la lista de tareas
        """
        return self._tareas.copy()

    def set_tareas(self, tareas: List['Tarea']) -> None:
        """
        Establece la lista de tareas.

        Args:
            tareas: Nueva lista de tareas
        """
        self._tareas = tareas.copy()

    def get_apto_medico(self) -> Optional['AptoMedico']:
        """
        Obtiene el apto medico.

        Returns:
            AptoMedico o None si no tiene
        """
        return self._apto_medico

    def set_apto_medico(self, apto_medico: 'AptoMedico') -> None:
        """
        Establece el apto medico.

        Args:
            apto_medico: Nuevo apto medico
        """
        self._apto_medico = apto_medico
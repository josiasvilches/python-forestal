"""
Archivo integrador generado automaticamente
Directorio: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/entidades/personal
Fecha: 2025-10-22 09:43:42
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/entidades/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/entidades/personal/apto_medico.py
# ================================================================================

"""
Entidad AptoMedico.

Certificacion medica de un trabajador.
"""

# Standard library
from datetime import date


class AptoMedico:
    """
    Certificacion medica de aptitud laboral.

    Indica si un trabajador esta apto para trabajar.
    """

    def __init__(self, apto: bool, fecha_emision: date, observaciones: str):
        """
        Inicializa un apto medico.

        Args:
            apto: True si esta apto, False si no
            fecha_emision: Fecha de emision del certificado
            observaciones: Observaciones medicas
        """
        self._apto = apto
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones

    def esta_apto(self) -> bool:
        """
        Indica si el trabajador esta apto.

        Returns:
            True si esta apto
        """
        return self._apto

    def set_apto(self, apto: bool) -> None:
        """
        Establece el estado de aptitud.

        Args:
            apto: True si esta apto
        """
        self._apto = apto

    def get_fecha_emision(self) -> date:
        """
        Obtiene la fecha de emision.

        Returns:
            Fecha de emision
        """
        return self._fecha_emision

    def set_fecha_emision(self, fecha_emision: date) -> None:
        """
        Establece la fecha de emision.

        Args:
            fecha_emision: Nueva fecha de emision
        """
        self._fecha_emision = fecha_emision

    def get_observaciones(self) -> str:
        """
        Obtiene las observaciones medicas.

        Returns:
            Observaciones
        """
        return self._observaciones

    def set_observaciones(self, observaciones: str) -> None:
        """
        Establece las observaciones medicas.

        Args:
            observaciones: Nuevas observaciones
        """
        self._observaciones = observaciones

# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/entidades/personal/herramienta.py
# ================================================================================

"""
Entidad Herramienta.

Herramienta de trabajo con certificacion H&S.
"""


class Herramienta:
    """
    Herramienta de trabajo agricola.

    Representa una herramienta con certificacion de higiene y seguridad.
    """

    def __init__(self, id_herramienta: int, nombre: str, certificado_hys: bool):
        """
        Inicializa una herramienta.

        Args:
            id_herramienta: ID unico de la herramienta
            nombre: Nombre de la herramienta
            certificado_hys: True si tiene certificado H&S
        """
        self._id_herramienta = id_herramienta
        self._nombre = nombre
        self._certificado_hys = certificado_hys

    def get_id_herramienta(self) -> int:
        """
        Obtiene el ID de la herramienta.

        Returns:
            ID de la herramienta
        """
        return self._id_herramienta

    def set_id_herramienta(self, id_herramienta: int) -> None:
        """
        Establece el ID de la herramienta.

        Args:
            id_herramienta: Nuevo ID
        """
        self._id_herramienta = id_herramienta

    def get_nombre(self) -> str:
        """
        Obtiene el nombre de la herramienta.

        Returns:
            Nombre de la herramienta
        """
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre de la herramienta.

        Args:
            nombre: Nuevo nombre
        """
        self._nombre = nombre

    def tiene_certificado_hys(self) -> bool:
        """
        Indica si tiene certificado H&S.

        Returns:
            True si tiene certificado
        """
        return self._certificado_hys

    def set_certificado_hys(self, certificado_hys: bool) -> None:
        """
        Establece el estado del certificado H&S.

        Args:
            certificado_hys: True si tiene certificado
        """
        self._certificado_hys = certificado_hys

# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/entidades/personal/tarea.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/entidades/personal/trabajador.py
# ================================================================================

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


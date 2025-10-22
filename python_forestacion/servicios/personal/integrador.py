"""
Archivo integrador generado automaticamente
Directorio: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/personal
Fecha: 2025-10-22 09:43:42
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: trabajador_service.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/personal/trabajador_service.py
# ================================================================================

"""
Servicio para Trabajador.

Logica de negocio para trabajadores agricolas.
"""

# Standard library
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion.entidades.personal.apto_medico import AptoMedico

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from python_forestacion.entidades.personal.herramienta import Herramienta


class TrabajadorService:
    """
    Servicio para gestion de trabajadores.

    Proporciona operaciones para asignar apto medico y ejecutar tareas.
    """

    def asignar_apto_medico(
        self,
        trabajador: 'Trabajador',
        apto: bool,
        fecha_emision: date,
        observaciones: str
    ) -> None:
        """
        Asigna un apto medico a un trabajador.

        Args:
            trabajador: Trabajador al que asignar apto
            apto: True si esta apto
            fecha_emision: Fecha de emision del certificado
            observaciones: Observaciones medicas
        """
        apto_medico = AptoMedico(apto, fecha_emision, observaciones)
        trabajador.set_apto_medico(apto_medico)
        print(f"Apto medico asignado a {trabajador.get_nombre()}")

    def trabajar(
        self,
        trabajador: 'Trabajador',
        fecha: date,
        util: 'Herramienta'
    ) -> bool:
        """
        Ejecuta las tareas asignadas a un trabajador.

        Args:
            trabajador: Trabajador que ejecuta tareas
            fecha: Fecha de ejecucion
            util: Herramienta a utilizar

        Returns:
            True si ejecuto tareas, False si no tiene apto medico
        """
        # Verificar apto medico
        apto_medico = trabajador.get_apto_medico()
        if apto_medico is None or not apto_medico.esta_apto():
            print(f"{trabajador.get_nombre()} no puede trabajar - sin apto medico valido")
            return False

        # Filtrar tareas de la fecha especificada
        tareas = trabajador.get_tareas()
        tareas_del_dia = [t for t in tareas if t.get_fecha() == fecha]

        if len(tareas_del_dia) == 0:
            print(f"{trabajador.get_nombre()} no tiene tareas asignadas para {fecha}")
            return True

        # Ordenar tareas por ID descendente (sin lambda)
        tareas_ordenadas = sorted(tareas_del_dia, key=self._obtener_id_tarea, reverse=True)

        # Ejecutar tareas
        nombre_herramienta = util.get_nombre()
        for tarea in tareas_ordenadas:
            print(f"El trabajador {trabajador.get_nombre()} realizo la tarea "
                  f"{tarea.get_id_tarea()} {tarea.get_descripcion()} "
                  f"con herramienta: {nombre_herramienta}")

        return True

    @staticmethod
    def _obtener_id_tarea(tarea) -> int:
        """
        Metodo auxiliar para ordenamiento sin lambda.

        Args:
            tarea: Tarea de la cual obtener ID

        Returns:
            ID de la tarea
        """
        return tarea.get_id_tarea()


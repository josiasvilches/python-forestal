"""
Archivo integrador generado automaticamente
Directorio: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\factory
Fecha: 2025-10-21 18:36:35
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\factory\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: cultivo_factory.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\factory\cultivo_factory.py
# ================================================================================

"""
Patron Factory Method - Fabrica de cultivos.

Centraliza la creacion de cultivos sin exponer clases concretas al cliente.
"""

# Standard library
from typing import TYPE_CHECKING, List
from datetime import date

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from python_forestacion.entidades.personal.herramienta import Herramienta
    from python_forestacion.entidades.personal.tarea import Tarea


class CultivoFactory:
    """
    Factory Method para crear cultivos.

    Encapsula la logica de creacion de diferentes tipos de cultivos,
    permitiendo al cliente crear cultivos sin conocer sus clases concretas.
    """

    @staticmethod
    def crear_cultivo(especie: str) -> 'Cultivo':
        """
        Crea un cultivo del tipo especificado.

        Args:
            especie: Nombre de la especie a crear

        Returns:
            Instancia de Cultivo del tipo solicitado

        Raises:
            ValueError: Si la especie es desconocida
        """
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")

        return factories[especie]()

    @staticmethod
    def _crear_pino() -> 'Cultivo':
        """
        Crea una instancia de Pino.

        Returns:
            Pino con variedad por defecto
        """
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.constantes import VARIEDAD_PINO_DEFAULT
        return Pino(variedad=VARIEDAD_PINO_DEFAULT)

    @staticmethod
    def _crear_olivo() -> 'Cultivo':
        """
        Crea una instancia de Olivo.

        Returns:
            Olivo con tipo de aceituna Arbequina
        """
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)

    @staticmethod
    def _crear_lechuga() -> 'Cultivo':
        """
        Crea una instancia de Lechuga.

        Returns:
            Lechuga con variedad por defecto
        """
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.constantes import VARIEDAD_LECHUGA_DEFAULT
        return Lechuga(variedad=VARIEDAD_LECHUGA_DEFAULT)

    @staticmethod
    def _crear_zanahoria() -> 'Cultivo':
        """
        Crea una instancia de Zanahoria.

        Returns:
            Zanahoria (no baby carrot por defecto)
        """
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        return Zanahoria(is_baby_carrot=False)

    @staticmethod
    def crear_trabajador(dni: int, nombre: str, tareas: List['Tarea']) -> 'Trabajador':
        """
        Crea un trabajador con sus tareas asignadas.

        Args:
            dni: DNI del trabajador
            nombre: Nombre completo del trabajador
            tareas: Lista de tareas asignadas

        Returns:
            Trabajador creado con las tareas asignadas

        Raises:
            ValueError: Si el DNI es negativo o el nombre esta vacio
        """
        if dni <= 0:
            raise ValueError("El DNI debe ser un numero positivo")
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre del trabajador no puede estar vacio")

        from python_forestacion.entidades.personal.trabajador import Trabajador
        return Trabajador(dni=dni, nombre=nombre, tareas=tareas)

    @staticmethod
    def crear_herramienta(id_herramienta: int, nombre: str, certificado_hys: bool = True) -> 'Herramienta':
        """
        Crea una herramienta de trabajo.

        Args:
            id_herramienta: ID unico de la herramienta
            nombre: Nombre de la herramienta
            certificado_hys: True si tiene certificado de higiene y seguridad

        Returns:
            Herramienta creada con los parametros especificados

        Raises:
            ValueError: Si el ID es negativo o el nombre esta vacio
        """
        if id_herramienta <= 0:
            raise ValueError("El ID de herramienta debe ser un numero positivo")
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre de la herramienta no puede estar vacio")

        from python_forestacion.entidades.personal.herramienta import Herramienta
        return Herramienta(id_herramienta=id_herramienta, nombre=nombre, certificado_hys=certificado_hys)


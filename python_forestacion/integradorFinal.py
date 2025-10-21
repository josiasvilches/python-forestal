"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion
Fecha de generacion: 2025-10-21 18:31:01
Total de archivos integrados: 66
Total de directorios procesados: 21
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. constantes.py
#
# DIRECTORIO: entidades
#   3. __init__.py
#
# DIRECTORIO: entidades\cultivos
#   4. __init__.py
#   5. arbol.py
#   6. cultivo.py
#   7. hortaliza.py
#   8. lechuga.py
#   9. olivo.py
#   10. pino.py
#   11. tipo_aceituna.py
#   12. zanahoria.py
#
# DIRECTORIO: entidades\personal
#   13. __init__.py
#   14. apto_medico.py
#   15. herramienta.py
#   16. tarea.py
#   17. trabajador.py
#
# DIRECTORIO: entidades\terrenos
#   18. __init__.py
#   19. plantacion.py
#   20. registro_forestal.py
#   21. tierra.py
#
# DIRECTORIO: excepciones
#   22. __init__.py
#   23. agua_agotada_exception.py
#   24. forestacion_exception.py
#   25. mensajes_exception.py
#   26. persistencia_exception.py
#   27. superficie_insuficiente_exception.py
#
# DIRECTORIO: patrones
#   28. __init__.py
#
# DIRECTORIO: patrones\factory
#   29. __init__.py
#   30. cultivo_factory.py
#
# DIRECTORIO: patrones\observer
#   31. __init__.py
#   32. observable.py
#   33. observer.py
#
# DIRECTORIO: patrones\observer\eventos
#   34. __init__.py
#   35. evento_plantacion.py
#   36. evento_sensor.py
#
# DIRECTORIO: patrones\singleton
#   37. __init__.py
#
# DIRECTORIO: patrones\strategy
#   38. __init__.py
#   39. absorcion_agua_strategy.py
#
# DIRECTORIO: patrones\strategy\impl
#   40. __init__.py
#   41. absorcion_constante_strategy.py
#   42. absorcion_seasonal_strategy.py
#
# DIRECTORIO: riego
#   43. __init__.py
#
# DIRECTORIO: riego\control
#   44. __init__.py
#   45. control_riego_task.py
#
# DIRECTORIO: riego\sensores
#   46. __init__.py
#   47. humedad_reader_task.py
#   48. temperatura_reader_task.py
#
# DIRECTORIO: servicios
#   49. __init__.py
#
# DIRECTORIO: servicios\cultivos
#   50. __init__.py
#   51. arbol_service.py
#   52. cultivo_service.py
#   53. cultivo_service_registry.py
#   54. lechuga_service.py
#   55. olivo_service.py
#   56. pino_service.py
#   57. zanahoria_service.py
#
# DIRECTORIO: servicios\negocio
#   58. __init__.py
#   59. fincas_service.py
#   60. paquete.py
#
# DIRECTORIO: servicios\personal
#   61. __init__.py
#   62. trabajador_service.py
#
# DIRECTORIO: servicios\terrenos
#   63. __init__.py
#   64. plantacion_service.py
#   65. registro_forestal_service.py
#   66. tierra_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/66: __init__.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/66: constantes.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\constantes.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/66: __init__.py
# Directorio: entidades
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades\cultivos
################################################################################

# ==============================================================================
# ARCHIVO 4/66: __init__.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 5/66: arbol.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\arbol.py
# ==============================================================================

"""
Entidad base Arbol.

Clase base para cultivos arboreos (Pino, Olivo).
"""

# Standard library
from abc import ABC

# Local application
from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Arbol(Cultivo, ABC):
    """
    Clase base abstracta para arboles.

    Los arboles tienen altura adicional a los atributos de cultivo.
    """

    def __init__(self, agua: int, superficie: float, altura: float):
        """
        Inicializa un arbol con sus atributos.

        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie ocupada en metros cuadrados
            altura: Altura del arbol en metros
        """
        super().__init__(agua, superficie)
        self._altura = altura

    def get_altura(self) -> float:
        """
        Obtiene la altura del arbol.

        Returns:
            Altura en metros
        """
        return self._altura

    def set_altura(self, altura: float) -> None:
        """
        Establece la altura del arbol.

        Args:
            altura: Nueva altura en metros
        """
        self._altura = altura

# ==============================================================================
# ARCHIVO 6/66: cultivo.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\cultivo.py
# ==============================================================================

"""
Entidad base Cultivo.

Interfaz base para todos los tipos de cultivos del sistema.
"""

# Standard library
from abc import ABC


class Cultivo(ABC):
    """
    Clase base abstracta para todos los cultivos.

    Define los atributos y comportamientos comunes a todos los cultivos.
    Esta es una entidad (DTO) que solo contiene datos, sin logica de negocio.
    """

    _contador_id = 0

    def __init__(self, agua: int, superficie: float):
        """
        Inicializa un cultivo con sus atributos basicos.

        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie ocupada en metros cuadrados
        """
        Cultivo._contador_id += 1
        self._id = Cultivo._contador_id
        self._agua = agua
        self._superficie = superficie

    def get_id(self) -> int:
        """
        Obtiene el ID unico del cultivo.

        Returns:
            ID del cultivo
        """
        return self._id

    def get_agua(self) -> int:
        """
        Obtiene la cantidad de agua almacenada.

        Returns:
            Agua en litros
        """
        return self._agua

    def set_agua(self, agua: int) -> None:
        """
        Establece la cantidad de agua almacenada.

        Args:
            agua: Nueva cantidad de agua en litros
        """
        self._agua = agua

    def get_superficie(self) -> float:
        """
        Obtiene la superficie ocupada por el cultivo.

        Returns:
            Superficie en metros cuadrados
        """
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie ocupada.

        Args:
            superficie: Nueva superficie en metros cuadrados
        """
        self._superficie = superficie

# ==============================================================================
# ARCHIVO 7/66: hortaliza.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\hortaliza.py
# ==============================================================================

"""
Entidad base Hortaliza.

Clase base para cultivos horticolas (Lechuga, Zanahoria).
"""

# Standard library
from abc import ABC

# Local application
from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Hortaliza(Cultivo, ABC):
    """
    Clase base abstracta para hortalizas.

    Las hortalizas pueden requerir o no invernadero.
    """

    def __init__(self, agua: int, superficie: float, invernadero: bool):
        """
        Inicializa una hortaliza con sus atributos.

        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie ocupada en metros cuadrados
            invernadero: True si requiere invernadero
        """
        super().__init__(agua, superficie)
        self._invernadero = invernadero

    def get_invernadero(self) -> bool:
        """
        Indica si la hortaliza esta en invernadero.

        Returns:
            True si esta en invernadero
        """
        return self._invernadero

    def set_invernadero(self, invernadero: bool) -> None:
        """
        Establece si la hortaliza esta en invernadero.

        Args:
            invernadero: True si esta en invernadero
        """
        self._invernadero = invernadero

# ==============================================================================
# ARCHIVO 8/66: lechuga.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\lechuga.py
# ==============================================================================

"""
Entidad Lechuga.

Cultivo horticola de tipo Lechuga con variedad especifica.
"""

# Local application
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_LECHUGA,
    SUPERFICIE_LECHUGA
)


class Lechuga(Hortaliza):
    """
    Cultivo tipo Lechuga.

    Hortaliza de hoja verde que requiere invernadero.
    """

    def __init__(self, variedad: str):
        """
        Inicializa una Lechuga con su variedad.

        Args:
            variedad: Variedad de lechuga (Crespa, Mantecosa, Morada, etc.)
        """
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        """
        Obtiene la variedad de la lechuga.

        Returns:
            Variedad de la lechuga
        """
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        """
        Establece la variedad de la lechuga.

        Args:
            variedad: Nueva variedad
        """
        self._variedad = variedad

# ==============================================================================
# ARCHIVO 9/66: olivo.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\olivo.py
# ==============================================================================

"""
Entidad Olivo.

Cultivo arboreo de tipo Olivo con tipo de aceituna.
"""

# Local application
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import (
    AGUA_INICIAL_OLIVO,
    SUPERFICIE_OLIVO,
    ALTURA_INICIAL_ARBOL
)


class Olivo(Arbol):
    """
    Cultivo tipo Olivo.

    Arbol olivicola con tipo de aceituna especifico.
    """

    def __init__(self, tipo_aceituna: TipoAceituna):
        """
        Inicializa un Olivo con su tipo de aceituna.

        Args:
            tipo_aceituna: Tipo de aceituna del olivo
        """
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=ALTURA_INICIAL_ARBOL
        )
        self._tipo_aceituna = tipo_aceituna

    def get_tipo_aceituna(self) -> TipoAceituna:
        """
        Obtiene el tipo de aceituna.

        Returns:
            Tipo de aceituna
        """
        return self._tipo_aceituna

    def set_tipo_aceituna(self, tipo_aceituna: TipoAceituna) -> None:
        """
        Establece el tipo de aceituna.

        Args:
            tipo_aceituna: Nuevo tipo de aceituna
        """
        self._tipo_aceituna = tipo_aceituna

# ==============================================================================
# ARCHIVO 10/66: pino.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\pino.py
# ==============================================================================

"""
Entidad Pino.

Cultivo arboreo de tipo Pino con variedad especifica.
"""

# Local application
from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import (
    AGUA_INICIAL_PINO,
    SUPERFICIE_PINO,
    ALTURA_INICIAL_ARBOL
)


class Pino(Arbol):
    """
    Cultivo tipo Pino.

    Arbol maderable con diferentes variedades posibles.
    """

    def __init__(self, variedad: str):
        """
        Inicializa un Pino con su variedad.

        Args:
            variedad: Variedad de pino (Parana, Elliott, Taeda, etc.)
        """
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=ALTURA_INICIAL_ARBOL
        )
        self._variedad = variedad

    def get_variedad(self) -> str:
        """
        Obtiene la variedad del pino.

        Returns:
            Variedad del pino
        """
        return self._variedad

    def set_variedad(self, variedad: str) -> None:
        """
        Establece la variedad del pino.

        Args:
            variedad: Nueva variedad
        """
        self._variedad = variedad

# ==============================================================================
# ARCHIVO 11/66: tipo_aceituna.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\tipo_aceituna.py
# ==============================================================================

"""
Enum para tipos de aceituna.
"""

# Standard library
from enum import Enum


class TipoAceituna(Enum):
    """
    Tipos de aceituna disponibles para olivos.
    """
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"

# ==============================================================================
# ARCHIVO 12/66: zanahoria.py
# Directorio: entidades\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\zanahoria.py
# ==============================================================================

"""
Entidad Zanahoria.

Cultivo horticola de tipo Zanahoria (regular o baby carrot).
"""

# Local application
from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import (
    AGUA_INICIAL_ZANAHORIA,
    SUPERFICIE_ZANAHORIA
)


class Zanahoria(Hortaliza):
    """
    Cultivo tipo Zanahoria.

    Hortaliza de raiz que puede ser regular o baby carrot.
    """

    def __init__(self, is_baby_carrot: bool):
        """
        Inicializa una Zanahoria.

        Args:
            is_baby_carrot: True si es baby carrot, False si es regular
        """
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._is_baby_carrot = is_baby_carrot

    def is_baby_carrot(self) -> bool:
        """
        Indica si es baby carrot.

        Returns:
            True si es baby carrot, False si es regular
        """
        return self._is_baby_carrot

    def set_baby_carrot(self, is_baby_carrot: bool) -> None:
        """
        Establece si es baby carrot.

        Args:
            is_baby_carrot: True para baby carrot, False para regular
        """
        self._is_baby_carrot = is_baby_carrot


################################################################################
# DIRECTORIO: entidades\personal
################################################################################

# ==============================================================================
# ARCHIVO 13/66: __init__.py
# Directorio: entidades\personal
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\personal\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 14/66: apto_medico.py
# Directorio: entidades\personal
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\personal\apto_medico.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 15/66: herramienta.py
# Directorio: entidades\personal
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\personal\herramienta.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 16/66: tarea.py
# Directorio: entidades\personal
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\personal\tarea.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 17/66: trabajador.py
# Directorio: entidades\personal
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\personal\trabajador.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: entidades\terrenos
################################################################################

# ==============================================================================
# ARCHIVO 18/66: __init__.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\terrenos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 19/66: plantacion.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\terrenos\plantacion.py
# ==============================================================================

"""
Entidad Plantacion.

Representa una plantacion con cultivos y trabajadores.
"""

# Standard library
from typing import TYPE_CHECKING, List

# Local application
from python_forestacion.excepciones.mensajes_exception import (
    MSG_SUPERFICIE_INVALIDA,
    MSG_AGUA_INVALIDA
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador


class Plantacion:
    """
    Plantacion agricola con cultivos y trabajadores.

    Contiene la lista de cultivos plantados y trabajadores asignados.
    """

    def __init__(self, nombre: str, superficie: float, agua: int):
        """
        Inicializa una plantacion.

        Args:
            nombre: Nombre identificatorio de la plantacion
            superficie: Superficie maxima en metros cuadrados
            agua: Agua disponible inicial en litros

        Raises:
            ValueError: Si superficie o agua son invalidas
        """
        if superficie <= 0:
            raise ValueError(MSG_SUPERFICIE_INVALIDA)
        if agua < 0:
            raise ValueError(MSG_AGUA_INVALIDA)

        self._nombre = nombre
        self._superficie = superficie
        self._agua_disponible = agua
        self._cultivos: List['Cultivo'] = []
        self._trabajadores: List['Trabajador'] = []
        self._superficie_ocupada = 0.0

    def get_nombre(self) -> str:
        """
        Obtiene el nombre de la plantacion.

        Returns:
            Nombre de la plantacion
        """
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        """
        Establece el nombre de la plantacion.

        Args:
            nombre: Nuevo nombre
        """
        self._nombre = nombre

    def get_superficie(self) -> float:
        """
        Obtiene la superficie maxima.

        Returns:
            Superficie en metros cuadrados
        """
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie maxima.

        Args:
            superficie: Nueva superficie

        Raises:
            ValueError: Si la superficie no es mayor a cero
        """
        if superficie <= 0:
            raise ValueError(MSG_SUPERFICIE_INVALIDA)
        self._superficie = superficie

    def get_agua_disponible(self) -> int:
        """
        Obtiene el agua disponible.

        Returns:
            Agua en litros
        """
        return self._agua_disponible

    def set_agua_disponible(self, agua: int) -> None:
        """
        Establece el agua disponible.

        Args:
            agua: Nueva cantidad de agua

        Raises:
            ValueError: Si el agua es negativa
        """
        if agua < 0:
            raise ValueError(MSG_AGUA_INVALIDA)
        self._agua_disponible = agua

    def get_cultivos(self) -> List['Cultivo']:
        """
        Obtiene la lista de cultivos (defensive copy).

        Returns:
            Copia de la lista de cultivos
        """
        return self._cultivos.copy()

    def set_cultivos(self, cultivos: List['Cultivo']) -> None:
        """
        Establece la lista de cultivos.

        Args:
            cultivos: Nueva lista de cultivos
        """
        self._cultivos = cultivos.copy()

    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        """
        Agrega un cultivo a la plantacion.

        Args:
            cultivo: Cultivo a agregar
        """
        self._cultivos.append(cultivo)

    def eliminar_cultivo(self, cultivo: 'Cultivo') -> None:
        """
        Elimina un cultivo de la plantacion.

        Args:
            cultivo: Cultivo a eliminar
        """
        if cultivo in self._cultivos:
            self._cultivos.remove(cultivo)

    def get_trabajadores(self) -> List['Trabajador']:
        """
        Obtiene la lista de trabajadores (defensive copy).

        Returns:
            Copia de la lista de trabajadores
        """
        return self._trabajadores.copy()

    def set_trabajadores(self, trabajadores: List['Trabajador']) -> None:
        """
        Establece la lista de trabajadores.

        Args:
            trabajadores: Nueva lista de trabajadores
        """
        self._trabajadores = trabajadores.copy()

    def get_superficie_ocupada(self) -> float:
        """
        Obtiene la superficie ocupada por cultivos.

        Returns:
            Superficie ocupada en metros cuadrados
        """
        return self._superficie_ocupada

    def set_superficie_ocupada(self, superficie_ocupada: float) -> None:
        """
        Establece la superficie ocupada.

        Args:
            superficie_ocupada: Nueva superficie ocupada
        """
        self._superficie_ocupada = superficie_ocupada

# ==============================================================================
# ARCHIVO 20/66: registro_forestal.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\terrenos\registro_forestal.py
# ==============================================================================

"""
Entidad RegistroForestal.

Vincula tierra, plantacion, propietario y avaluo fiscal.
"""

# Standard library
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class RegistroForestal:
    """
    Registro forestal completo.

    Vincula terreno catastral con plantacion, propietario y avaluo.
    """

    def __init__(
        self,
        id_padron: int,
        tierra: 'Tierra',
        plantacion: 'Plantacion',
        propietario: str,
        avaluo: float
    ):
        """
        Inicializa un registro forestal.

        Args:
            id_padron: ID del padron catastral
            tierra: Terreno asociado
            plantacion: Plantacion asociada
            propietario: Nombre del propietario
            avaluo: Avaluo fiscal
        """
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo

    def get_id_padron(self) -> int:
        """
        Obtiene el ID del padron.

        Returns:
            ID del padron
        """
        return self._id_padron

    def set_id_padron(self, id_padron: int) -> None:
        """
        Establece el ID del padron.

        Args:
            id_padron: Nuevo ID de padron
        """
        self._id_padron = id_padron

    def get_tierra(self) -> 'Tierra':
        """
        Obtiene el terreno asociado.

        Returns:
            Tierra asociada
        """
        return self._tierra

    def set_tierra(self, tierra: 'Tierra') -> None:
        """
        Establece el terreno asociado.

        Args:
            tierra: Nueva tierra
        """
        self._tierra = tierra

    def get_plantacion(self) -> 'Plantacion':
        """
        Obtiene la plantacion asociada.

        Returns:
            Plantacion asociada
        """
        return self._plantacion

    def set_plantacion(self, plantacion: 'Plantacion') -> None:
        """
        Establece la plantacion asociada.

        Args:
            plantacion: Nueva plantacion
        """
        self._plantacion = plantacion

    def get_propietario(self) -> str:
        """
        Obtiene el nombre del propietario.

        Returns:
            Nombre del propietario
        """
        return self._propietario

    def set_propietario(self, propietario: str) -> None:
        """
        Establece el nombre del propietario.

        Args:
            propietario: Nuevo propietario
        """
        self._propietario = propietario

    def get_avaluo(self) -> float:
        """
        Obtiene el avaluo fiscal.

        Returns:
            Avaluo fiscal
        """
        return self._avaluo

    def set_avaluo(self, avaluo: float) -> None:
        """
        Establece el avaluo fiscal.

        Args:
            avaluo: Nuevo avaluo
        """
        self._avaluo = avaluo

# ==============================================================================
# ARCHIVO 21/66: tierra.py
# Directorio: entidades\terrenos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\terrenos\tierra.py
# ==============================================================================

"""
Entidad Tierra.

Representa un terreno catastral con padron y superficie.
"""

# Standard library
from typing import TYPE_CHECKING, Optional

# Local application
from python_forestacion.excepciones.mensajes_exception import MSG_SUPERFICIE_INVALIDA

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class Tierra:
    """
    Terreno catastral registrado.

    Contiene informacion catastral y puede tener una plantacion asociada.
    """

    def __init__(self, id_padron_catastral: int, superficie: float, domicilio: str):
        """
        Inicializa un terreno.

        Args:
            id_padron_catastral: Numero de padron catastral unico
            superficie: Superficie en metros cuadrados
            domicilio: Ubicacion del terreno

        Raises:
            ValueError: Si la superficie no es mayor a cero
        """
        if superficie <= 0:
            raise ValueError(MSG_SUPERFICIE_INVALIDA)

        self._id_padron_catastral = id_padron_catastral
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca: Optional['Plantacion'] = None

    def get_id_padron_catastral(self) -> int:
        """
        Obtiene el ID del padron catastral.

        Returns:
            Numero de padron
        """
        return self._id_padron_catastral

    def set_id_padron_catastral(self, id_padron_catastral: int) -> None:
        """
        Establece el ID del padron catastral.

        Args:
            id_padron_catastral: Nuevo numero de padron
        """
        self._id_padron_catastral = id_padron_catastral

    def get_superficie(self) -> float:
        """
        Obtiene la superficie del terreno.

        Returns:
            Superficie en metros cuadrados
        """
        return self._superficie

    def set_superficie(self, superficie: float) -> None:
        """
        Establece la superficie del terreno.

        Args:
            superficie: Nueva superficie en metros cuadrados

        Raises:
            ValueError: Si la superficie no es mayor a cero
        """
        if superficie <= 0:
            raise ValueError(MSG_SUPERFICIE_INVALIDA)
        self._superficie = superficie

    def get_domicilio(self) -> str:
        """
        Obtiene el domicilio del terreno.

        Returns:
            Domicilio
        """
        return self._domicilio

    def set_domicilio(self, domicilio: str) -> None:
        """
        Establece el domicilio del terreno.

        Args:
            domicilio: Nuevo domicilio
        """
        self._domicilio = domicilio

    def get_finca(self) -> Optional['Plantacion']:
        """
        Obtiene la plantacion asociada.

        Returns:
            Plantacion asociada o None
        """
        return self._finca

    def set_finca(self, finca: 'Plantacion') -> None:
        """
        Establece la plantacion asociada.

        Args:
            finca: Plantacion a asociar
        """
        self._finca = finca


################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 22/66: __init__.py
# Directorio: excepciones
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\excepciones\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 23/66: agua_agotada_exception.py
# Directorio: excepciones
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\excepciones\agua_agotada_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 24/66: forestacion_exception.py
# Directorio: excepciones
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\excepciones\forestacion_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 25/66: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\excepciones\mensajes_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 26/66: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\excepciones\persistencia_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 27/66: superficie_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\excepciones\superficie_insuficiente_exception.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 28/66: __init__.py
# Directorio: patrones
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones\factory
################################################################################

# ==============================================================================
# ARCHIVO 29/66: __init__.py
# Directorio: patrones\factory
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\factory\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 30/66: cultivo_factory.py
# Directorio: patrones\factory
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\factory\cultivo_factory.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones\observer
################################################################################

# ==============================================================================
# ARCHIVO 31/66: __init__.py
# Directorio: patrones\observer
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\observer\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 32/66: observable.py
# Directorio: patrones\observer
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\observer\observable.py
# ==============================================================================

"""
Patron Observer - Clase Observable.

Clase base para objetos que pueden ser observados.
"""

# Standard library
from abc import ABC
from typing import Generic, TypeVar, List

# Local application
from python_forestacion.patrones.observer.observer import Observer

T = TypeVar('T')


class Observable(Generic[T], ABC):
    """
    Clase Observable generica tipo-segura.

    Mantiene una lista de observadores y los notifica cuando ocurren cambios.

    Type Parameters:
        T: Tipo de evento que puede notificar
    """

    def __init__(self):
        """
        Inicializa lista de observadores vacia.
        """
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Agrega un observador a la lista.

        Args:
            observador: Observador a agregar
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """
        Elimina un observador de la lista.

        Args:
            observador: Observador a eliminar
        """
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores con el evento.

        Args:
            evento: Evento o dato a notificar del tipo T
        """
        for observador in self._observadores:
            observador.actualizar(evento)

# ==============================================================================
# ARCHIVO 33/66: observer.py
# Directorio: patrones\observer
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\observer\observer.py
# ==============================================================================

"""
Patron Observer - Interfaz Observer.

Define el contrato para objetos que observan cambios en Observables.
"""

# Standard library
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Observer(Generic[T], ABC):
    """
    Interfaz Observer generica tipo-segura.

    Los observadores reciben notificaciones cuando el Observable cambia.

    Type Parameters:
        T: Tipo de evento que puede recibir
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Metodo llamado cuando el Observable notifica un cambio.

        Args:
            evento: Evento o dato actualizado del tipo T
        """
        pass


################################################################################
# DIRECTORIO: patrones\observer\eventos
################################################################################

# ==============================================================================
# ARCHIVO 34/66: __init__.py
# Directorio: patrones\observer\eventos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\observer\eventos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 35/66: evento_plantacion.py
# Directorio: patrones\observer\eventos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\observer\eventos\evento_plantacion.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 36/66: evento_sensor.py
# Directorio: patrones\observer\eventos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\observer\eventos\evento_sensor.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones\singleton
################################################################################

# ==============================================================================
# ARCHIVO 37/66: __init__.py
# Directorio: patrones\singleton
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\singleton\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones\strategy
################################################################################

# ==============================================================================
# ARCHIVO 38/66: __init__.py
# Directorio: patrones\strategy
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\strategy\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 39/66: absorcion_agua_strategy.py
# Directorio: patrones\strategy
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\strategy\absorcion_agua_strategy.py
# ==============================================================================

"""
Patron Strategy - Interfaz para estrategias de absorcion de agua.

Define el contrato que deben cumplir todas las estrategias de absorcion.
"""

# Standard library
from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """
    Interfaz Strategy para algoritmos de absorcion de agua.

    Permite implementar diferentes estrategias de absorcion segun
    el tipo de cultivo (estacional, constante, etc.).
    """

    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula la cantidad de agua que absorbe un cultivo.

        Args:
            fecha: Fecha actual para determinar estacion
            temperatura: Temperatura ambiental en grados Celsius
            humedad: Humedad ambiental en porcentaje
            cultivo: Cultivo que absorbe agua

        Returns:
            Cantidad de agua absorbida en litros
        """
        pass


################################################################################
# DIRECTORIO: patrones\strategy\impl
################################################################################

# ==============================================================================
# ARCHIVO 40/66: __init__.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\strategy\impl\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 41/66: absorcion_constante_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\strategy\impl\absorcion_constante_strategy.py
# ==============================================================================

"""
Estrategia de absorcion constante para hortalizas.

Las hortalizas absorben siempre la misma cantidad de agua.
"""

# Standard library
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorcion constante.

    Hortalizas absorben siempre la misma cantidad independientemente
    de la estacion o condiciones ambientales.
    """

    def __init__(self, cantidad_constante: int):
        """
        Inicializa estrategia con cantidad fija.

        Args:
            cantidad_constante: Litros a absorber siempre
        """
        self._cantidad_constante = cantidad_constante

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Retorna siempre la misma cantidad de agua.

        Args:
            fecha: No utilizada en esta estrategia
            temperatura: No utilizada en esta estrategia
            humedad: No utilizada en esta estrategia
            cultivo: No utilizado en esta estrategia

        Returns:
            Cantidad constante configurada
        """
        return self._cantidad_constante

# ==============================================================================
# ARCHIVO 42/66: absorcion_seasonal_strategy.py
# Directorio: patrones\strategy\impl
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\patrones\strategy\impl\absorcion_seasonal_strategy.py
# ==============================================================================

"""
Estrategia de absorcion estacional para arboles.

Los arboles absorben mas agua en verano que en invierno.
"""

# Standard library
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy
from python_forestacion.constantes import (
    ABSORCION_SEASONAL_VERANO,
    ABSORCION_SEASONAL_INVIERNO,
    MES_INICIO_VERANO,
    MES_FIN_VERANO
)

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorcion estacional.

    Arboles absorben:
    - Verano (marzo-agosto): 5 litros
    - Invierno (sept-feb): 2 litros
    """

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula absorcion basada en la estacion del anio.

        Args:
            fecha: Fecha actual para determinar estacion
            temperatura: No utilizada en esta estrategia
            humedad: No utilizada en esta estrategia
            cultivo: Cultivo que absorbe

        Returns:
            5 litros en verano, 2 litros en invierno
        """
        mes = fecha.month

        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO
        else:
            return ABSORCION_SEASONAL_INVIERNO


################################################################################
# DIRECTORIO: riego
################################################################################

# ==============================================================================
# ARCHIVO 43/66: __init__.py
# Directorio: riego
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\riego\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: riego\control
################################################################################

# ==============================================================================
# ARCHIVO 44/66: __init__.py
# Directorio: riego\control
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\riego\control\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 45/66: control_riego_task.py
# Directorio: riego\control
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\riego\control\control_riego_task.py
# ==============================================================================

"""
Thread controlador de riego (Observer).

Observa sensores y riega automaticamente segun condiciones.
"""

# Standard library
import threading
import time
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import (
    INTERVALO_CONTROL_RIEGO,
    TEMP_MIN_RIEGO,
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO
)

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
    from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
    from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask


class ControlRiegoTask(threading.Thread, Observer[float]):
    """
    Thread daemon controlador de riego automatico.

    Observa sensores de temperatura y humedad, y riega cuando se cumplen condiciones.
    """

    def __init__(
        self,
        sensor_temperatura: 'TemperaturaReaderTask',
        sensor_humedad: 'HumedadReaderTask',
        plantacion: 'Plantacion',
        plantacion_service: 'PlantacionService'
    ):
        """
        Inicializa el controlador de riego.

        Args:
            sensor_temperatura: Sensor de temperatura a observar
            sensor_humedad: Sensor de humedad a observar
            plantacion: Plantacion a regar
            plantacion_service: Servicio para operaciones de riego
        """
        threading.Thread.__init__(self, daemon=True)
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        self._detenido = threading.Event()
        
        # Estado de sensores
        self._ultima_temperatura = 20.0
        self._ultima_humedad = 50.0
        
        # Suscribirse a sensores
        sensor_temperatura.agregar_observador(self)
        sensor_humedad.agregar_observador(self)

    def actualizar(self, evento: float) -> None:
        """
        Recibe actualizaciones de sensores (patron Observer).

        Args:
            evento: Valor del sensor (temperatura o humedad)
        """
        # El evento es float, determinar si es temperatura o humedad por rango
        if -25 <= evento <= 50:
            self._ultima_temperatura = evento
        elif 0 <= evento <= 100:
            self._ultima_humedad = evento

    def run(self) -> None:
        """
        Ejecuta control automatico de riego.
        """
        while not self._detenido.is_set():
            self._evaluar_y_regar()
            time.sleep(INTERVALO_CONTROL_RIEGO)

    def _evaluar_y_regar(self) -> None:
        """
        Evalua condiciones y riega si es necesario.
        """
        temperatura = self._ultima_temperatura
        humedad = self._ultima_humedad

        # Condiciones de riego
        if (TEMP_MIN_RIEGO <= temperatura <= TEMP_MAX_RIEGO) and (humedad < HUMEDAD_MAX_RIEGO):
            try:
                print(f"\n[RIEGO AUTO] Temp: {temperatura:.1f}C, Humedad: {humedad:.1f}% - REGANDO")
                self._plantacion_service.regar(self._plantacion)
            except AguaAgotadaException as e:
                print(f"[RIEGO AUTO] {e.get_user_message()}")

    def detener(self) -> None:
        """
        Detiene el thread de forma segura.
        """
        self._detenido.set()


################################################################################
# DIRECTORIO: riego\sensores
################################################################################

# ==============================================================================
# ARCHIVO 46/66: __init__.py
# Directorio: riego\sensores
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\riego\sensores\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 47/66: humedad_reader_task.py
# Directorio: riego\sensores
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\riego\sensores\humedad_reader_task.py
# ==============================================================================

"""
Thread sensor de humedad (Observable).

Lee humedad ambiental y notifica a observadores.
"""

# Standard library
import threading
import time
import random

# Local application
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    SENSOR_HUMEDAD_MIN,
    SENSOR_HUMEDAD_MAX
)


class HumedadReaderTask(threading.Thread, Observable[float]):
    """
    Thread daemon que lee humedad periodicamente.

    Implementa patron Observer como Observable[float].
    """

    def __init__(self):
        """
        Inicializa el thread sensor de humedad.
        """
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """
        Ejecuta lectura continua de humedad.
        """
        while not self._detenido.is_set():
            humedad = self._leer_humedad()
            self.notificar_observadores(humedad)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)

    def _leer_humedad(self) -> float:
        """
        Lee humedad del sensor (simulado).

        Returns:
            Humedad en porcentaje
        """
        return random.uniform(SENSOR_HUMEDAD_MIN, SENSOR_HUMEDAD_MAX)

    def detener(self) -> None:
        """
        Detiene el thread de forma segura.
        """
        self._detenido.set()

# ==============================================================================
# ARCHIVO 48/66: temperatura_reader_task.py
# Directorio: riego\sensores
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\riego\sensores\temperatura_reader_task.py
# ==============================================================================

"""
Thread sensor de temperatura (Observable).

Lee temperatura ambiental y notifica a observadores.
"""

# Standard library
import threading
import time
import random

# Local application
from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    SENSOR_TEMP_MIN,
    SENSOR_TEMP_MAX
)


class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """
    Thread daemon que lee temperatura periodicamente.

    Implementa patron Observer como Observable[float].
    """

    def __init__(self):
        """
        Inicializa el thread sensor de temperatura.
        """
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()

    def run(self) -> None:
        """
        Ejecuta lectura continua de temperatura.
        """
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)

    def _leer_temperatura(self) -> float:
        """
        Lee temperatura del sensor (simulado).

        Returns:
            Temperatura en grados Celsius
        """
        return random.uniform(SENSOR_TEMP_MIN, SENSOR_TEMP_MAX)

    def detener(self) -> None:
        """
        Detiene el thread de forma segura.
        """
        self._detenido.set()


################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 49/66: __init__.py
# Directorio: servicios
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios\cultivos
################################################################################

# ==============================================================================
# ARCHIVO 50/66: __init__.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\cultivos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 51/66: arbol_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\cultivos\arbol_service.py
# ==============================================================================

"""
Servicio base para arboles.

Contiene logica de negocio comun a todos los arboles.
"""

# Standard library
from abc import ABC
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService, ABC):
    """
    Servicio base para arboles.

    Los arboles pueden crecer en altura al recibir agua.
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """
        Inicializa el servicio de arbol.

        Args:
            estrategia_absorcion: Estrategia de absorcion de agua
        """
        super().__init__(estrategia_absorcion)

    def mostrar_datos(self, arbol: 'Arbol') -> None:
        """
        Muestra datos del arbol incluyendo altura.

        Args:
            arbol: Arbol a mostrar
        """
        super().mostrar_datos(arbol)
        print(f"ID: {arbol.get_id()}")
        print(f"Altura: {arbol.get_altura()} m")

# ==============================================================================
# ARCHIVO 52/66: cultivo_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\cultivos\cultivo_service.py
# ==============================================================================

"""
Servicio base para cultivos.

Contiene logica de negocio comun a todos los cultivos.
"""

# Standard library
from abc import ABC
from datetime import date
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService(ABC):
    """
    Servicio base abstracto para cultivos.

    Implementa logica comun y delega absorcion a estrategias.
    """

    def __init__(self, estrategia_absorcion: AbsorcionAguaStrategy):
        """
        Inicializa el servicio con una estrategia de absorcion.

        Args:
            estrategia_absorcion: Estrategia para calcular absorcion de agua
        """
        self._estrategia_absorcion = estrategia_absorcion

    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        """
        Calcula y aplica absorcion de agua al cultivo.

        Args:
            cultivo: Cultivo que absorbe agua

        Returns:
            Cantidad de agua absorbida en litros
        """
        fecha_actual = date.today()
        temperatura = 20.0
        humedad = 50.0

        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha_actual,
            temperatura,
            humedad,
            cultivo
        )

        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos basicos del cultivo.

        Args:
            cultivo: Cultivo a mostrar
        """
        print(f"Cultivo: {type(cultivo).__name__}")
        print(f"Superficie: {cultivo.get_superficie()} m2")
        print(f"Agua almacenada: {cultivo.get_agua()} L")

# ==============================================================================
# ARCHIVO 53/66: cultivo_service_registry.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\cultivos\cultivo_service_registry.py
# ==============================================================================

"""
Registry de servicios de cultivos (Patron Singleton + Registry).

Proporciona acceso centralizado a servicios de cultivos con dispatch polimorfico.
"""

# Standard library
from threading import Lock
from typing import TYPE_CHECKING, Dict, Callable

# Local application
from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.cultivos.pino import Pino
    from python_forestacion.entidades.cultivos.olivo import Olivo
    from python_forestacion.entidades.cultivos.lechuga import Lechuga
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class CultivoServiceRegistry:
    """
    Registry Singleton de servicios de cultivos.

    Implementa:
    - Patron Singleton: Una sola instancia compartida
    - Patron Registry: Dispatch polimorfico sin isinstance()
    """

    _instance = None
    _lock = Lock()

    def __new__(cls):
        """
        Crea o retorna la instancia unica (thread-safe).

        Returns:
            Instancia unica del registry
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar_servicios()
        return cls._instance

    def _inicializar_servicios(self) -> None:
        """
        Inicializa los servicios y registros una sola vez.
        """
        # Servicios especificos
        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()

        # Registry de handlers (evita isinstance cascades)
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria

        self._absorber_agua_handlers: Dict[type, Callable] = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }

        self._mostrar_datos_handlers: Dict[type, Callable] = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }

    @classmethod
    def get_instance(cls) -> 'CultivoServiceRegistry':
        """
        Obtiene la instancia unica del registry.

        Returns:
            Instancia del registry
        """
        if cls._instance is None:
            cls()
        return cls._instance

    def absorber_agua(self, cultivo: 'Cultivo') -> int:
        """
        Absorbe agua usando dispatch polimorfico.

        Args:
            cultivo: Cultivo que absorbe agua

        Returns:
            Cantidad de agua absorbida

        Raises:
            ValueError: Si el tipo de cultivo no esta registrado
        """
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo de cultivo no registrado: {tipo}")
        return self._absorber_agua_handlers[tipo](cultivo)

    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos usando dispatch polimorfico.

        Args:
            cultivo: Cultivo a mostrar

        Raises:
            ValueError: Si el tipo de cultivo no esta registrado
        """
        tipo = type(cultivo)
        if tipo not in self._mostrar_datos_handlers:
            raise ValueError(f"Tipo de cultivo no registrado: {tipo}")
        self._mostrar_datos_handlers[tipo](cultivo)

    def _absorber_agua_pino(self, cultivo: 'Pino') -> int:
        """Handler para absorber agua de Pino."""
        return self._pino_service.absorver_agua(cultivo)

    def _absorber_agua_olivo(self, cultivo: 'Olivo') -> int:
        """Handler para absorber agua de Olivo."""
        return self._olivo_service.absorver_agua(cultivo)

    def _absorber_agua_lechuga(self, cultivo: 'Lechuga') -> int:
        """Handler para absorber agua de Lechuga."""
        return self._lechuga_service.absorver_agua(cultivo)

    def _absorber_agua_zanahoria(self, cultivo: 'Zanahoria') -> int:
        """Handler para absorber agua de Zanahoria."""
        return self._zanahoria_service.absorver_agua(cultivo)

    def _mostrar_datos_pino(self, cultivo: 'Pino') -> None:
        """Handler para mostrar datos de Pino."""
        self._pino_service.mostrar_datos(cultivo)

    def _mostrar_datos_olivo(self, cultivo: 'Olivo') -> None:
        """Handler para mostrar datos de Olivo."""
        self._olivo_service.mostrar_datos(cultivo)

    def _mostrar_datos_lechuga(self, cultivo: 'Lechuga') -> None:
        """Handler para mostrar datos de Lechuga."""
        self._lechuga_service.mostrar_datos(cultivo)

    def _mostrar_datos_zanahoria(self, cultivo: 'Zanahoria') -> None:
        """Handler para mostrar datos de Zanahoria."""
        self._zanahoria_service.mostrar_datos(cultivo)

# ==============================================================================
# ARCHIVO 54/66: lechuga_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\cultivos\lechuga_service.py
# ==============================================================================

"""
Servicio para Lechuga.

Logica de negocio especifica para cultivos de tipo Lechuga.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_LECHUGA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """
    Servicio para cultivos tipo Lechuga.

    Implementa logica especifica de lechugas (absorcion constante).
    """

    def __init__(self):
        """
        Inicializa servicio con estrategia constante.
        """
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_LECHUGA))

    def mostrar_datos(self, lechuga: 'Lechuga') -> None:
        """
        Muestra datos de la lechuga incluyendo variedad e invernadero.

        Args:
            lechuga: Lechuga a mostrar
        """
        super().mostrar_datos(lechuga)
        print(f"Variedad: {lechuga.get_variedad()}")
        print(f"Invernadero: {lechuga.get_invernadero()}")

# ==============================================================================
# ARCHIVO 55/66: olivo_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\cultivos\olivo_service.py
# ==============================================================================

"""
Servicio para Olivo.

Logica de negocio especifica para cultivos de tipo Olivo.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """
    Servicio para cultivos tipo Olivo.

    Implementa logica especifica de olivos (crecimiento lento, absorcion estacional).
    """

    def __init__(self):
        """
        Inicializa servicio con estrategia estacional.
        """
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, olivo: 'Olivo') -> int:
        """
        Absorbe agua y hace crecer el olivo.

        Args:
            olivo: Olivo que absorbe agua

        Returns:
            Cantidad de agua absorbida
        """
        agua_absorvida = super().absorver_agua(olivo)
        
        # Olivo crece lentamente al recibir agua
        altura_actual = olivo.get_altura()
        olivo.set_altura(altura_actual + CRECIMIENTO_OLIVO)
        
        return agua_absorvida

    def mostrar_datos(self, olivo: 'Olivo') -> None:
        """
        Muestra datos del olivo incluyendo tipo de aceituna.

        Args:
            olivo: Olivo a mostrar
        """
        super().mostrar_datos(olivo)
        print(f"Tipo de aceituna: {olivo.get_tipo_aceituna().value}")

# ==============================================================================
# ARCHIVO 56/66: pino_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\cultivos\pino_service.py
# ==============================================================================

"""
Servicio para Pino.

Logica de negocio especifica para cultivos de tipo Pino.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """
    Servicio para cultivos tipo Pino.

    Implementa logica especifica de pinos (crecimiento, absorcion estacional).
    """

    def __init__(self):
        """
        Inicializa servicio con estrategia estacional.
        """
        super().__init__(AbsorcionSeasonalStrategy())

    def absorver_agua(self, pino: 'Pino') -> int:
        """
        Absorbe agua y hace crecer el pino.

        Args:
            pino: Pino que absorbe agua

        Returns:
            Cantidad de agua absorbida
        """
        agua_absorvida = super().absorver_agua(pino)
        
        # Pino crece al recibir agua
        altura_actual = pino.get_altura()
        pino.set_altura(altura_actual + CRECIMIENTO_PINO)
        
        return agua_absorvida

    def mostrar_datos(self, pino: 'Pino') -> None:
        """
        Muestra datos del pino incluyendo variedad.

        Args:
            pino: Pino a mostrar
        """
        super().mostrar_datos(pino)
        print(f"Variedad: {pino.get_variedad()}")

# ==============================================================================
# ARCHIVO 57/66: zanahoria_service.py
# Directorio: servicios\cultivos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\cultivos\zanahoria_service.py
# ==============================================================================

"""
Servicio para Zanahoria.

Logica de negocio especifica para cultivos de tipo Zanahoria.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_ZANAHORIA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """
    Servicio para cultivos tipo Zanahoria.

    Implementa logica especifica de zanahorias (absorcion constante).
    """

    def __init__(self):
        """
        Inicializa servicio con estrategia constante.
        """
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_ZANAHORIA))

    def mostrar_datos(self, zanahoria: 'Zanahoria') -> None:
        """
        Muestra datos de la zanahoria incluyendo si es baby carrot.

        Args:
            zanahoria: Zanahoria a mostrar
        """
        super().mostrar_datos(zanahoria)
        tipo = "Baby carrot" if zanahoria.is_baby_carrot() else "Regular"
        print(f"Tipo: {tipo}")


################################################################################
# DIRECTORIO: servicios\negocio
################################################################################

# ==============================================================================
# ARCHIVO 58/66: __init__.py
# Directorio: servicios\negocio
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\negocio\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 59/66: fincas_service.py
# Directorio: servicios\negocio
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\negocio\fincas_service.py
# ==============================================================================

"""
Servicio de alto nivel para gestion de fincas.

Orquesta operaciones complejas sobre multiples fincas.
"""

# Standard library
from typing import TYPE_CHECKING, Dict, Type, TypeVar

# Local application
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.negocio.paquete import Paquete

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
    from python_forestacion.entidades.cultivos.cultivo import Cultivo

T = TypeVar('T', bound='Cultivo')


class FincasService:
    """
    Servicio de alto nivel para operaciones sobre fincas.

    Gestiona multiples fincas y proporciona operaciones complejas.
    """

    def __init__(self):
        """
        Inicializa el servicio con diccionario de fincas.
        """
        self._fincas: Dict[int, 'RegistroForestal'] = {}
        self._plantacion_service = PlantacionService()

    def add_finca(self, registro: 'RegistroForestal') -> None:
        """
        Agrega una finca al sistema.

        Args:
            registro: Registro forestal a agregar
        """
        id_padron = registro.get_id_padron()
        self._fincas[id_padron] = registro
        print(f"Finca {id_padron} agregada al sistema")

    def buscar_finca(self, id_padron: int) -> 'RegistroForestal':
        """
        Busca una finca por su ID de padron.

        Args:
            id_padron: ID del padron a buscar

        Returns:
            Registro forestal encontrado

        Raises:
            KeyError: Si la finca no existe
        """
        if id_padron not in self._fincas:
            raise KeyError(f"Finca con padron {id_padron} no encontrada")
        return self._fincas[id_padron]

    def fumigar(self, id_padron: int, plaguicida: str) -> None:
        """
        Fumiga una finca especifica.

        Args:
            id_padron: ID del padron a fumigar
            plaguicida: Tipo de plaguicida
        """
        registro = self.buscar_finca(id_padron)
        plantacion = registro.get_plantacion()
        self._plantacion_service.fumigar(plantacion, plaguicida)

    def cosechar_yempaquetar(self, tipo_cultivo: Type[T]) -> Paquete[T]:
        """
        Cosecha todos los cultivos de un tipo especifico de todas las fincas.

        Args:
            tipo_cultivo: Clase del tipo de cultivo a cosechar

        Returns:
            Paquete con todos los cultivos cosechados del tipo especificado
        """
        paquete: Paquete[T] = Paquete(tipo_cultivo)

        # Recorrer todas las fincas
        for registro in self._fincas.values():
            plantacion = registro.get_plantacion()
            cultivos = plantacion.get_cultivos()

            # Filtrar cultivos del tipo especificado
            cultivos_tipo = [c for c in cultivos if isinstance(c, tipo_cultivo)]

            # Agregar al paquete
            for cultivo in cultivos_tipo:
                paquete.agregar(cultivo)

            # Remover de la plantacion
            for cultivo in cultivos_tipo:
                plantacion.eliminar_cultivo(cultivo)
                superficie_actual = plantacion.get_superficie_ocupada()
                plantacion.set_superficie_ocupada(superficie_actual - cultivo.get_superficie())

        cantidad = paquete.get_cantidad()
        print(f"\nCOSECHANDO {cantidad} unidades de {tipo_cultivo}")

        return paquete

# ==============================================================================
# ARCHIVO 60/66: paquete.py
# Directorio: servicios\negocio
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\negocio\paquete.py
# ==============================================================================

"""
Clase Paquete generica tipo-segura.

Representa un paquete de cultivos empaquetados.
"""

# Standard library
from typing import Generic, TypeVar, List

T = TypeVar('T')


class Paquete(Generic[T]):
    """
    Paquete generico tipo-seguro para empaquetar cultivos.

    Type Parameters:
        T: Tipo de cultivo contenido en el paquete
    """

    _contador_id = 0

    def __init__(self, tipo_contenido: type):
        """
        Inicializa un paquete vacio.

        Args:
            tipo_contenido: Clase del tipo de cultivo contenido
        """
        Paquete._contador_id += 1
        self._id_paquete = Paquete._contador_id
        self._tipo_contenido = tipo_contenido
        self._contenido: List[T] = []

    def agregar(self, item: T) -> None:
        """
        Agrega un item al paquete.

        Args:
            item: Item a agregar
        """
        self._contenido.append(item)

    def get_contenido(self) -> List[T]:
        """
        Obtiene el contenido del paquete.

        Returns:
            Lista de items contenidos
        """
        return self._contenido.copy()

    def get_cantidad(self) -> int:
        """
        Obtiene la cantidad de items.

        Returns:
            Cantidad de items en el paquete
        """
        return len(self._contenido)

    def get_tipo_contenido(self) -> type:
        """
        Obtiene el tipo de contenido.

        Returns:
            Clase del tipo contenido
        """
        return self._tipo_contenido

    def get_id_paquete(self) -> int:
        """
        Obtiene el ID del paquete.

        Returns:
            ID unico del paquete
        """
        return self._id_paquete

    def mostrar_contenido_caja(self) -> None:
        """
        Muestra el contenido del paquete.
        """
        print("\nContenido de la caja:")
        print(f"  Tipo: {self._tipo_contenido.__name__}")
        print(f"  Cantidad: {self.get_cantidad()}")
        print(f"  ID Paquete: {self._id_paquete}")


################################################################################
# DIRECTORIO: servicios\personal
################################################################################

# ==============================================================================
# ARCHIVO 61/66: __init__.py
# Directorio: servicios\personal
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\personal\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 62/66: trabajador_service.py
# Directorio: servicios\personal
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\personal\trabajador_service.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios\terrenos
################################################################################

# ==============================================================================
# ARCHIVO 63/66: __init__.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\terrenos\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 64/66: plantacion_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\terrenos\plantacion_service.py
# ==============================================================================

"""
Servicio para Plantacion.

Logica de negocio para plantaciones agricolas.
"""

# Standard library
from typing import TYPE_CHECKING

# Local application
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException
from python_forestacion.constantes import AGUA_MINIMA

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class PlantacionService:
    """
    Servicio para gestion de plantaciones.

    Proporciona operaciones como plantar, regar, cosechar y fumigar.
    """

    def __init__(self):
        """
        Inicializa el servicio con factory y registry.
        """
        self._factory = CultivoFactory()
        self._registry = CultivoServiceRegistry.get_instance()

    def plantar(self, plantacion: 'Plantacion', especie: str, cantidad: int) -> None:
        """
        Planta cultivos de una especie especifica.

        Args:
            plantacion: Plantacion donde plantar
            especie: Tipo de cultivo a plantar
            cantidad: Cantidad de cultivos

        Raises:
            SuperficieInsuficienteException: Si no hay superficie suficiente
        """
        # Crear cultivo de muestra para calcular superficie
        cultivo_muestra = self._factory.crear_cultivo(especie)
        superficie_requerida = cultivo_muestra.get_superficie() * cantidad
        superficie_disponible = plantacion.get_superficie() - plantacion.get_superficie_ocupada()

        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(superficie_requerida, superficie_disponible)

        # Plantar cultivos
        for i in range(cantidad):
            cultivo = self._factory.crear_cultivo(especie)
            plantacion.agregar_cultivo(cultivo)

        # Actualizar superficie ocupada
        nueva_superficie_ocupada = plantacion.get_superficie_ocupada() + superficie_requerida
        plantacion.set_superficie_ocupada(nueva_superficie_ocupada)

        print(f"{cantidad} {especie}(s) plantado(s) exitosamente")

    def regar(self, plantacion: 'Plantacion') -> None:
        """
        Riega todos los cultivos de la plantacion.

        Args:
            plantacion: Plantacion a regar

        Raises:
            AguaAgotadaException: Si no hay agua suficiente
        """
        agua_disponible = plantacion.get_agua_disponible()
        
        if agua_disponible < AGUA_MINIMA:
            raise AguaAgotadaException(AGUA_MINIMA, agua_disponible)

        # Consumir agua de la plantacion
        plantacion.set_agua_disponible(agua_disponible - AGUA_MINIMA)

        # Cada cultivo absorbe agua segun su estrategia
        cultivos = plantacion.get_cultivos()
        for cultivo in cultivos:
            self._registry.absorber_agua(cultivo)

        print(f"Plantacion regada. Agua restante: {plantacion.get_agua_disponible()} L")

    def cosechar(self, plantacion: 'Plantacion') -> None:
        """
        Cosecha todos los cultivos de la plantacion.

        Args:
            plantacion: Plantacion a cosechar
        """
        cultivos = plantacion.get_cultivos()
        cantidad = len(cultivos)

        # Vaciar lista de cultivos
        plantacion.set_cultivos([])
        plantacion.set_superficie_ocupada(0.0)

        print(f"Cosechados {cantidad} cultivos")

    def fumigar(self, plantacion: 'Plantacion', plaguicida: str) -> None:
        """
        Fumiga la plantacion con un plaguicida.

        Args:
            plantacion: Plantacion a fumigar
            plaguicida: Tipo de plaguicida a aplicar
        """
        print(f"Fumigando plantacion con: {plaguicida}")

    def mostrar_cultivos(self, plantacion: 'Plantacion') -> None:
        """
        Muestra todos los cultivos de la plantacion.

        Args:
            plantacion: Plantacion a mostrar
        """
        cultivos = plantacion.get_cultivos()
        print(f"\nCantidad de cultivos plantados: {len(cultivos)}")
        
        if len(cultivos) > 0:
            print("Listado de Cultivos plantados")
            print("_" * 28)
            print()
            
            for cultivo in cultivos:
                self._registry.mostrar_datos(cultivo)
                print()

# ==============================================================================
# ARCHIVO 65/66: registro_forestal_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\terrenos\registro_forestal_service.py
# ==============================================================================

"""
Servicio para RegistroForestal.

Logica de negocio para registros forestales (persistencia).
"""

# Standard library
import pickle
import os
from typing import TYPE_CHECKING

# Local application
from python_forestacion.excepciones.persistencia_exception import (
    PersistenciaException,
    TipoOperacionPersistencia
)
from python_forestacion.excepciones.mensajes_exception import (
    MSG_PERSISTENCIA_ERROR_ESCRITURA_USER,
    MSG_PERSISTENCIA_ERROR_ESCRITURA_TECH,
    MSG_PERSISTENCIA_ERROR_LECTURA_USER,
    MSG_PERSISTENCIA_ERROR_LECTURA_TECH,
    MSG_PERSISTENCIA_ARCHIVO_NO_ENCONTRADO_USER,
    MSG_PERSISTENCIA_ARCHIVO_NO_ENCONTRADO_TECH,
    MSG_PROPIETARIO_VACIO
)
from python_forestacion.constantes import DIRECTORIO_DATA, EXTENSION_DATA

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal


class RegistroForestalService:
    """
    Servicio para gestion de registros forestales.

    Proporciona operaciones de persistencia y mostracion de registros.
    """

    def mostrar_datos(self, registro: 'RegistroForestal') -> None:
        """
        Muestra todos los datos del registro forestal.

        Args:
            registro: Registro a mostrar
        """
        print("\nREGISTRO FORESTAL")
        print("=" * 17)
        print(f"Padron:      {registro.get_id_padron()}")
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Avaluo:      {registro.get_avaluo()}")
        
        tierra = registro.get_tierra()
        print(f"Domicilio:   {tierra.get_domicilio()}")
        print(f"Superficie: {tierra.get_superficie()}")
        
        plantacion = registro.get_plantacion()
        cultivos = plantacion.get_cultivos()
        print(f"Cantidad de cultivos plantados: {len(cultivos)}")
        
        if len(cultivos) > 0:
            print("Listado de Cultivos plantados")
            print("_" * 28)
            print()
            
            from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
            registry = CultivoServiceRegistry.get_instance()
            
            for cultivo in cultivos:
                registry.mostrar_datos(cultivo)
                print()

    def persistir(self, registro: 'RegistroForestal') -> None:
        """
        Persiste un registro forestal en disco usando Pickle.

        Args:
            registro: Registro a persistir

        Raises:
            PersistenciaException: Si ocurre error al guardar
        """
        propietario = registro.get_propietario()
        
        # Crear directorio si no existe
        if not os.path.exists(DIRECTORIO_DATA):
            os.makedirs(DIRECTORIO_DATA)
        
        nombre_archivo = os.path.join(DIRECTORIO_DATA, f"{propietario}{EXTENSION_DATA}")
        
        file_handle = None
        try:
            file_handle = open(nombre_archivo, 'wb')
            pickle.dump(registro, file_handle)
            print(f"Registro de {propietario} persistido exitosamente en {nombre_archivo}")
        
        except Exception as e:
            tech_msg = MSG_PERSISTENCIA_ERROR_ESCRITURA_TECH.format(archivo=nombre_archivo)
            raise PersistenciaException(
                MSG_PERSISTENCIA_ERROR_ESCRITURA_USER,
                tech_msg,
                nombre_archivo,
                TipoOperacionPersistencia.ESCRITURA
            ) from e
        
        finally:
            if file_handle is not None:
                file_handle.close()

    @staticmethod
    def leer_registro(propietario: str) -> 'RegistroForestal':
        """
        Lee un registro forestal desde disco.

        Args:
            propietario: Nombre del propietario

        Returns:
            Registro forestal deserializado

        Raises:
            ValueError: Si el propietario es vacio
            PersistenciaException: Si ocurre error al leer
        """
        if not propietario or propietario.strip() == "":
            raise ValueError(MSG_PROPIETARIO_VACIO)
        
        nombre_archivo = os.path.join(DIRECTORIO_DATA, f"{propietario}{EXTENSION_DATA}")
        
        if not os.path.exists(nombre_archivo):
            tech_msg = MSG_PERSISTENCIA_ARCHIVO_NO_ENCONTRADO_TECH.format(archivo=nombre_archivo)
            raise PersistenciaException(
                MSG_PERSISTENCIA_ARCHIVO_NO_ENCONTRADO_USER,
                tech_msg,
                nombre_archivo,
                TipoOperacionPersistencia.LECTURA
            )
        
        file_handle = None
        try:
            file_handle = open(nombre_archivo, 'rb')
            registro = pickle.load(file_handle)
            print(f"Registro de {propietario} recuperado exitosamente desde {nombre_archivo}")
            return registro
        
        except Exception as e:
            tech_msg = MSG_PERSISTENCIA_ERROR_LECTURA_TECH.format(archivo=nombre_archivo)
            raise PersistenciaException(
                MSG_PERSISTENCIA_ERROR_LECTURA_USER,
                tech_msg,
                nombre_archivo,
                TipoOperacionPersistencia.LECTURA
            ) from e
        
        finally:
            if file_handle is not None:
                file_handle.close()

# ==============================================================================
# ARCHIVO 66/66: tierra_service.py
# Directorio: servicios\terrenos
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\servicios\terrenos\tierra_service.py
# ==============================================================================

"""
Servicio para Tierra.

Logica de negocio para terrenos catastrales.
"""

# Local application
from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion
from python_forestacion.constantes import AGUA_INICIAL_PLANTACION


class TierraService:
    """
    Servicio para gestion de terrenos.

    Proporciona operaciones de negocio sobre terrenos catastrales.
    """

    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        """
        Crea un terreno con una plantacion asociada.

        Args:
            id_padron_catastral: ID del padron catastral
            superficie: Superficie en metros cuadrados
            domicilio: Domicilio del terreno
            nombre_plantacion: Nombre de la plantacion

        Returns:
            Tierra creada con plantacion asociada
        """
        tierra = Tierra(
            id_padron_catastral=id_padron_catastral,
            superficie=superficie,
            domicilio=domicilio
        )

        plantacion = Plantacion(
            nombre=nombre_plantacion,
            superficie=superficie,
            agua=AGUA_INICIAL_PLANTACION
        )

        tierra.set_finca(plantacion)

        return tierra


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 66
# Generado: 2025-10-21 18:31:01
################################################################################

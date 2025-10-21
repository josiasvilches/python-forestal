"""
Archivo integrador generado automaticamente
Directorio: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\terrenos
Fecha: 2025-10-21 18:36:35
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\terrenos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\terrenos\plantacion.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\terrenos\registro_forestal.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\terrenos\tierra.py
# ================================================================================

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


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
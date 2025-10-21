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
"""
Archivo integrador generado automaticamente
Directorio: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos
Fecha: 2025-10-21 18:36:35
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\arbol.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\cultivo.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\hortaliza.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\lechuga.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\olivo.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\pino.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\tipo_aceituna.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\Parcial\python_forestacion\entidades\cultivos\zanahoria.py
# ================================================================================

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


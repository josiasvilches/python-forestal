"""
Archivo integrador generado automaticamente
Directorio: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/negocio
Fecha: 2025-10-22 09:43:42
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/negocio/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: fincas_service.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/negocio/fincas_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: /home/josiasvilches/cursada/disenosistemas/python-forestal/python_forestacion/servicios/negocio/paquete.py
# ================================================================================

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


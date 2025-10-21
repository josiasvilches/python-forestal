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
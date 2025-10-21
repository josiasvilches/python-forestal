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
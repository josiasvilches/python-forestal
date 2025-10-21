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
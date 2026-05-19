class Reserva:
    """
    Clase que representa una reserva de clase grupal en el gimnasio FitUdeA.
    """
    id: int
    fecha: str
    hora: str
    estado: str

    def __init__(self, id=0, fecha="N.A.", hora="N.A.", estado="activa"):
        self.id = id
        self.fecha = fecha
        self.hora = hora
        self.estado = estado

    def cambiar_estado_cancelada(self) -> None:
        """
        Cambia el estado de la reserva a cancelada.
        """
        self.estado = "cancelada"
        print("La reserva ha sido cancelada exitosamente.")

    def mostrar_reserva(self)->None:
        """
        Este método muestra los detalles de la reserva.
        """
        print("\n=== Mostrar reserva ===")
        print("El id de la reserva es", self.id)
        print("La fecha de la reserva es", self.fecha)
        print("La hora de la reserva es", self.hora)
        print("El estado de la reserva es", self.estado)
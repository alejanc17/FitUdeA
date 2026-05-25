class Pago:
    id: int
    fecha : str
    concepto: str
    saldo_vigencia: str
    valor_cancelado: float

    def __init__(self, id=0, fecha="N.A.", concepto="N.A.", saldo_vigencia="N.A.", valor_cancelado=0.0):
        self.id= id
        self.fecha= fecha
        self.concepto= concepto
        self.saldo_vigencia=saldo_vigencia
        self.valor_cancelado= valor_cancelado

    def mostrar_pago(self)->None:
        """ Muestra en pantalla los detalles del pago"""
        print("\n=== Detalle del Pago ===")
        print("El id del pago es", self.id)
        print("La fecha de pago fue", self.fecha)
        print("El concepto de pago es", self.concepto)
        print("El saldo de vigencia es", self.saldo_vigencia)
        print("El valor cancelado fue de", self.valor_cancelado)

    def calcular_descuento(self, tipo_plan, tipo_afiliacion, estrato, edad, valor_base )->float:
        #Plan anual → 25% de descuento
        #Docente o egresado mayor de 50 años → 10% adicional
        #Estudiante estrato 1 o 2 → 15% de descuento

        descuento= 0.0
        if tipo_plan == "anual":
            descuento += valor_base * 12 * 0.25

        if (tipo_afiliacion == 2 or tipo_afiliacion == 3) and edad > 50:
            descuento += valor_base * 0.10

        if tipo_afiliacion == 1 and (estrato == 1 or estrato == 2):
            descuento += valor_base * 0.15

        return descuento
# Clase hecha por Manuela (lista)
import numpy as np
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
        self.valores_afiliacion = np.empty(4, dtype=float)

    def mostrar_pago(self)->None:
        """ Muestra en pantalla los detalles del pago"""
        print("\n=== Detalle del Pago ===")
        print("El id del pago es", self.id)
        print("La fecha de pago fue", self.fecha)
        print("El concepto de pago es", self.concepto)
        print("El saldo de vigencia es", self.saldo_vigencia)
        print("El valor cancelado fue de", self.valor_cancelado)

    def calcular_descuento(self, tipo_plan, tipo_afiliacion, estrato, edad, valor_base) -> float:
        """
        Calcula y retorna el valor del descuento según las reglas de negocio.
        PARAM:
            tipo_plan (str): Tipo de plan (mensual o anual).
            tipo_afiliacion (int): Tipo de afiliación (1.estudiante, 2.docente, 3.egresado, 4.particular).
            estrato (int): Estrato socioeconómico del usuario (1-6).
            edad (int): Edad actual del usuario en años.
            valor_base (float): Valor base mensual de la membresía.
        RETURN: (float) Valor total del descuento a aplicar.
        """
        descuento = 0.0

        if tipo_plan == "anual":
            valor_total = valor_base * 12
        else:
            valor_total = valor_base

        # Regla 1: Plan anual → 25% de descuento
        if tipo_plan == "anual":
            descuento += valor_total * 0.25

        # Regla 2: Docente o egresado mayor de 50 años → 10% adicional
        if (tipo_afiliacion == 2 or tipo_afiliacion == 3) and edad > 50:
            descuento += valor_total * 0.10

        # Regla 3: Estudiante estrato 1 o 2 → 15% de descuento
        if tipo_afiliacion == 1 and (estrato == 1 or estrato == 2):
            descuento += valor_total * 0.15

        return descuento

    #R18: Actualizar el valor mensual de los tipos de afiliación.
    def actualizar_valor_afiliacion(self) -> None:
        tipos = np.array(["Estudiante", "Egresado", "Docente", "Particular"])
        for i in range(len(tipos)):
            print(f" # {i+1}. {tipos[i]} ${self.valores_afiliacion[i]}")
    
        opcion = int(input("Ingrese el tipo de afiliado a modificar (1-4): "))
        nuevo_valor = float(input("Ingrese el nuevo valor mensual: "))
        self.valores_afiliacion[opcion - 1] = nuevo_valor
        print("Valor actualizado exitosamente.")
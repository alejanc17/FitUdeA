class Membresia:
    id: int
    tipo_plan: str
    fecha_inicio: str
    fecha_vencimiento: str
    estado: str

    def __init__(self, id=0,tipo_plan="", fecha_inicio="",fecha_vencimiento="", estado=""):
        self.id = id
        self.tipo_plan = tipo_plan
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado = estado
    
    #R17: Actualizar el estado o vigencia de un plan de membresía
    def actualizar_estado_membresia(self):

        print("\n === Actualizar Membresía ===")

        while True:
            nuevo_estado = input("Ingrese el nuevo estado de la membresía (activa / inactiva / vencida): ").lower()

            if nuevo_estado=="":
                break

            if nuevo_estado == "activa" or nuevo_estado == "inactiva" or nuevo_estado == "vencida":
                self.estado = nuevo_estado
                break
            else:
                print("¡Error! Opción no válida.")
        
        nueva_fecha = input("Ingrese la nueva fecha de vencimiento (dia/mes/año): ")

        if nueva_fecha != "":
            self.fecha_vencimiento = nueva_fecha

        print("Membresía actualizada exitosamente")
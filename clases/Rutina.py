class Rutina:
    id:int
    nombre:str
    descripcion_general: str
    objetivo_principal: str
    nivel_dificultad: str
    duracion_estimada:int
    estado: str
    ejercicios: str

    def __init__(self,id=0,nombre="N.A.", descripcion_general="N.A.", objetivo_principal="N.A.", nivel_dificultad="N.A.",
                 duracio_estimada=0, estado="N.A."):
        self.id= id
        self.nombre= nombre
        self.descripcion_general= descripcion_general
        self.objetivo_principal= objetivo_principal
        self.nivel_dificultad=nivel_dificultad
        self.duracion_estimada=duracio_estimada
        self.estado=estado
        self.ejercicios=[]

    def agregar_ejercicio(self,ejercicio)->None:
        self.ejercicios.append(ejercicio)


    def mostrar_detalle_rutina(self)->None:
        print("\n=== Detalle de la rutina ===")
        print("El id de la rutina es", self.id)
        print("El nombre de la rutina es", self.nombre)
        print("Descripción de esta rutina", self.descripcion_general)
        print("El objetivo principal de esta rutina es", self.objetivo_principal)
        print("La duración estimada de la rutina será de", self.duracion_estimada)
        print("El estado de la rutina es", self.estado)
        if len(self.ejercicios)==0:
            print("No hay ejercicios")
        else:
            for i in range(len(self.ejercicios)):
                print(f"\n Ejercicio #{i+1}")
                print(self.ejericicios[i])



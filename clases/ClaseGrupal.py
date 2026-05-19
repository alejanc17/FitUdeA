class Clase_Grupal:
    id:int
    nombre:str
    descripcion: str
    fecha: str
    hora: str
    duracion: int
    cupo_maximo: int
    cant_usuarios_inscritos: int
    
    def __init__(self,id=0, nombre="N.A.", descripcion="N.A.", fecha="N.A.", hora="N.A.", duracion=0,cupo_maximo=0,cant_usuarios_inscritos=0):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.fecha= fecha
        self.hora= hora
        self.duracion= duracion
        self.cupo_maximo= cupo_maximo
        self.cant_usuarios_inscritos= cant_usuarios_inscritos
        self.usuarios_inscritos = []  # arreglo de usuarios inscritos

    def sumar_inscritos(self, usuario)->None:
        self.usuarios_inscritos.append(usuario)
        self.cant_usuarios_inscritos+=1

    def restar_inscrito(self,usuario)->None:
        self.usuarios_inscritos.remove(usuario)
        self.cant_usuarios_inscritos-=1

    def validar_cupo_disponible(self)->bool:
        if(self.cant_usuarios_inscritos < self.cupo_maximo):
            return True
        else:
            return False
        
    def mostrar_clase_grupal(self)->None:
        print("\n=== Clase grupal ===")
        print("El id de la clase es", self.id)
        print("El nombre de la clase es", self.nombre)
        print("Descripción de la clase", self.descripcion)
        print("La fecha de la clase es", self.fecha)
        print("La hora de clase", self.hora)
        print("La duración de la clase es", self.duracion)
        print("El cupo máximo para esta clase es de", self.cupo_maximo)
        print("La cantidad de usuarios inscritos para esta clase es de ", self.cant_usuarios_inscritos, "usuarios")
        
    # R12: Consultar la lista de usuarios inscritos en una clase grupal
    def mostrar_inscritos(self) -> None:
        print("\n=== Usuarios inscritos ===")
        if len(self.usuarios_inscritos) == 0:
            print("No hay usuarios inscritos.")
        else:
            for i in range(len(self.usuarios_inscritos)):
                print(f"\nUsuario #{i+1}")
                print(self.usuarios_inscritos[i].nombre)






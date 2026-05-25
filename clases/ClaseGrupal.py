import numpy as np
class Clase_Grupal:
    id:int
    nombre:str
    descripcion: str
    fecha: str
    hora: str
    duracion: int
    cupo_maximo: int
    cant_usuarios_inscritos: int
    usuarios_inscritos = np.ndarray 
    
    def __init__(self,id=0, nombre="N.A.", descripcion="N.A.", fecha="N.A.", hora="N.A.", duracion=0,cupo_maximo=0,cant_usuarios_inscritos=0):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.fecha= fecha
        self.hora= hora
        self.duracion= duracion
        self.cupo_maximo= cupo_maximo
        self.cant_usuarios_inscritos= cant_usuarios_inscritos
        self.usuarios_inscritos = np.empty(0, dtype=object) # arreglo de usuarios inscritos

    def sumar_inscrito(self, usuario) -> None:
        copia = self.usuarios_inscritos.copy()
        nuevo_arreglo = np.empty(len(copia) + 1, dtype=object)
        for i in range(len(copia)):
            nuevo_arreglo[i] = copia[i]
        nuevo_arreglo[len(copia)] = usuario
        self.usuarios_inscritos = nuevo_arreglo
        self.cant_usuarios_inscritos += 1

    def restar_inscrito(self, usuario) -> None:
        copia = self.usuarios_inscritos.copy()
        nuevo_arreglo = np.empty(len(copia) - 1, dtype=object)
        j = 0
        for i in range(len(copia)):
            if copia[i] != usuario:
                nuevo_arreglo[j] = copia[i]
                j += 1
        self.usuarios_inscritos = nuevo_arreglo
        self.cant_usuarios_inscritos -= 1


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






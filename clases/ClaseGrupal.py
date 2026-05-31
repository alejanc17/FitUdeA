# Clase hecha por Manuela (lista)
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
    
    def __init__(self,id=0, nombre="N.A.", descripcion="N.A.", entrenador=None, fecha="N.A.", hora="N.A.", duracion=0,cupo_maximo=0,cant_usuarios_inscritos=0):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.entrenador = entrenador
        self.fecha= fecha
        self.hora= hora
        self.duracion= duracion
        self.cupo_maximo= cupo_maximo
        self.cant_usuarios_inscritos= cant_usuarios_inscritos
        self.usuarios_inscritos = np.empty(0, dtype=object) # arreglo de usuarios inscritos

    #R15: Registrar una una clase grupal 
    def registrar_clase_grupal(self)->None:
        """Este método permite al administrador registrar una nueva clase"""
        self.id=int(input("Ingrese el id de la clase:"))
        self.nombre= input("Ingrese el nombre de la clase grupal:")
        self.descripcion=input("Ingrese una breve descripción de esta clase grupal:")
        self.fecha=input("Ingrese la fecha de la clase grupal en formato dia/mes/año :")
        self.hora=input("Ingrese la hora de la clase grupal en formato HH-MM-SS:")
        self.duracion=int(input("Ingrese la duración de la clase en minutos:"))
        self.cupo_maximo=int(input("Ingrese el cupo máximo que tendrá esta clase grupal :"))
        print("Clase registrada exitosamente.")

    #R16 Modificar una clase grupal
    def modificar_clase_grupal(self)->None:

        """Este método permite al administrador modificar los datos de una clase existente"""
        self.mostrar_clase_grupal()
        
        opcion= 0
        while (opcion!=7):
            print("\n===Seleccione una opción a modificar===")
            opcion=int(input("\n Ingresa una opción \n1.nombre \n2.descripción \n3.fecha \n4.hora \n5.duración \n.6 cupo máximo " \
            "\n7. salir"))
            match opcion:
                case 1:
                    self.nombre=input("Ingresa el nuevo nombre:")
                    print("Nuevo nombre guardado exitosamente.")
                case 2:
                    self.descripcion=input("Ingresa la nueva descripción:")
                    print("Descripción guardada exitosamente.")
                case 3: 
                    self.fecha=input("Ingrese la nueva fecha en el formato dd/mm/aaaa:")
                    print("Fecha guardada exitosamente.")
                case 4:
                    self.hora=input("Ingrese la nueva hora en formato HH-MM-SS: ")
                    print("Hora guardada exitosamente")
                case 5:
                    self.duracion= int(input("Ingrese la duración en minutos"))
                    print("La duración ha sido guardada correctamente.")
                case 6: 
                    self.cupo_maximo=int(input("Ingrese el nuevo cupo máximo:"))
                    print("El cupo máximo ha sido guardado correctamente.")
                case 7:
                    print("Saliendo")


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

        if self.entrenador != None:
            print("Entrenador asignado: ", self.entrenador.nombre)
        else:
            print("Entrenador asignado: Por definir")
            
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






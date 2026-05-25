# Clase hecha por Manuela (lista)
import numpy as np
class Rutina:
    id: int
    nombre: str
    descripcion_general: str
    objetivo_principal: str
    nivel_dificultad: str
    duracion_estimada: int
    estado: str

    def __init__(self, id=0, nombre="N.A.", descripcion_general="N.A.", objetivo_principal="N.A.", 
                 nivel_dificultad="N.A.", duracio_estimada=0, estado="N.A."):
        """
        Método constructor que inicializa los atributos de la rutina.
        PARAM:
            id (int): Identificador único de la rutina.
            nombre (str): Nombre de la rutina.
            descripcion_general (str): Descripción general de la rutina.
            objetivo_principal (str): Objetivo principal de la rutina.
            nivel_dificultad (str): Nivel de dificultad de la rutina.
            duracio_estimada (int): Duración estimada en minutos.
            estado (str): Estado de la rutina (activa/inactiva).
        """
        self.id = id
        self.nombre = nombre
        self.descripcion_general = descripcion_general
        self.objetivo_principal = objetivo_principal
        self.nivel_dificultad = nivel_dificultad
        self.duracion_estimada = duracio_estimada
        self.estado = estado
        self.ejercicios = np.empty(0, dtype=object)
        self.usuarios_asignados = np.empty(0, dtype=object)

    # R13: Crear una rutina de entrenamiento y asignar una rutina de entrenamiento
    def crear_rutina(self) -> None:
        """
        Permite al entrenador registrar una nueva rutina de entrenamiento
        ingresando sus datos y ejercicios.
        """
        self.id = int(input("Ingrese el id de la rutina: "))
        self.nombre = input("Ingrese el nombre de la rutina: ")
        self.descripcion_general = input("Ingrese una descripcion general sobre esta rutina: ")
        self.objetivo_principal = input("Escribe aquí cuál es el objetivo principal de la rutina: ")
        self.nivel_dificultad = input("Ingrese aquí el nivel de dificultad de esta rutina: ")
        self.duracion_estimada = int(input("Ingrese la duración estimada de la rutina: "))
        self.estado = input("Ingrese el estado de la rutina (Activa o Inactiva): ")
        self.agregar_ejercicio()
        print("Rutina creada exitosamente.")

    # R14: Consultar usuarios asignados
    def consultar_usuarios_asignados(self) -> None:
        """
        Muestra en pantalla los usuarios que tienen asignada esta rutina.
        """
        print("\n=== Usuarios asignados ===")
        if len(self.usuarios_asignados) == 0:
            print("No hay usuarios asignados a esta rutina.")
        else:
            for i in range(len(self.usuarios_asignados)):
                print(f"El usuario asignado es {self.usuarios_asignados[i].nombre}")

    def agregar_ejercicio(self) -> None:
        """
        Permite al entrenador agregar los ejercicios que conforman la rutina.
        """
        n = int(input("¿Cuántos ejercicios tiene la rutina? "))
        self.ejercicios = np.empty(n, dtype=object)
        for i in range(n):
            self.ejercicios[i] = input(f"Ingrese el nombre del ejercicio #{i+1}: ")

    def asignar_usuario(self) -> None:
        """
        Permite asignar uno o más usuarios a esta rutina de entrenamiento.
        """
        n = int(input("¿Cuántos usuarios deseas ingresar?: "))
        self.usuarios_asignados = np.empty(n, dtype=object)
        for i in range(n):
            self.usuarios_asignados[i] = input(f"Ingrese el nombre del usuario #{i+1}: ")

    def mostrar_detalle_rutina(self) -> None:
        """
        Muestra en pantalla todos los datos de la rutina incluyendo sus ejercicios.
        """
        print("\n=== Detalle de la rutina ===")
        print("El id de la rutina es", self.id)
        print("El nombre de la rutina es", self.nombre)
        print("Descripción de esta rutina:", self.descripcion_general)
        print("El objetivo principal de esta rutina es", self.objetivo_principal)
        print("La duración estimada de la rutina será de", self.duracion_estimada)
        print("El estado de la rutina es", self.estado)
        if len(self.ejercicios) == 0:
            print("No hay ejercicios que mostrar")
        else:
            for i in range(len(self.ejercicios)):
                print(f"\nEjercicio #{i+1}")
                print(self.ejercicios[i])
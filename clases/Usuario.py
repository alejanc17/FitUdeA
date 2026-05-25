
import numpy as np
class Usuario:
    """
    Clase que representa y gestiona la información de los usuarios del gimnasio FitUdeA.
    """
    id: int
    nombre: str
    tipo_documento: str
    num_documento: int
    fecha_nacimiento: str
    correo: str
    telefono: int
    estrato: int
    contrasena: str
    tipo_usuario: int

    # CONSTANTES
    ADMINISTRADOR=1 
    ENTRENADOR=2
    AFILIADO=3


    def __init__(self, id=0, nombre="N.A.", tipo_documento="N.A.", num_documento="N.A.",
                 fecha_nacimiento="N.A.", correo="N.A.", telefono=0, estrato=0, contrasena="N.A.", tipo_usuario="N.A."):
        """
        Método constructor que inicializa los atributos del objeto Usuario.
        PARAM:
            id (int): Identificador único del usuario.
            nombre (str): Nombre completo del usuario.
            tipo_documento (str): Tipo de documento de identidad (TI, CC, CE).
            num_documento (int): Número del documento de identidad.
            fecha_nacimiento (str): Fecha de nacimiento en formato dia/mes/anno.
            correo (str): Correo electrónico de contacto.
            telefono (int): Número de teléfono de contacto.
            estrato (int): Estrato socioeconómico (1-6).
            tipo_afiliacion (int): Tipo de afiliación (1.estudiante, 2.docente, 3.egresado, 4.particular).
            estado_membresia (int): Estado actual de la membresía (1.activa, 2.inactiva).
            contrasena (str): Contraseña para ingresar al sistema.
            perfil (str): Rol del usuario en el sistema.
        """
        self.id = id
        self.nombre = nombre
        self.tipo_documento = tipo_documento
        self.num_documento = num_documento
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.telefono = telefono
        self.estrato = estrato
        self.contrasena = contrasena
        self.tipo_usuario = tipo_usuario

    def pedir_datos(self) -> None:
        """
        Solicita por teclado la información básica de registro al usuario y la asigna a los atributos.
        """
        self.nombre = input("Ingrese el nombre completo: ")
        self.tipo_documento = input("Ingrese el tipo de documento (TI, CC, CE): ")
        self.num_documento = int(input("Ingrese el numero de documento sin espacios: "))
        self.fecha_nacimiento = input("Ingrese la fecha de nacimiento (dia/mes/anno): ")
        self.correo = input("Ingrese el correo electronico: ")
        self.telefono = int(input("Ingrese el numero de telefono: "))
        self.estrato = int(input("Ingrese su estrato (1-6): "))
        self.contrasena = input("Ingrese la contrasena: ")
        self.tipo_usuario = int(input("Ingrese el tipo de usuario \n1. ADMINISTRADOR \n2.ENTRENADOR \n3.AFILIADO. "))

    def mostrar_datos(self) -> None:
        """
        Muestra en pantalla los datos personales y de registro básicos del usuario.
        """
        print("El nombre completo es:", self.nombre)
        print("El tipo de documento es:", self.tipo_documento)
        print("El numero de documento es:", self.num_documento)
        print("La fecha de nacimiento es:", self.fecha_nacimiento)
        print("El correo electronico es:", self.correo)
        print("El numero de telefono es:", self.telefono)
        print("El estrato es:", self.estrato)
        print("El  es tipo de usuario es:", self.tipo_usuario)

    # R1: Autenticar usuario
    def autenticar(self, correo_ingresado: str, contrasena_ingresada: str) -> bool:
        """
        Método lógico que valida si las credenciales ingresadas coinciden con los datos registrados
        y verifica si la membresía se encuentra activa.
        PARAM:
            correo_ingresado (str): El correo electrónico digitado por el usuario en el inicio de sesión.
            contrasena_ingresada (str): La contraseña digitada por el usuario en el inicio de sesión.
        RETURN: (bool) True si las credenciales son correctas y la membresía es activa, False en caso contrario.
        """

        if self.estado_membresia != 1:
            print("Membresia inactiva. Procede al pago.")
            return False
        if self.correo == correo_ingresado and self.contrasena == contrasena_ingresada:
            print("Bienvenido,", self.nombre)
            return True
        else:
            print("Correo o contraseña incorrectos.")
            return False

    def iniciar_sesion(self) -> bool:
        """
        Solicita las credenciales del usuario por consola e invoca al método de autenticación.
        RETURN: (bool) True si el inicio de sesión fue exitoso, False en caso contrario.
        """

        print("\n=== Inicio de sesion ===")
        correo = input("Correo electronico: ")
        clave = input("Contrasena: ")
        return self.autenticar(correo, clave)

    # R2: Consultar informacion personal y estado de membresia
    def consultar_informacion(self) -> None:
        """
        Muestra en pantalla toda la información personal y traduce los códigos numéricos
        de tipo de afiliación y estado de membresía a texto comprensible para el usuario.
        CONST:
            ESTADOS (dict): Diccionario de mapeo para los estados de la membresía.
            TIPOS (dict): Diccionario de mapeo para los tipos de afiliación.
        RETURN: (None) No retorna ningún valor.
        """

        ESTADOS = {1: "Activa", 2: "Inactiva"}
        TIPOS = {1: "Estudiante", 2: "Docente", 3: "Egresado", 4: "Particular"}

        print("\n=== Mi informacion ===")
        print(f"Nombre          : {self.nombre}")
        print(f"Documento       : {self.tipo_documento} {self.num_documento}")
        print(f"Fecha nacimiento: {self.fecha_nacimiento}")
        print(f"Correo          : {self.correo}")
        print(f"Telefono        : {self.telefono}")
        print(f"Estrato         : {self.estrato}")
        print(f"Tipo afiliacion : {TIPOS.get(self.tipo_afiliacion, 'Desconocido')}")
        print(f"Membresia       : {ESTADOS.get(self.estado_membresia, 'Desconocido')}")
        print(f"Perfil          : {self.perfil}")

    # R3: Actualizar datos de contacto
    def actualizar_contacto(self) -> None:
        """
        Permite al usuario modificar su correo electrónico, teléfono y estrato en el sistema.
        """

        print("\n=== Actualizar datos de contacto ===")
        print(f"Correo actual   : {self.correo}")
        print(f"Telefono actual : {self.telefono}")

        nuevo_correo = input("Nuevo correo (Enter para conservar el actual): ")
        nuevo_telefono = input("Nuevo telefono (Enter para conservar el actual): ")

        if nuevo_correo:
            self.correo = nuevo_correo
            print("Correo actualizado.")
        if nuevo_telefono:
            self.telefono = int(nuevo_telefono)
            print("Telefono actualizado.")

    # R4: Registrar el pago de membresía
    def registrar_pago(self) -> None:
        """
        Registra el pago de la membresía, calculando y aplicando automáticamente los descuentos
        según el tipo de afiliación, el estrato socioeconómico y la edad del usuario.
        CONST:
            valor_base (float): Simula el precio fijo base de la membresía mensual.
        """

        print("\n=== Registrar Pago de Membresía")
        tipo_plan = input("Ingrese el tipo de plan (mensual / anual): ")
        fecha_pago = input("Ingrese la fecha de pago (dia/mes/año): ")
        concepto = input("Ingrese el concepto del pago: ")

        # Valor base de la mensualidad
        valor_base = 100000
        descuento = 0.0

        if (tipo_plan == "anual"):
            valor_total = valor_base * 12
            descuento += valor_total * 0.25
        else:
            valor_total = valor_base

        edad = int(input("Ingrese la edad actual en años: "))

        # Descuento para Docentes (2) o Egresados (3) mayores de 50 años
        if (self.tipo_afiliacion == 2 or self.tipo_afiliacion == 3) and (edad > 50):
            descuento += valor_total * 0.10

        # Descuento para Estudiantes (1) de estrato 1 o 2
        if (self.tipo_afiliacion == 1) and (self.estrato == 1 or self.estrato == 2):
            descuento += valor_total * 0.10

        # Cálculo final y actualización del estado de membresía (1 = Activa)
        valor_final = valor_total - descuento
        self.estado_membresia = 1

        print("\n¡Pago registrado exitosamente!")
        print(f"Valor original: ${valor_total}")
        print(f"Descuentos    : ${descuento}")
        print(f"Total a pagar : ${valor_final}")
        print("Estado actual de su membresía ahora es: Activa")

class Afiliado(Usuario):
    """
    Clase que representa a un usuario afiliado del gimnasio FitUdeA.
    Hereda de Usuario y agrega funcionalidades propias del perfil afiliado.
    """

    tipo_afiliación: int 
    tipo_plan: int 
    fecha_de_inicio: str 
    fecha_de_vencimiento: str 
    estado_de_membresia: str 
    rutinas_asignadas: np.ndarray     
    #CONSTANTES
    ESTUDIANTE= 1
    EGRESADO= 2
    DOCENTE= 3
    PARTICULAR = 4
    MENSUAL= 1
    ANUAL= 2
    ACTIVA= 1
    INACTIVA= 2



    def __init__(self, nombre="N.A.", tipo_documento=0, num_documento=0, fecha_nacimiento="N.A.",
                         correo="N.A.", telefono="N.A.", tipo_afiliacion=0, tipo_plan=0, fecha_de_inicio="N.A.", fecha_de_vencimiento="N.A.",
                 estado_de_membresia=0):
        super().__init__(id, nombre, tipo_documento, num_documento, fecha_nacimiento,
                         correo, telefono,estrato=0,
                         contrasena="N.A.", tipo_usuario=3)

        self.tipo_afiliación= tipo_afiliacion
        self.tipo_plan= tipo_plan
        self.fecha_de_inicio= fecha_de_inicio
        self.fecha_de_vencimiento= fecha_de_vencimiento
        self.estado_de_membresia=estado_de_membresia
    
        self.rutinas_asignadas = []    # arreglo de rutinas asignadas
    # R5: Consultar historial de pagos
    def consultar_historial_pagos(self) -> None:
        """
        Muestra en pantalla el historial de pagos realizados por el afiliado.
        """
        print("\n=== Historial de Pagos ===")
        if len(self.historial_pagos) == 0:
            print("No hay pagos registrados.")
        else:
            for i in range(len(self.historial_pagos)):
                print(f"\nPago #{i + 1}")
                print(self.historial_pagos[i])
    # R6:Consultar las rutinas de entrenamiento asignadas. 
    def consultar_rutinas(self)->None:
        """ Muestra en pantalla las rutinas asignadas para el usuario afiliado """
        print("\n=== Rutinas asignadas ===")
        if len(self.rutinas_asignadas)==0:
            print("No hay rutinas asignadas.")
        else: 
            for i in range(len(self.rutinas_asignadas)):
                print(f"\nRutina #{i+1}")
                print(self.rutinas_asignadas[i])
    # R7: Consultar la programación semanal de clases grupales.
    def consultar_clases_grupales(self,clases)->None:
        print("\n=== Clases grupales ===")
        if len(clases)==0:
            print("No hay clases grupales")
        else:
            for i in range(len(clases)):
                print(f"\nClase grupal #{i+1}")
                clases[i].mostrar_clase_grupal()


class Entrenador(Usuario):
    # Atributo exclusivo del entrenador
    areas_especialidad: str

    def __init__(self, id=0, nombre="N.A.", tipo_documento="N.A.", num_documento=0,
                 fecha_nacimiento="N.A.", correo="N.A.", telefono=0, estrato=0,
                 tipo_afiliacion=0, estado_membresia=0, contrasena="N.A.",
                 areas_especialidad="N.A."):
        super().__init__(id, nombre, tipo_documento, num_documento, fecha_nacimiento,
                         correo, telefono, estrato, tipo_afiliacion, estado_membresia,
                         contrasena, "Entrenador")
        
        self.areas_especialidad = areas_especialidad

    def crear_rutina(self):
        pass

    def consultar_agenda(self):
        pass

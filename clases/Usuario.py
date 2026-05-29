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
    ADMINISTRADOR = 1
    ENTRENADOR = 2
    AFILIADO = 3

    def __init__(self, id=0, nombre="N.A.", tipo_documento="N.A.", num_documento="N.A.",
                 fecha_nacimiento="N.A.", correo="N.A.", telefono=0, estrato=0,
                 contrasena="N.A.", tipo_usuario="N.A."):
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
            contrasena (str): Contraseña para ingresar al sistema.
            tipo_usuario (int): Tipo de usuario (1.Admin, 2.Entrenador, 3.Afiliado).
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
        Solicita por teclado la información básica del usuario.
        """
        self.nombre = input("Ingrese el nombre completo: ")
        self.tipo_documento = input("Ingrese el tipo de documento (TI, CC, CE): ")
        self.num_documento = int(input("Ingrese el numero de documento sin espacios: "))
        self.fecha_nacimiento = input("Ingrese la fecha de nacimiento (dia/mes/anno): ")
        self.correo = input("Ingrese el correo electronico: ")
        self.telefono = int(input("Ingrese el numero de telefono: "))
        self.estrato = int(input("Ingrese su estrato (1-6): "))
        self.contrasena = input("Ingrese la contrasena: ")
        self.tipo_usuario = int(input("Ingrese el tipo de usuario \n1. ADMINISTRADOR \n2. ENTRENADOR \n3. AFILIADO: "))

    def mostrar_datos(self) -> None:
        """
        Muestra en pantalla los datos básicos del usuario.
        """
        print("El nombre completo es:", self.nombre)
        print("El tipo de documento es:", self.tipo_documento)
        print("El numero de documento es:", self.num_documento)
        print("La fecha de nacimiento es:", self.fecha_nacimiento)
        print("El correo electronico es:", self.correo)
        print("El numero de telefono es:", self.telefono)
        print("El estrato es:", self.estrato)
        print("El tipo de usuario es:", self.tipo_usuario)

    # R1: Autenticar usuario
    def autenticar(self, correo_ingresado: str, contrasena_ingresada: str) -> bool:
        """
        Valida si las credenciales ingresadas coinciden con los datos registrados.
        PARAM:
            correo_ingresado (str): Correo electrónico digitado por el usuario.
            contrasena_ingresada (str): Contraseña digitada por el usuario.
        RETURN: (bool) True si las credenciales son correctas, False en caso contrario.
        """
        if self.correo == correo_ingresado and self.contrasena == contrasena_ingresada:
            print("Bienvenido,", self.nombre)
            return True
        else:
            print("Correo o contraseña incorrectos.")
            return False

    def iniciar_sesion(self) -> bool:
        """
        Solicita las credenciales del usuario e invoca al método de autenticación.
        RETURN: (bool) True si el inicio de sesión fue exitoso, False en caso contrario.
        """
        print("\n=== Inicio de sesion ===")
        correo = input("Correo electronico: ")
        clave = input("Contrasena: ")
        return self.autenticar(correo, clave)

    # R3: Actualizar datos de contacto
    def actualizar_contacto(self) -> None:
        """
        Permite al usuario modificar su correo electrónico y teléfono.
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


class Afiliado(Usuario):
    """
    Clase que representa a un usuario afiliado del gimnasio FitUdeA.
    Hereda de Usuario y agrega funcionalidades propias del perfil afiliado.
    """
    tipo_afiliacion: int
    tipo_plan: int
    fecha_de_inicio: str
    fecha_de_vencimiento: str
    estado_de_membresia: int

    # CONSTANTES
    ESTUDIANTE = 1
    EGRESADO = 2
    DOCENTE = 3
    PARTICULAR = 4
    MENSUAL = 1
    ANUAL = 2
    ACTIVA = 1
    INACTIVA = 2

    def __init__(self, id=0, nombre="N.A.", tipo_documento="N.A.", num_documento=0,
                 fecha_nacimiento="N.A.", correo="N.A.", telefono=0, estrato=0,
                 contrasena="N.A.", tipo_afiliacion=0, tipo_plan=0,
                 fecha_de_inicio="N.A.", fecha_de_vencimiento="N.A.",
                 estado_de_membresia=1):
        """
        Constructor de Afiliado. Llama al constructor de Usuario y agrega atributos propios.
        PARAM:
            estado_de_membresia (int): Por defecto 1 (Activa).
        """
        super().__init__(id, nombre, tipo_documento, num_documento, fecha_nacimiento,
                         correo, telefono, estrato, contrasena, tipo_usuario=3)
        self.tipo_afiliacion = tipo_afiliacion
        self.tipo_plan = tipo_plan
        self.fecha_de_inicio = fecha_de_inicio
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.estado_de_membresia = estado_de_membresia
        self.historial_pagos = np.empty(0, dtype=object)
        self.historial_reservas = np.empty(0, dtype=object)
        self.rutinas_asignadas = np.empty(0, dtype=object)

    def pedir_datos(self) -> None:
        """
        Solicita los datos del afiliado por teclado.
        """
        super().pedir_datos()
        self.tipo_afiliacion = int(input("Tipo de afiliacion (1.Estudiante, 2.Egresado, 3.Docente, 4.Particular): "))
        self.tipo_plan = int(input("Tipo de plan (1.Mensual, 2.Anual): "))
        self.fecha_de_inicio = input("Fecha de inicio del plan (dia/mes/anno): ")
        self.fecha_de_vencimiento = input("Fecha de vencimiento del plan (dia/mes/anno): ")
        self.estado_de_membresia = 1 

    # R2: Consultar informacion personal y estado de membresia
    def consultar_informacion(self) -> None:
        """
        Muestra en pantalla la información personal y el estado de membresía del afiliado.
        """
        ESTADOS = {1: "Activa", 2: "Inactiva"}
        TIPOS = {1: "Estudiante", 2: "Egresado", 3: "Docente", 4: "Particular"}
        PLANES = {1: "Mensual", 2: "Anual"}

        print("\n=== Mi informacion ===")
        print(f"Nombre           : {self.nombre}")
        print(f"Documento        : {self.tipo_documento} {self.num_documento}")
        print(f"Fecha nacimiento : {self.fecha_nacimiento}")
        print(f"Correo           : {self.correo}")
        print(f"Telefono         : {self.telefono}")
        print(f"Estrato          : {self.estrato}")
        print(f"Tipo afiliacion  : {TIPOS.get(self.tipo_afiliacion, 'Desconocido')}")
        print(f"Tipo plan        : {PLANES.get(self.tipo_plan, 'Desconocido')}")
        print(f"Fecha inicio     : {self.fecha_de_inicio}")
        print(f"Fecha vencimiento: {self.fecha_de_vencimiento}")
        print(f"Membresia        : {ESTADOS.get(self.estado_de_membresia, 'Desconocido')}")

    # R4: Registrar el pago de membresía
    def registrar_pago(self) -> None:
        """
        Registra el pago de la membresía aplicando descuentos automáticamente.
        """
        from clases.Pago import Pago

        print("\n=== Registrar Pago de Membresía ===")
        tipo_plan = input("Ingrese el tipo de plan (mensual / anual): ")
        fecha_pago = input("Ingrese la fecha de pago (dia/mes/año): ")
        concepto = input("Ingrese el concepto del pago: ")
        edad = int(input("Ingrese la edad actual en años: "))
        valor_base = 100000.0

        pago = Pago()
        pago.fecha = fecha_pago
        pago.concepto = concepto

        descuento = pago.calcular_descuento(tipo_plan, self.tipo_afiliacion, self.estrato, edad, valor_base)

        if tipo_plan == "anual":
            valor_total = valor_base * 12
        else:
            valor_total = valor_base

        pago.valor_cancelado = valor_total - descuento

        copia = self.historial_pagos.copy()
        nuevo_arreglo = np.empty(len(copia) + 1, dtype=object)
        for i in range(len(copia)):
            nuevo_arreglo[i] = copia[i]
        nuevo_arreglo[len(copia)] = pago
        self.historial_pagos = nuevo_arreglo

        self.estado_de_membresia = 1

        print("\n¡Pago registrado exitosamente!")
        print(f"Valor original : ${valor_total}")
        print(f"Descuentos     : ${descuento}")
        print(f"Total a pagar  : ${pago.valor_cancelado}")
        print("Estado de membresía: Activa")

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
                self.historial_pagos[i].mostrar_pago()

    # R6: Consultar las rutinas de entrenamiento asignadas.
    def consultar_rutinas(self) -> None:
        """
        Muestra en pantalla las rutinas asignadas para el usuario afiliado.
        """
        print("\n=== Rutinas asignadas ===")
        if len(self.rutinas_asignadas) == 0:
            print("No hay rutinas asignadas.")
        else:
            for i in range(len(self.rutinas_asignadas)):
                print(f"\nRutina #{i+1}")
                self.rutinas_asignadas[i].mostrar_detalle_rutina()

    # R7: Consultar la programación semanal de clases grupales.
    def consultar_clases_grupales(self, clases) -> None:
        """
        Muestra en pantalla las clases grupales disponibles.
        PARAM:
            clases: arreglo de objetos ClaseGrupal.
        """
        print("\n=== Clases grupales ===")
        if len(clases) == 0:
            print("No hay clases grupales disponibles.")
        else:
            for i in range(len(clases)):
                print(f"\nClase grupal #{i+1}")
                clases[i].mostrar_clase_grupal()


class Entrenador(Usuario):
    """
    Clase que representa a un entrenador del gimnasio FitUdeA.
    Hereda de Usuario y agrega funcionalidades propias del perfil entrenador.
    """
    areas_especialidad: str

    def __init__(self, id=0, nombre="N.A.", tipo_documento="N.A.", num_documento=0,
                 fecha_nacimiento="N.A.", correo="N.A.", telefono=0, estrato=0,
                 contrasena="N.A.", areas_especialidad="N.A."):
        """
        Constructor de Entrenador. Llama al constructor de Usuario y agrega atributos propios.
        """
        super().__init__(id, nombre, tipo_documento, num_documento, fecha_nacimiento,
                         correo, telefono, estrato, contrasena, tipo_usuario=2)
        self.areas_especialidad = areas_especialidad

    def crear_rutina(self):
        pass

    def consultar_agenda(self):
        pass
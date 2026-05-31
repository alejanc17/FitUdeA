import numpy as np
import os
from clases.Usuario import Usuario, Afiliado, Entrenador
from clases.ClaseGrupal import Clase_Grupal
from clases.Rutina import Rutina
from clases.Pago import Pago
from clases.Reserva import Reserva

class App():
    """
    Clase orquestadora principal que gestiona el menú iterativo de la aplicación FitUdeA.
    """

    # Constantes
    MAX_USUARIOS = 50
    MAX_CLASES = 50
    MAX_RUTINAS = 50
    MAX_PAGOS = 50
    MAX_RESERVAS = 50

    ARCHIVO_USUARIOS = "datos_usuarios.npy"
    ARCHIVO_CLASES = "datos_clases.npy"
    ARCHIVO_RUTINAS = "datos_rutinas.npy"
    ARCHIVO_PAGOS = "datos_pagos.npy"
    ARCHIVO_RESERVAS = "datos_reservas.npy"
    ARCHIVO_VALORES = "datos_valores.npy"

    def __init__(self):
        """
        Constructor que carga los datos almacenados en los archivos al iniciar la app.
        """
        self.usuarios, self.cont_usuarios = self.cargar_datos(self.ARCHIVO_USUARIOS, self.MAX_USUARIOS)
        self.clases, self.cont_clases = self.cargar_datos(self.ARCHIVO_CLASES, self.MAX_CLASES)
        self.rutinas, self.cont_rutinas = self.cargar_datos(self.ARCHIVO_RUTINAS, self.MAX_RUTINAS)
        self.pagos, self.cont_pagos = self.cargar_datos(self.ARCHIVO_PAGOS, self.MAX_PAGOS)
        self.reservas, self.cont_reservas = self.cargar_datos(self.ARCHIVO_RESERVAS, self.MAX_RESERVAS)
        self.valores, self.cont_valores = self.cargar_datos(self.ARCHIVO_VALORES, 4)
        self.usuario_autenticado = None

    def cargar_datos(self, archivo: str, num_max_datos: int) -> tuple:
        """
        Carga los datos de un archivo en un arreglo.
        PARAM:
            archivo (str): Ruta del archivo a cargar.
            num_max_datos (int): Tamaño máximo del arreglo.
        RETURN: tuple con el arreglo y el contador de datos.
        """
        try:
            arreglo_de_datos = np.load(archivo, allow_pickle=True)
            i = 0
            while arreglo_de_datos[i] != None:
                i += 1
            return arreglo_de_datos, i
        except (FileNotFoundError, EOFError):
            print(f"No se pudo cargar el archivo {archivo}. Se creó un arreglo vacío.")
            arreglo_de_datos = np.full((num_max_datos), fill_value=None, dtype=object)
            return arreglo_de_datos, 0

    def guardar_datos(self, arreglo_de_datos: np.ndarray, archivo: str) -> bool:
        """
        Guarda los datos de un arreglo en un archivo.
        PARAM:
            arreglo_de_datos (np.ndarray): Arreglo con los datos a guardar.
            archivo (str): Ruta del archivo donde se guardarán los datos.
        RETURN: True si se guardó correctamente, False si no.
        """
        try:
            np.save(archivo, arreglo_de_datos)
            return True
        except (FileNotFoundError, EOFError):
            print(f"Error: no se pudieron guardar los datos en {archivo}.")
            return False

    def registrar_usuario(self) -> None:
        """
        Registra un nuevo usuario en el sistema garantizando la jerarquía de roles.
        """
        print("\n=== Registro de Usuario ===")

        # Lógica de asignación automática de roles
        if self.cont_usuarios == 0:
            print("¡Atención! NO hay usuarios registrados. Este primer usuario usuario será ADMINISTRADOR por defecto.")
            tipo = Usuario.ADMINISTRADOR

        elif self.usuario_autenticado != None and self.usuario_autenticado.tipo_usuario == Usuario.ADMINISTRADOR:
            tipo = int(input("¿Qué tipo de cuenta deseas crear? \n1. Administrador \n2. Entrenador: "))
        
        else:
            print("Registrando cuenta de AFILIADO por defecto...")
            tipo = Usuario.AFILIADO

        # Instanciación de la clase correcta
        if tipo == Usuario.AFILIADO:
            usu = Afiliado()
        elif tipo == Usuario.ENTRENADOR:
            usu = Entrenador()
        else:
            usu = Usuario()

        usu.pedir_datos()
        usu.tipo_usuario = tipo
        
        self.usuarios[self.cont_usuarios] = usu
        self.cont_usuarios += 1

        if self.guardar_datos(self.usuarios, self.ARCHIVO_USUARIOS):
            print("Usuario registrado exitosamente.")
        else:
            print("Error al guardar el usuario.")

    def autenticar_usuario(self) -> bool:
        """
        Autentica un usuario verificando su número de documento y contraseña.
        RETURN: True si se autenticó correctamente, False si no.
        """
        print("\n=== Autenticación ===")
        num_doc = int(input("Ingrese el número de documento del usuario: "))
        pas = input("Ingrese la contraseña del usuario: ")

        for i in range(self.cont_usuarios):
            if (self.usuarios[i].num_documento == num_doc):

                if (self.usuarios[i].contrasena == pas):
                    # Corregido: usuarios (en plural)
                    self.usuario_autenticado = self.usuarios[i] 
                    print(f"Bienvenido, {self.usuarios[i].nombre}!")
                    return True
                else:
                    input("La contraseña ingresada no coincide. Presione enter para continuar")
                    return False
        
        input(f"El usuario con documento {num_doc} no está registrado. Presione enter para continuar")
        return False
    
    def registrar_reserva(self, reserva) -> None:
        reserva.registrar_reserva()
        self.reservas[self.cont_reservas] = reserva
        self.cont_reservas += 1
        self.guardar_datos(self.reservas, self.ARCHIVO_RESERVAS)

    def registrar_rutina(self, rutina) -> None:
        rutina.crear_rutina()
        self.rutinas[self.cont_rutinas] = rutina
        self.cont_rutinas += 1
        self.guardar_datos(self.rutinas, self.ARCHIVO_RUTINAS)
    def registrar_clase(self, clase) -> None:
        clase.registrar_clase_grupal()
        self.clases[self.cont_clases] = clase
        self.cont_clases += 1
        self.guardar_datos(self.clases, self.ARCHIVO_CLASES)

    def menu_afiliado(self, afiliado: Afiliado) -> None:
        """
        Muestra el menú del afiliado y gestiona sus opciones.
        PARAM:
            afiliado (Afiliado): objeto del afiliado autenticado.
        """
        reserva = Reserva()
        opcion = 0

        while opcion != 10:
            print("\n" + "="*30)
            print("MENÚ AFILIADO - FITUDEA")
            print("="*30)
            print("\n1. Consultar información personal")
            print("\n2. Actualizar datos de contacto")
            print("\n3. Registrar pago de membresía")
            print("\n4. Consultar historial de pagos")
            print("\n5. Consultar rutinas asignadas")
            print("\n6. Consultar clases grupales")
            print("\n7. Reservar una clase grupal")
            print("\n8. Cancelar una reserva")
            print("\n9. Consultar historial de reservas")
            print("\n10. Cerrar sesión")

            opcion = int(input("\nElije una opción: "))

            match opcion:
                case 1:
                    afiliado.consultar_informacion()
                case 2:
                    afiliado.actualizar_contacto()
                    self.guardar_datos(self.usuarios, self.ARCHIVO_USUARIOS)
                case 3:
                    afiliado.registrar_pago()
                    self.guardar_datos(self.usuarios, self.ARCHIVO_USUARIOS)
                case 4:
                    afiliado.consultar_historial_pagos()
                case 5:
                    afiliado.consultar_rutinas()
                case 6:
                    afiliado.consultar_clases_grupales(self.clases[:self.cont_clases])
                case 7:
                    reserva.registrar_reserva()
                    
                case 8:
                    reserva.cambiar_estado_cancelada()
                case 9:
                    reserva.mostrar_reserva()
                case 10:
                    self.usuario_autenticado = None
                    print("\nCerrando sesión...")
                case _:
                    print("\nOpción no válida.")

    def menu_entrenador(self, entrenador: Entrenador) -> None:
        """
        Muestra el menú del entrenador y gestiona sus opciones.
        PARAM:
            entrenador (Entrenador): objeto del entrenador autenticado.
        """
        rutina = Rutina()
        clase = Clase_Grupal()
        opcion = 0

        while opcion != 5:
            print("\n" + "="*30)
            print("MENÚ ENTRENADOR - FITUDEA")
            print("="*30)
            print("\n1. Consultar agenda semanal")
            print("\n2. Consultar usuarios inscritos en una clase")
            print("\n3. Crear rutina de entrenamiento")
            print("\n4. Consultar usuarios asignados a una rutina")
            print("\n5. Cerrar sesión")

            opcion = int(input("\nElije una opción: "))

            match opcion:
                case 1:
                    pass
                case 2:
                    clase.mostrar_inscritos()
                case 3:
                    rutina.crear_rutina()
                case 4:
                    rutina.consultar_usuarios_asignados()
                case 5:
                    self.usuario_autenticado = None
                    print("\nCerrando sesión...")
                case _:
                    print("\nOpción no válida.")

    def menu_administrador(self, admin: Usuario) -> None:
        """
        Muestra el menú del administrador y gestiona sus opciones.
        PARAM:
            admin (Usuario): objeto del administrador autenticado.
        """
        clase = Clase_Grupal()
        pago = Pago()
        opcion = 0

        while opcion != 7:
            print("\n" + "="*30)
            print("MENÚ ADMINISTRADOR - FITUDEA")
            print("="*30)
            print("\n1. Registrar nueva clase grupal")
            print("\n2. Modificar información de una clase grupal")
            print("\n3. Actualizar estado de membresía")
            print("\n4. Actualizar valor de afiliación")
            print("\n5. Generar reportes estadísticos")
            print("\n6. Crear cuenta entrenador/administrador")
            print("\n7. Cerrar sesión")

            opcion = int(input("\nElije una opción: "))

            match opcion:
                case 1:
                    clase.registrar_clase_grupal()
                case 2:
                    clase.modificar_clase_grupal()
                    self.guardar_datos(self.clases, self.ARCHIVO_CLASES)
                case 3:
                    self.actualizar_membresia()
                case 4:
                    pago.actualizar_valor_afiliacion()
                    self.guardar_datos(pago.valores_afiliacion, self.ARCHIVO_VALORES)
                case 5:
                    pass
                case 6:
                    self.registrar_usuario()
                case 7:
                    self.usuario_autenticado = None
                    print("\nCerrando sesión...")
                case _:
                    print("\nOpción no válida.")

    def principal(self) -> None:
        """
        Método principal que gestiona el menú de inicio de la aplicación.
        """
        opcion = 0
        while opcion != 3:
            print("\n" + "="*30)
            print("FITUDEA - MENÚ PRINCIPAL")
            print("="*30)
            print("\n1. Registrarse")
            print("\n2. Autenticarse")
            print("\n3. Salir")

            opcion = int(input("\nElije una opción: "))

            match opcion:
                case 1:
                    self.registrar_usuario()
                case 2:
                    # Si la autenticación retorna True, evaluamos la sesión
                    if self.autenticar_usuario():
                        if self.usuario_autenticado.tipo_usuario == Usuario.AFILIADO:
                            self.menu_afiliado(self.usuario_autenticado)

                        elif self.usuario_autenticado.tipo_usuario == Usuario.ENTRENADOR:
                            self.menu_entrenador(self.usuario_autenticado)
                        
                        elif self.usuario_autenticado.tipo_usuario == Usuario.ADMINISTRADOR:
                            self.menu_administrador(self.usuario_autenticado)

                case 3:
                    print("\nHasta luego!")
                case _:
                    print("\nOpción no válida.")

    def actualizar_membresia(self) -> None:
        """
        R17: Permite al administrador buscar un afiliado por documento
        y modificar su estado de membresía o fecha de vencimiento.
        """

        print("\n=== Actualizar Membresía ===")
        doc_buscar = int(input("Ingrese el número de documento del afiliado: "))
        afiliado_encontrado = None

        for i in range(self.cont_usuarios):
            if self.usuarios[i].num_documento == doc_buscar and self.usuarios[i].tipo_usuario == Usuario.AFILIADO:
                afiliado_encontrado = self.usuarios[i]
                break
        
        if afiliado_encontrado != None:
            while True:
                nuevo_estado = input("Ingrese el nuevo estado (1. Activa / 2. Inactiva / 3. Vencida) o presione Enter para omitir: ")

                if nuevo_estado == "":
                    break
                elif nuevo_estado == "1" or nuevo_estado == "2" or nuevo_estado == "3":
                    afiliado_encontrado.estado_de_membresia = int(nuevo_estado)
                else:
                    print("¡Error! Opción no válida. Desbe ingresar 1, 2 o 3. \n")
            
            nueva_fecha = input("INgrese la nueva fecha de vencimiento (día/mes/año) o presione ENTER para omitir: ")
            if nueva_fecha != "":
                afiliado_encontrado.fecha_de_vencimiento = nueva_fecha
            
            self.guardar_datos(self.usuarios, self.ARCHIVO_USUARIOS)
            print("\nMembresía actualizada exitosamente.")

if __name__ == "__main__":
    mi_app = App()
    mi_app.principal()
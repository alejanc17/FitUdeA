import numpy as np
import os
from clases.Usuario import Usuario, Afiliado, Entrenador
from clases.ClaseGrupal import Clase_Grupal
from clases.Rutina import Rutina
from clases.Pago import Pago
from clases.Reserva import Reserva

class App():
    """
    Clase orquestadora principal que gestiona el menú iterativo de la aplicación.
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

    def __init__(self):
        self.usuarios, self.cont_usuarios = self.cargar_datos(self.ARCHIVO_USUARIOS, self.MAX_USUARIOS)
        self.clases, self.cont_clases = self.cargar_datos(self.ARCHIVO_CLASES, self.MAX_CLASES)
        self.rutinas, self.cont_rutinas = self.cargar_datos(self.ARCHIVO_RUTINAS, self.MAX_RUTINAS)
        self.pagos, self.cont_pagos = self.cargar_datos(self.ARCHIVO_PAGOS, self.MAX_PAGOS)
        self.reservas, self.cont_reservas = self.cargar_datos(self.ARCHIVO_RESERVAS, self.MAX_RESERVAS)

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
            while (arreglo_de_datos[i] != None):
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

    def principal(self) -> None:
        """
        Método que controla el ciclo de repetición del menú principal.
        """
        afiliado = Afiliado()
        entrenador = Entrenador()
        clase = Clase_Grupal()
        rutina = Rutina()
        pago = Pago()
        reserva = Reserva()

        opcion = 0

        while (opcion != 21):
            print("\n" + "="*30)
            print("MENÚ DE USUARIO - FITUDEA")
            print("="*30)
            print("\n1. Pedir datos")
            print("\n2. Iniciar sesión")
            print("\n3. Consultar información personal")
            print("\n4. Actualizar datos de contacto")
            print("\n5. Registrar pago de membresía")
            print("\n6. Consultar historial de pagos")
            print("\n7. Consultar las rutinas de entrenamiento asignadas.")
            print("\n8. Consultar la programación semanal de clases grupales.")
            print("\n9. Reservar un cupo en una clase grupal.")
            print("\n10. Cancelar una reserva de clase grupal.")
            print("\n11. Consultar el historial de reservas.")
            print("\n12. Consultar agenda semanal de clases asignadas.")
            print("\n13. Consultar la lista de usuarios inscritos en una clase grupal.")
            print("\n14. Crear una rutina de entrenamiento.")
            print("\n15. Consultar usuarios asignados a una rutina.")
            print("\n16. Registrar una nueva clase grupal.")
            print("\n17. Modificar la información de una clase grupal.")
            print("\n18. Actualizar el estado o vigencia de un plan de membresía.")
            print("\n19. Actualizar el valor mensual de los tipos de afiliación.")
            print("\n20. Generar reportes estadísticos del gimnasio.")
            print("\n21. Salir")

            opcion = int(input("\nElije una opción: "))

            match (opcion):
                case 1:
                    afiliado.pedir_datos()
                    self.usuarios[self.cont_usuarios] = afiliado
                    self.cont_usuarios += 1
                    self.guardar_datos(self.usuarios, self.ARCHIVO_USUARIOS)
                case 2:
                    afiliado.iniciar_sesion()
                case 3:
                    afiliado.consultar_informacion()
                case 4:
                    afiliado.actualizar_contacto()
                case 5:
                    afiliado.registrar_pago()
                case 6:
                    afiliado.consultar_historial_pagos()
                case 7:
                    afiliado.consultar_rutinas()
                case 8:
                    afiliado.consultar_clases_grupales(self.clases[:self.cont_clases])
                case 9:
                    reserva.registrar_reserva()
                    self.reservas[self.cont_reservas] = reserva
                    self.cont_reservas += 1
                    self.guardar_datos(self.reservas, self.ARCHIVO_RESERVAS)
                case 10:
                    reserva.cambiar_estado_cancelada()
                case 11:
                    reserva.mostrar_reserva()
                case 12:
                    pass
                case 13:
                    clase.mostrar_inscritos()
                case 14:
                    rutina.crear_rutina()
                    self.rutinas[self.cont_rutinas] = rutina
                    self.cont_rutinas += 1
                    self.guardar_datos(self.rutinas, self.ARCHIVO_RUTINAS)
                case 15:
                    rutina.consultar_usuarios_asignados()
                case 16:
                    clase.registrar_clase_grupal()
                    self.clases[self.cont_clases] = clase
                    self.cont_clases += 1
                    self.guardar_datos(self.clases, self.ARCHIVO_CLASES)
                case 17:
                    clase.modificar_clase_grupal()
                    self.guardar_datos(self.clases, self.ARCHIVO_CLASES)
                case 18:
                    pass
                case 19:
                    pago.actualizar_valor_afiliacion()
                case 20:
                    pass
                case 21:
                    print("\nSaliendo del sistema. ¡Gracias por usar FitUdeA!")
                case _:
                    print("\nOpción no válida.")

if __name__ == "__main__":
    mi_app = App()
    mi_app.principal()
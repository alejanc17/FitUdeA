from clases.Usuario import Usuario
class App():
    """
    Clase orquestadora principal que gestiona el menú iterativo de la aplicación.
    """
    def principal(self) -> None:
        """
        Método que inicializa los objetos, controla el ciclo de repetición del menú principal
        de usuario.
        """

        usu = Usuario()

        usu.pedir_datos()

        opcion = 0

        while (opcion != 6):
            print("\n" + "="*30)
            print("MENÚ DE USUARIO - FITUDEA")
            print("="*30)
            print("1. Iniciar sesión")
            print("2. Consultar información personal")
            print("3. Actualizar datos de contacto")
            print("4. Registrar pago de membresía")
            print("5. Consultar historial de pagos")
            print("6. Salir")

            opcion = int(input("\nELige una opción: "))

            match (opcion):
                case 1:
                    usu.iniciar_sesion()
                case 2:
                    usu.consultar_informacion()
                case 3:
                    usu.actualizar_contacto()
                case 4:
                    usu.registrar_pago()
                case 5:
                    print("\nEn construcción. Opción correspondiente al quinto requerimiento")
                case 6:
                    print("\nSaliendo del sistema. ¡Gracias por usar FitUdeA!")
                case _:
                    print("\nOpcion no valida. Por favor, elige una opcion del 1 al 6.")

if __name__ == "__main__":
    mi_app = App()
    mi_app.principal()
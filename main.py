from clases.Usuario import Usuario
from clases.Usuario import Usuario, Afiliado, Entrenador
from clases.ClaseGrupal import Clase_Grupal
from clases.Rutina import Rutina
from clases.Pago import Pago
from clases.Reserva import Reserva
class App():
    """
    Clase orquestadora principal que gestiona el menú iterativo de la aplicación.
    """
    

    def principal(self) -> None:
        """
        Método que inicializa los objetos, controla el ciclo de repetición del menú principal
        de usuario.
        """
        clase = Clase_Grupal()
        rutina = Rutina()
        pago = Pago()
        reserva = Reserva()
        usu = Usuario()
        afiliado= Afiliado()
        entrenador= Entrenador()

        usu.pedir_datos()

        opcion = 0

        while (opcion != 20):
            print("\n" + "="*30)
            print("MENÚ DE USUARIO - FITUDEA")
            print("="*30)
            print("\n1. Iniciar sesión")
            print("\n2. Consultar información personal")
            print("\n3. Actualizar datos de contacto")
            print("\n4. Registrar pago de membresía")
            print("\n5. Consultar historial de pagos")
            print("\n6. Consultar las rutinas de entrenamiento asignadas.")
            print("\n7. Consultar la programación semanal de clases grupales.")
            print("\n8. Reservar un cupo en una clase grupal.")
            print("\n9. Cancelar una reserva de clase grupal.")
            print("\n10.Consultar el historial de reservas.")
            print("\n11.Consultar agenda semanal de clases asignadas")
            print("\n12.Consultar la lista de usuarios inscritos en una clase grupal.")
            print("\n13.Crear una rutina de entrenamiento y asignar una rutina de entrenamiento")
            print("\n14.Consultar la información básica y de progreso de los usuarios a su cargo.")
            print("\n15.Registrar una nueva clase grupal.")
            print("\n16.Modificar la información de una clase grupal.")
            print("\n17.Actualizar el estado o vigencia de un plan de membresía.")
            print("\n18.Actualizar el valor mensual de los tipos de afiliación.")
            print("\n19.Generar reportes estadísticos del gimnasio")
            print("\n20. Salir")

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
                    afiliado.consultar_historial_pagos()
                case 6:
                    afiliado.consultar_rutinas()
                case 7:
                    afiliado.consultar_clases_grupales()
                case 8:
                    reserva.registrar_reserva()
                case 9:
                    reserva.cambiar_estado_cancelada()
                case 10:
                    reserva.mostrar_reserva()
                case 11:
                    pass
                case 12:
                    clase.mostrar_inscritos()
                case 13:
                    rutina.crear_rutina()
                case 14:
                    rutina.consultar_usuarios_asignados()
                case 15:
                    clase.registrar_clase_grupal()
                case 16: 
                    clase.modificar_clase_grupal()
                case 17:
                    pass
                case 18:
                    pago.actualizar_valor_afiliacion()
                case 19:
                    pass
                case 20:
                    print("\nSaliendo del sistema. ¡Gracias por usar FitUdeA!")
                case _:
                    print("\nOpcion no valida. Por favor, elige una opcion del 1 al 6.")

if __name__ == "__main__":
    mi_app = App()
    mi_app.principal()
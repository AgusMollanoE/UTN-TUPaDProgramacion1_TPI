import os
import funciones

# Funciones para uso del sistema. Limpiar y pausar la terminal.
def limpiar_pantalla():
    os.system("cls")
    
def pausar():
    os.system("pause")
    
def mostrarLogo():
    # funcion para mostrar el logo del sistema
    # se utiliza un logo en ASCII para mostrar el nombre del sistema de control de inventario
    # fuente ASCII: https://coddy.tech/tools/es/ascii-art-generator
    print("------------------------------------------------------")
    print("|                                                    |")
    print("|   █████  ███   ███  █        ████   ███  █   █     |")
    print("|     █   █   █ █   █ █        █   █ █   █  █ █      |")
    print("|     █   █   █ █   █ █        ████  █   █   █       |")
    print("|     █   █   █ █   █ █        █   █ █   █  █ █      |")
    print("|     █    ███   ███  █████    ████   ███  █   █     |")
    print("|                                                    |")
    print("------------------------------------------------------")
    print("|   SISTEMA DE CONTROL DE INVENTARIO - FERRETERÍA    |")

def menu_principal(inventario):    
## Menú principal del sistema
    while True:
        mostrarLogo()
        print("------------------------------------------------------")
        print("|                  MENÚ DEL SISTEMA                  |")
        print("------------------------------------------------------")
        print("| 1. Carga de herramientas con existencias iniciales |")
        print("| 2. Visualización de inventario                     |")
        print("| 3. Consulta de stock                               |")
        print("| 4. Reporte de agotados                             |")
        print("| 5. Alta de nuevo producto                          |")
        print("| 6. Actualización de stock (venta / ingreso)        |")
        print("| 7. Salir                                           |")
        print("------------------------------------------------------")
        
        try:
            # Validación exigida: int() dentro de try/except
            opcion = int(input("Seleccione una opción: "))
            limpiar_pantalla()

        
            if opcion == 1:
                mostrarLogo()
                print("------------------------------------------------------")
                print("|                CARGA DE HERRAMIENTA                |")
                print("------------------------------------------------------")
                # FUNCION
                # funcion para cargar herramientas con existencias iniciales
                # recibe como parámetro el inventario
                funciones.carga_herramientas(inventario)
                pausar()
                limpiar_pantalla()
                
            elif opcion == 2:
                mostrarLogo()
                print("------------------------------------------------------")
                print("|            VISUALIZACIÓN DE INVENTARIO             |")
                print("------------------------------------------------------")
                # FUNCION
                # funcion para visualizar el inventario
                # recibe como parámetro el inventario
                funciones.visualizacion_inventario(inventario)
                pausar()
                limpiar_pantalla()

            elif opcion == 3:
                mostrarLogo()
                print("------------------------------------------------------")
                print("|                 CONSULTA DE STOCK                  |")
                print("------------------------------------------------------")
                # FUNCIONES 
                # funcion para consultar el stock de herramientas
                # recibe como parámetro el inventario
                funciones.consulta_stock(inventario)
                pausar()
                limpiar_pantalla()

            elif opcion == 4:
                mostrarLogo()
                print("------------------------------------------------------")
                print("|          REPORTE DE HERRAMIENTAS AGOTADAS          |")
                print("------------------------------------------------------")
                # FUNCIONES
                # funcion para generar un reporte de herramientas agotadas
                # recibe como parámetro el inventario
                funciones.reporte_agotados(inventario)
                pausar()
                limpiar_pantalla()
                
            elif opcion == 5:
                mostrarLogo()
                print("------------------------------------------------------")
                print("|               ALTA DE PRODUCTO NUEVO               |")
                print("------------------------------------------------------")
                # FUNCIONES
                # funcion para dar de alta un nuevo producto
                # recibe como parámetro el inventario
                funciones.alta_nuevo_producto(inventario)
                pausar()
                limpiar_pantalla()
                
            elif opcion == 6:
                mostrarLogo()
                print("------------------------------------------------------")
                print("|      ACTUALIZACIÓN DE STOCK (VENTA/ INGRESO)       |")
                print("------------------------------------------------------")
                # FUNCIONES
                # funcion para actualizar el stock de herramientas
                # recibe como parámetro el inventario
                funciones.actualizar_stock(inventario)
                pausar()
                limpiar_pantalla()

            elif opcion == 7:
                mostrarLogo()
                print("------------------------------------------------------")
                print("|                                                    |")
                print("| Saliendo del Sistema...                            |")
                print("| ¡Programa finalizado con éxito!                    |")
                print("|                                                    |")
                print("|             ¡Gracias por lo enseñado!              |")
                print("|                                                    |")
                print("------------------------------------------------------\n")
                break
            
            else:
                # Si el número está fuera del 1 al 7, lanzamos el ValueError obligatorio
                raise ValueError("Opción fuera de rango (debe ser entre 1 y 7).")
                
        except ValueError as e:
                # Captura letras ("abc"), decimales ("3.5") y el raise de rango fuera de 1-7
                print(f"\nError: {e}\n")
                pausar()
                limpiar_pantalla()
                
                
                
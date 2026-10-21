import os
import funciones

# Funciones para uso del sistema. Limpiar y pausar la terminal.
def limpiar_pantalla():
    os.system("cls")
    
def pausar():
    os.system("pause")

def menu_principal(inventario):    

    while True:
        print("-------------------------------------------------")
        print("| SISTEMA DE CONTROL DE INVENTARIO - FERRETERÍA |")
        print("-------------------------------------------------")
        print("|      Seleccione una opción        |")
        print("-------------------------------------")
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
                print("----------------------------------------")
                print("|        CARGA DE HERRAMIENTA          |")
                print("----------------------------------------")
                # FUNCION
                funciones.carga_herramientas(inventario)
                pausar()
                limpiar_pantalla()
                
            elif opcion == 2:
                print("-------------------------------------")
                print("|     VISUALIZACIÓN DE INVENTARIO   |")
                print("-------------------------------------")
                # FUNCION
                funciones.visualizacion_inventario(inventario)
                pausar()
                limpiar_pantalla()

            elif opcion == 3:
                print("-------------------------------------")
                print("|        CONSULTA DE STOCK          |")
                print("-------------------------------------")
                # FUNCIONES 
                
                pausar()
                limpiar_pantalla()

            elif opcion == 4:
                print("-------------------------------------")
                print("|       REPORTE DE AGOTADOS         |")
                print("-------------------------------------")
                # FUNCIONES
                
                pausar()
                limpiar_pantalla()
                
            elif opcion == 5:
                print("-------------------------------------")
                print("|     ALTA DE PRODUCTO NUEVO        |")
                print("-------------------------------------")
                # FUNCIONES
                
                pausar()
                limpiar_pantalla()
                
            elif opcion == 6:
                print("-------------------------------------")
                print("|      ACTUALIZACIÓN DE STOCK       |")
                print("-------------------------------------")
                # FUNCIONES
                
                pausar()
                limpiar_pantalla()

            elif opcion == 7:
                print("-------------------------------------")
                print("| ¡Hasta luego!                     |")
                print("-------------------------------------")
                break
            
            else:
                # Si el número está fuera del 1 al 7, lanzamos el ValueError obligatorio
                raise ValueError("Opción fuera de rango (debe ser entre 1 y 7).")
                #pausar()
                #limpiar_pantalla()
        except ValueError as e:
                # Captura letras ("abc"), decimales ("3.5") y el raise de rango fuera de 1-7
                print(f"Error: {e}\n")
                pausar()
                limpiar_pantalla()
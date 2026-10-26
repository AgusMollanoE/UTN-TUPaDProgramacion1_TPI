import os
# Funciones para uso del sistema. Limpiar y pausar la terminal.
def limpiar_pantalla():
    os.system("cls")
    
def pausar():
    os.system("pause")

# FUNCIONES

# Opcion 1
def carga_herramientas(inventario):
    while True:
        try:
            # 1. Intentamos convertir a entero
            cantidad = int(input("\n¿Cuántas herramientas desea cargar?: "))
            
            # 2. Si se convirtió pero es menor o igual a 0, lanzamos el error a proposito
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a 0.")
            
            # Si todo salio bien, salimos del while con un break
            break
        except ValueError as e:
            print(f"\nError: {e}\n")
            pausar()
            
    for productos in range(cantidad):
        # 1. Validación del Nombre de herramienta
        while True:
            try:
                herramienta = input(f"\nIngrese nombre de herramienta Nº {productos + 1}: ").strip().lower()
                
                if not herramienta:
                    raise ValueError("El nombre no puede estar vacío.")
                    
                for producto in inventario:
                    if producto["herramienta"] == herramienta:
                        raise ValueError("La herramienta ya se encuentra registrada en el inventario.")
                
                # Si paso todas las validaciones sin error, rompemos el while interno
                break
                
            except ValueError as e:
                print(f"ERROR: {e}")
                
        # 2. Validación del stock
        while True:
            try:
                cantidad = int(input(f"Ingrese las unidades para {herramienta}: "))
                
                if cantidad < 0:
                    raise ValueError("La cantidad ingresada no puede ser negativa.")
                    
                break   
            except ValueError as e:
                print(f"\nERROR: {e}\n")
                      
        # 3. Agregamos el diccionario al inventario global
        inventario.append({"herramienta": herramienta, "cantidad": cantidad})
        print(f"\n¡Herramienta {herramienta} cargada con éxito!")
        
# Opcion 2
def visualizacion_inventario(inventario):
    # Verificamos que el inventario no este vacio, si lo esta damos un mensaje dentro del if
    if not inventario:
        print("\nEl inventario esta vacío. No hay herramientas cargadas.\n")
        return
    
    # Si esta lleno el inventario lo mostramos.
    print("|                LISTA DE INVENTARIO                 |")
    print("------------------------------------------------------\n")
    
    for producto in inventario:
        unidad = ""
        
        if producto["cantidad"] == 1 or producto["cantidad"] == 0:
            unidad = "unidad"
        else:
            unidad = "unidades"
        
        print(f"|| Herramienta: {producto["herramienta"]} | Stock: {producto["cantidad"]} {unidad} ||")
    print("\n")

# Opcion 3
def consulta_stock(inventario):
    # Verificamos que el inventario no este vacio
    if not inventario:
        print("\nEl inventario esta vacío. No hay herramientas cargadas.\n")
        return
    
    while True:
        try:
            busqueda = input("\nIngrese Herramienta para consultar stock: ").strip().lower()
            
            # Variable Bandera
            encontrado = False
            if not busqueda:
                raise ValueError("El nombre no puede estar vacio.")
            
            for producto in inventario:
                if producto["herramienta"] == busqueda:
                    unidad = ""
                            
                    if producto["cantidad"] == 1 or producto["cantidad"] == 0:
                        unidad = "unidad"
                    else:
                        unidad = "unidades"
                                
                    print(f"\nHerramienta {producto["herramienta"]} cuenta con {producto["cantidad"]} {unidad} en stock.\n")
                    encontrado = True
                    break
                
             # Si la bandera sigue en False, significa que no se encontro la herramienta en el inventario   
            if not encontrado:
                print(f"\nLa herramienta {busqueda} no se encuentra en el inventario.\n")    
            break
        except ValueError as e:
            print(f"Error. {e}")

# Opcion 4
def reporte_agotados(inventario):
    # verificamos que el inventario no este vacio
    if not inventario:
        print("\nEl inventario esta vacío. No hay herramientas cargadas.\n")
        return
    
    # variable bandera
    hay_agotado = False
    
    print("|                   STOCK AGOTADO                    |")
    print("------------------------------------------------------\n")
    for producto in inventario:
        # Se recorre el invetario hasta encontrar value  0 (stock)
        if producto["cantidad"] == 0:
            print(f"La herramienta {producto["herramienta"]} cuenta con {producto["cantidad"]} unidades en stock.\n") 
            hay_agotado = True
    
    if not hay_agotado:
        print("No hay herramientas agotadas en el inventario.\n")

# Opcion 5
def alta_nuevo_producto(inventario):
    
    print("|               AGREGAR NUEVO PRODUCTO               |")
    print("------------------------------------------------------\n")    
    herramienta = input("Ingrese nombre de la herramienta: ").strip().lower()
            
     #Verificamos que el usuario no ingrese un nombre vacio
    if not herramienta:
        raise ValueError("El nombre no puede estar vacío.")
    
    # Verificamo que la herramienta no se esncuentre en el inventario
    for producto in inventario:
        if producto["herramienta"] == herramienta:
            raise ValueError(f"La herramienta {herramienta} ya se encuentra en el inventario.")
            
    # si no esta duplicado le pedimos al usuario el stock
    stock_new = int(input("Ingrese la cantidad de stock: ").strip())
    
    if stock_new <= 0:
        raise ValueError("El stock no puede ser negativo.")
            
    stock = stock_new
    inventario.append({"herramienta": herramienta, "cantidad": stock})
            
    print(f"\nSe agregó con éxito la herramienta {herramienta} con un stock de: {stock}\n")
                    
          
# Opcion 6
def actualizar_stock(inventario):
    if not inventario:
        # verificamos que el inventario no este vacio
        print("\nEl inventario esta vacío. No hay herramientas cargadas.\n")
        return
    
    print("|                  ACTUALIZAR STOCK                  |")
    print("------------------------------------------------------\n")
    herramienta = input("Ingrese nombre de la herramienta: ").strip().lower()
    
    # Verificamos que el usuario no ingrese un nombre vacio
    if not herramienta:
        raise ValueError("El nombre no puede estar vacío.")
        
    # Buscamos la herramienta con una bandera
    herramienta_encontrada = None
    for producto in inventario:
        # Verificamos si la herramienta ingresada por el usuario se encuentra en el inventario
        if producto["herramienta"] == herramienta:
            herramienta_encontrada = producto
            break
    
    if not herramienta_encontrada:
        print(f"\nLa herramienta {herramienta} no se encuentra en el catálogo.\n")
        return
            
    while True:
        print("\n------------------------------------------------------")
        print("|            ¿Qué acción desea realizar?             |")
        print("------------------------------------------------------")
        print("| 1. VENTA                                           |")
        print("| 2. INGRESOS                                        |")
        print("------------------------------------------------------")
        
        opcion = input("Seleccione una opción (1 o 2): ")
        limpiar_pantalla()
        
        if opcion == "1":
            print("------------------------------------------------------")
            print("|                       VENTAS                       |")
            print("------------------------------------------------------\n")
            unidades = int(input(f"Ingrese la cantidad de unidades vendidas para {herramienta}: ").strip())
            
            # se valida que la cantidad no sea negativa o mayor al stock actual
            if unidades <= 0:
                raise ValueError("La cantidad no puede ser un número negativo o 0.")
            
            # Validamos que la cantidad vendida no sea mayor al stock actual
            if unidades > herramienta_encontrada["cantidad"]:
                raise ValueError(f"Stock insuficiente. Stock actual {herramienta_encontrada["cantidad"]}")
            
            # Actualizamos el stock restando la cantidad vendida
            herramienta_encontrada["cantidad"] -= unidades
            
            print(f"\n¡Venta realizada con éxito!")
            print(f"Stock actual de {herramienta_encontrada['herramienta']} es: {herramienta_encontrada['cantidad']}\n")
            break
        elif opcion == "2":
            print("------------------------------------------------------")
            print("|                      INGRESOS                      |")
            print("------------------------------------------------------\n")
            unidades = int(input(f"Ingrese la cantidad de unidades para {herramienta}: ").strip())
            
            if unidades <= 0:
                raise ValueError("La cantidad no puede ser un número negativo o 0.")
            
            # Actualizamos el stock sumando la cantidad ingresada
            herramienta_encontrada["cantidad"] += unidades
            print(f"\n¡Stock actualizado con éxito!")
            print(f"Stock actual de {herramienta_encontrada['herramienta']} es: {herramienta_encontrada['cantidad']}\n")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción correcta (1 o 2).")
            pausar()
            limpiar_pantalla()
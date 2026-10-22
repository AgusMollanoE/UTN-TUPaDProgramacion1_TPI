import os

# FUNCIONES

# Opcion 1
def carga_herramientas(inventario):
    while True:
        try:
            # 1. Intentamos convertir a entero
            cantidad = int(input("¿Cuántas herramientas desea cargar?: "))
            # 2. Si se convirtió pero es menor o igual a 0, lanzamos el error a proposito
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a 0.")
            # Si todo salio bien, salimos del while con un break
            break
        except ValueError as e:
            print(f"Error: {e}")
            
    for i in range(cantidad):
        # 1. Validación del Nombre de herramienta
        while True:
            try:
                herramienta = input(f"Ingrese Nombre de Herramienta Nº{i + 1}: ").strip().lower()
                
                if not herramienta:
                    raise ValueError("El nombre no puede estar vacío.")
                    
                for item in inventario:
                    if item["nombre"] == herramienta:
                        raise ValueError("La herramienta ya se encuentra registrada en el inventario.")
                
                # Si paso todas las validaciones sin error, rompemos el while interno
                break
                
            except ValueError as e:
                print(f"ERROR: {e}")
         # 2. Validación del stock
        while True:
            try:
                stock = int(input(f"Ingrese stock para {herramienta}: "))
                
                if stock < 0:
                    raise ValueError("El stock no puede ser negativo.")
                    
                break   
            except ValueError as e:
                print(f"ERROR: {e}")       
        # 3. Agregamos el diccionario al inventario global
        inventario.append({"nombre": herramienta, "stock": stock})
        print(f"¡Herramienta {herramienta} cargada con éxito!\n")
        
# Opcion 2
def visualizacion_inventario(inventario):
    # Verificamos que el Inventario no este vacio, si lo esta damos un mensaje dentro del if
    if not inventario:
        print("\n El inventario esta Vacio. No hay Herramientas cargadas.")
        return
    # Si esta lleno el inventario lo mostramos.
    print("|    Lista de Inventario    |")
    for item in inventario:
        print(f"|| Herramienta: {item["nombre"]} | Stock: {item["stock"]} ||")

# Opcion 3
def consulta_stock(inventario):
    # Verificamos que el inventario no este vacio
    if not inventario:
        print("\n El inventario esta Vacio. No hay Herramientas cargadas. ")
        return
    while True:
        try:
            busqueda = input("Ingrese Herramienta para consultar stock: ").strip().lower()
            
            # Variable Bandera
            encontrado = False
            if not busqueda:
                raise ValueError("El nombre no puede estar vacio. ")
            
            for item in inventario:
                if item["nombre"] == busqueda:
                    print(f"Herramienta {item["nombre"]} cuenta con un stock de {item["stock"]}")
                    encontrado = True
                    break
                
            if not encontrado:
                print(f"La Herramienta {busqueda} no se encuentra en el Inventario.")
                
            break
        except ValueError as e:
            print(f"Error. {e}")

# Opcion 4
def reporte_agotados(inventario):
    # verificamos que el inventario no este vacio
    if not inventario:
        print("\n El Inventario esta vacio. No hay Herramientas cargadas. ")
        return
    # variable bandera
    hay_agotado = False
    print("|    STOCK AGOTADO    |")
    for item in inventario:
        # Se recorre el invetario hasta encontrar value  0 (stock)
        if item["stock"] == 0:
            print(f"la Herramienta {item["nombre"]} cuenta con stock: {item["stock"]}.") 
            hay_agotado = True
    
    if not hay_agotado:
        print("No hay Herramientas agotadas en el inventario. ")

# Opcion 5
def alta_nuevo_producto(inventario):

    print("|   AGREGAR NUEVO PRODUCTO   |")    
    
    nombre = input("Ingrese Nombre de la Herramienta: ").strip().lower()
            
            #Verificamos que el usuario no ingrese un nombre vacio
    if not nombre:
        raise ValueError("El nombre no puede estar vacio.")
    # Verificamo que la herramienta no se esncuentre en el inventario
    for item in inventario:
        if item["nombre"] == nombre:
            raise ValueError(f"La herramienta {nombre} ya se encuentra en el inventario.")
            
    # si no esta duplicado le pedimos al usuario el stock
    stock_new = int(input("Ingrese la cantidad de stock: ").strip())
    if stock_new < 0:
        raise ValueError("El stock no puede ser negativo.")
            
    stock = stock_new
    inventario.append({"nombre": nombre, "stock": stock})
            
    print(f"Se agrego con Exito la Herramienta {nombre} con un Stock de: {stock}")
                    
          
# Opcion 6
def actualizar_stock(inventario):
    pass
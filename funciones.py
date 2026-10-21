import os

# FUNCIONES

# Opcion 1
def carga_herramientas(inventario):
    while True:
        try:
            # 1. Intentamos convertir a entero
            cantidad = int(input("¿Cuántas herramientas...?: "))
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
    print("---- Lista de Inventario ----")
    for item in inventario:
        print(f"|| Herramienta: {item["nombre"]} | Stock: {item["stock"]} ||")

# Opcion 3
def consulta_stock(inventario):
    pass

# Opcion 4
def reporte_agotados(inventario):
    pass

# Opcion 5
def alta_nuevo_producto(inventario):
          
# Opcion 6
# def actualizar_stock(inventario):
    pass
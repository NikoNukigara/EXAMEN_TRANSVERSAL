#Menu principal
def menu():
    while True:
        print("***MENU PRINCIPAL***")
        print("1.Stock Marca")
        print("2.Búsqueda por Precio")
        print("3.Actualizar precio")
        print("4.Salir")
        opcion = input("Ingrese opcion deseada: ")
        if opcion == "1":
            marca = input("Ingrese marca: ")
            stock_marca(marca)
        elif opcion == "2":
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
            búsqueda_precio(p_min, p_max)
        elif opcion == "3":
            while True:
                modelo = input("Ingrese el modelo a actualizar: ")
                try:
                    p = int(input("Ingrese el nuevo precio: "))
                except ValueError:
                    print("Debe ingresar un precio válido entero")
                    continue
                resultado = actualizar_precio(modelo, p)
                if resultado:
                    print("Precio actualizado!!")
                else:
                    print("El modelo no existe!!")
                otra = input("¿Desea actualizar otro precio de computador? (si/no): ").strip().lower()
                if otra != "si":
                    break
        elif opcion == "4":
            print("Programa finalizado")
            break
        else:
            print("Ingrese una opcion Valida")

# Funcion para stock por marca           
def stock_marca(marca):
    print(f"Stock disponible para la marca {marca}:")
    encontrado = False
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            cantidad = stock.get(modelo, [0, 0])[1]
            print(f"Modelo: {modelo}, Cantidad: {cantidad}")
            encontrado = True
    if not encontrado:
        print("No hay modelos de la marca a consultar.")

# Funcion para buscar precio
def búsqueda_precio(p_min, p_max):
    lista_precios = []
    for modelo, datos_stock in stock.items():
        precio, cantidad = datos_stock
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            lista_precios.append(f"{marca} {modelo}")
    if not lista_precios:
        print("No hay computadores en ese rango de precios")
        return
    lista_precios.sort()
    print("Los computadores consultados entre esos precios son:")
    for item in lista_precios:
        print(item)

#Funcion actualizar precio
def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False

# Diccionarios base
productos = {
    'N745HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 14, '8GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
    'JJFFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'FGDXHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    'GF75HD': ['Asus', 14, '16GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    'L32FHD': ['Lenovo', 14, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
    '342FHD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JJFFHD': [424990, 1],
    'FGDXFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0],
}

#Ejecuta menu
menu()
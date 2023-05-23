import time


class Cliente:
    def __init__(self, nombre, celular, address):
        self.nombre = nombre
        self.celular = celular
        self.address = address

    def __str__(self):
        return (
            f"Nombre del Cliente: {self.nombre}\n"
            f"Número celular: {self.celular}\n"
            f"Dirección: {self.address}\n"
        )

    def set_Cliente(self):
        print("El cliente ha modificar es:\n" + self.__str__())
        self.nombre = input("Re-ingresa el nombre del cliente: ").rstrip()
        self.celular = input("Re-ingresa su número celular: ").rstrip()
        self.address = input("Re-ingresa su dirección: ").rstrip()
        print("Cambios Realizados!")
        return f"{self.nombre}, {self.celular}, {self.address}\n"


class Pant:
    def __init__(self, marca, modelo, talla, precio, existencias=1):
        self.marca = marca
        self.modelo = modelo
        self.talla = talla
        self.precio = precio
        self.enInventario = existencias

    def __str__(self):
        return (
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Talla: {self.talla}\n"
            f"Precio: ${self.precio}\n"
            f"Existencias en Inventario: {self.enInventario}"
        )

    def set_Pant(self):
        print("El pantalón a modificar es:\n" + self.__str__())
        self.marca = input("Re-ingresa la marca del pantalón: ")
        self.modelo = input("Re-ingresa el modelo del pantalón: ")
        self.talla = input("Re-ingresa la talla del pantalón: ")
        self.precio = input("Re-ingresa el precio unitario del pantalón: ")
        self.enInventario = input("Re-ingresa cuantos pantalones hay disponibles: ")
        print("Cambios Realizados!")
        return f"{self.marca}, {self.modelo}, {self.talla}, {self.precio}, {self.enInventario}\n"

class Proveedor:
    def __init__(self, nombre, marcas, celular, correo):
        self.nombre = nombre
        self.marcas = marcas
        self.celular = celular
        self.correo = correo

    def __str__(self):
        return (
            f"Nombre del Proveedor: {self.nombre}\n"
            f"Marcas que maneja: {self.marcas}\n"
            f"Número de Contacto: {self.celular}\n"
            f"Correo de Contacto: {self.correo}\n"
        )

    def set_Proveedor(self):
        print(f"El proveedor ha modificar es:\n{self.__str__()}")
        self.nombre = input("Re-ingresa el nombre del proveedor: ").rstrip()
        self.marcas = input("Re-ingresa las marcas. Separadas por un ( & ): ").rstrip()
        self.celular = input("Re-Ingresa el número celular: ").rstrip()
        self.correo = input("Re-Ingresa su corre electrónico: ").rstrip()
        print("Cambios realizados con éxito!")
        return f"{self.nombre}, {self.marcas}, {self.celular}, {self.correo}\n"


class Ventas:
    def __init__(self, monto, pantalones):
        self.data = time.strftime("%H:%M:%S | %d-%m-%Y")
        self.monto = monto
        self.pantalones = pantalones

    def __str__(self):
        return (f"{self.data} -> Pantalon(es) Vendidos: {self.pantalones} | Monto de Venta: ${self.monto}\n")

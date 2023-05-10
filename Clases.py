from datetime import datetime


class Cliente:

    def __init__(self, nombre, address, celular):
        self.nombre = nombre
        self.address = address
        self.celular = celular
        self.deuda = 0

    def __str__(self):
        return f'Nombre del Cliente: {self.nombre}\n' \
               f'Número celular: {self.celular}\n' \
               f'Dirección: {self.address}\n' \
               f'Deuda: ${self.deuda}\n'

    def setCliente(self):
        print("El cliente ha modificar es: \n", self.__str__())
        self.nombre = input('Ingresa el nombre del cliente: ').rstrip()
        self.celular = input('Ingresa su número celular: ').rstrip()
        self.address = input('Ingresa su dirección: ').rstrip()
        self.deuda = 0

    def setDeuda(self, agregado):
        self.deuda += agregado


class Pant:

    def __init__(self, marca, modelo, talla, precio):
        self.marca = marca
        self.modelo = modelo
        self.talla = talla
        self.precio = precio
        self.enInventario = 1

    def __str__(self):
        return f'Marca: {self.marca}\n' \
               f'Modelo: {self.modelo}\n' \
               f'Talla: {self.talla}\n' \
               f'Precio: ${self.precio}\n' \
               f'Existencias en Inventario: {self.enInventario}\n'

    def set_enInventario(self, valor: int):
        try:
            self.enInventario += valor
        except:
            print("Debes ingresar un valor numérico.")


class Proveedor:

    def __init__(self, nombre, celular, correo, marcas):
        self.nombre = nombre
        self.marcas = marcas
        self.celular = celular
        self.correo = correo

    def __str__(self):
        return f'Nombre del Proveedor: {self.nombre}\n' \
               f'Marcas que maneja: {self.marcas}\n' \
               f'Número de Contacto: {self.celular}\n' \
               f'Correo de Contacto: {self.correo}\n'

    def setProveedor(self):
        print(f'El proveedor ha modificar es: \n {self.__str__()}')
        self.nombre = input("Re-ingresa el nombre del proveedor: ").rstrip()
        self.marcas = input("Re-ingresa las marcas. Separadas por una (,): ").rstrip()
        self.celular = input("Re-Ingresa el número celular: ").rstrip()
        self.correo = input("Re-Ingresa su corre electrónico: ").rstrip()


class Ventas:

    def __init__(self, monto, pantalones: list[Pant]):
        self.data = datetime.now.strftime('%H:%M:%S | %d-%m-%Y')
        self.monto = monto
        self.pantalones = pantalones

    def __str__(self):
        return f'{self.data}\n' \
               f'Pantalón(es) Vendidos: {self.pantalones}\n' \
               f'Monto de Venta: ${self.monto}'

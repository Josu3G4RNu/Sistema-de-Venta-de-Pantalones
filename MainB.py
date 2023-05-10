from Archivo import Archivo
from Clases import Pant, Ventas, Cliente, Proveedor
from datetime import datetime


class Main:

    def __init__(self):
        self.Inventario = Archivo("Inventario.txt")
        self.RegistroVentas = Archivo("Ventas.txt")
        self.RegistroClientes = Archivo("Clientes.txt")
        self.RegistroProveedores = Archivo("Proveedores.txt")

    @staticmethod
    def __buscar(archivo: Archivo, atributo1, atributo2):
        cosas = archivo.leerInfo()
        for cosa in cosas:
            datos = cosa.rstrip('\n').split(", ")
            if atributo1 == datos[0] and (atributo2 == datos[1] or atributo2 is None):
                return datos
        else:
            return None

    def buscar(self, metodo: int):
        """Realiza una búsqueda en el archivo correspondiente al parámetro método

        :param metodo: 1) Para Cliente,  2) Para Pantalón, 3) Para Proveedor
        """
        if 0 < metodo > 3 or metodo is not int:
            print('Operación inválida!')
        elif metodo == 1:
            datos = self.__buscar(self.RegistroClientes, input("Nombre: ").rstrip(), input("Celular: ").rstrip())
            if datos is not None:
                return Cliente(datos[0], datos[1], datos[2])
            return datos
        elif metodo == 2:
            datos = self.__buscar(self.Inventario, input("Modelo del pantalón: ").rstrip(), input("Talla: ").rstrip())
            if datos is not None:
                return Pant(datos[0], datos[1], datos[2], datos[3])
            return datos
        elif metodo == 3:
            datos = self.__buscar(self.RegistroProveedores, input("Nombre Proveedor: ").rstrip())
            if datos is not None:
                return Proveedor(datos[0], datos[1], datos[2], datos[3])
            return datos

    def registrarCliente(self):
        registrado: Cliente = self.buscar(1)
        if registrado is not None:
            print(f"El cliente ya existe.\n {registrado.__str__()}")
            op = input('Deseas modificar algún dato del mismo? (S/N): ')
            if op == ("S", "s"):
                registrado.setCliente()
            else:
                return
        nombre = input('Nombre del Cliente: ').rstrip()
        celular = input('Número Celular: ').rstrip()
        address = input("Dirección: ").rstrip()
        linea = f'{nombre}, {celular}, {address}\n'
        self.RegistroClientes.añadirInfo(linea)
        print("Cliente Agregado con Éxito.")

    def registrarPant(self):
        registrado: Pant = self.buscar(2)
        if registrado is not None:
            print(f'El pantalón ya existe.\n{registrado.__str__()}')
            op = input('Gustar agregar estos pantalones al inventario? (S/N): ')
            if op == ('S', 's'):
                registrado.set_enInventario(int(input('Ingresa la cantidad a agregar: ').rstrip()))
            else:
                return
        marca = input('Marca: ').rstrip()
        modelo = input('Modelo: ').rstrip()
        talla = input('Talla: ').rstrip()
        precio = input('Precio: $').rstrip()
        linea = f'{marca}, {modelo}, {talla}, {precio}\n'
        self.Inventario.añadirInfo(linea)
        print("Pantalón agregado con éxito.")

    def registrarProveedor(self):
        registrado: Proveedor = self.buscar(3)
        if registrado is not None:
            print(f"El provedor ya existe.\n{registrado.__str__()}")
            op = input("Deseas modificar alguno de sus datos? (S/N): ")
            if op == ('S', 's'):
                registrado.setProveedor()
            else:
                return
        nombre = input("Ingresa el nombre del proveedor: ").rstrip()
        marcas = input("Ingresa las marcas que maneja, separadas por una(,): ").rstrip()
        celular = input("Ingresa el número de contacto: ").rstrip()
        correo = input("Ingresa el correo electrónico de contacto: ").rstrip()
        linea = f'{nombre}, {marcas}, {celular}, {correo}\n'
        self.RegistroProveedores.añadirInfo(linea)
        print("Proveedor Agregado Con Éxito.")

    def registrarVenta(self):
        cantidad = int(input('Ingresa cuántos pantalones se han vendido: ').rstrip())
        pantalonesVendidos = []
        monto = 0
        for pant in range(cantidad):
            pant = self.buscar(2)
            if pant is not None:
                pantalonesVendidos.append(pant)
                monto += pant.precio
                continue
            else:
                print("El pantalón no existe. Verifique los datos")
                self.registrarVenta()
        print('A continuación ha de ingresar el nombre del cliente y su celular para verificar si es deudor.')
        deudor = self.buscar(1)
        if deudor is not None:
            deudor.setDeuda()

        venta = Ventas(datetime.now.strftime('%H:%M:%S | %d-%m-%Y'), monto, pantalonesVendidos)
        venta.modificarInventario()
        self.RegistroVentas.añadirInfo(venta.__str__())

from Archivo import Archivo
from Clases import Pant, Ventas, Cliente, Proveedor


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

    def buscar(self, metodo: int, atributo1, atributo2 = None):
        """Realiza una búsqueda en el archivo correspondiente al parámetro método

        :param metodo: 1) Para Cliente,  2) Para Pantalón, 3) Para Proveedor
        """
        if 0 < metodo > 3 or metodo is not int:
            print('Operación inválida!')
        elif metodo == 1:
            datos = self.__buscar(self.RegistroClientes, atributo1, atributo2)
            if datos is not None:
                return Cliente(datos[0], datos[1], datos[2])
            return datos
        elif metodo == 2:
            datos = self.__buscar(self.Inventario, atributo1, atributo2)
            if datos is not None:
                return Pant(datos[0], datos[1], datos[2], datos[3])
            return datos
        elif metodo == 3:
            datos = self.__buscar(self.RegistroProveedores, atributo1, atributo2)
            if datos is not None:
                return Proveedor(datos[0], datos[1], datos[2], datos[3])
            return datos

    def registrarCliente(self, nombre, celular):
        registrado: Cliente = self.buscar(1, nombre, celular)
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

    def registrarPant(self, modelo, marca):
        registrado: Pant = self.buscar(2, modelo, marca)
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
        enInventario = input('Cantidad de pantalones a inventariar: ')
        linea = f'{marca}, {modelo}, {talla}, {precio}, {enInventario}\n'
        self.Inventario.añadirInfo(linea)
        print("Pantalón agregado con éxito.")

    def registrarProveedor(self, nombre):
        registrado: Proveedor = self.buscar(3, nombre)
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

    def registrarVenta(self, pantalones: list[Pant], cliente: Cliente):
        monto = 0
        for pant in pantalones:
            pant.set_enInventario(-1)
            monto += int(pant.precio)
        venta = Ventas(monto, pantalones)
        self.RegistroVentas.añadirInfo(venta.__str__())
        pago = input("El total a pagar es de: $", monto, "Ingrese la cantidad de pago: $")
        if pago > monto:
            print("El cambio sería: $", pago-monto)
        else:
            print(f'El siguiente monto {monto-pago} será añadida a la deuda del cliente {cliente.nombre}')
            cliente.setDeuda(monto-pago)
        print("Se ha registrado la compra!")

    def __borrar(self, archivo: Archivo, atributo1, atributo2):
        lineas = archivo.leerInfo()
        for linea in lineas:
            datos = linea.rsplit(", ")
            if atributo1 == datos[0] and atributo2 == (datos[1], None):
                lineas.remove(linea)
                break
            else:
                continue
        archivo.sobrescribirInfo(lineas)

    def borrar(self, metodo, atributo1, atributo2):
        if metodo == 1:
            self.__borrar(self.RegistroClientes, atributo1, atributo2)
        elif metodo == 2:
            self.__borrar(self.Inventario, atributo1, atributo2)
        elif metodo == 3:
            self.__borrar(self.RegistroProveedores, atributo1, atributo2) 
        print("El objeto ha sido eliminado del archivo.")   

from Archivo import Archivo
from Clases import *


class Main:
    
    # Proceso de Registro
    def __agregar_cliente(self):
        address = input("Ingresa la dirección del cliente: ").rstrip().upper()
        return address
    
    def __agregar_pant(self):
        marca = input("Ingresa la marca del pantalón: ").rstrip().upper()
        modelo = input("Ingresa el modelo del pantalón: ").rstrip().upper()
        talla = input("Ingresa la talla del pantalón: ").rstrip().upper()
        precio = input("Precio unitario del pantalón: ").rstrip().upper()
        disponibles = input("Cantidad a inventariar: ").rstrip().upper()
        return marca, modelo, talla, precio, disponibles
        
    def __agregar_proveedor(self):
        marcas = input("Ingresa las marcas que manjea separadas por un (&): ").rstrip().upper()
        celular = input("Ingresa el número celular proveedor: ").rstrip().upper()
        correo = input("Ingresa la correo del proveedor: ").rstrip().upper()
        return marcas, celular, correo
    
    def registrar(self, archivo: Archivo, atributo1=None, atributo2=None):
        if archivo.ruta == "Archivos/Registro de Clientes.txt":
            address = self.__agregar_cliente()
            archivo.añadirInfo(f'{atributo1}, {atributo2}, {address}\n')
        elif archivo.ruta == "Archivos/Inventario.txt":
            marca, modelo, talla, precio, disponibles = self.__agregar_pant()
            archivo.añadirInfo(f'{marca}, {modelo}, {talla}, {precio}, {disponibles}\n')
        elif archivo.ruta == "Archivos/Registro de Proveedores.txt":
            marcas, celular, correo = self.__agregar_proveedor()
            archivo.añadirInfo(f'{atributo1}, {marcas}, {celular}, {correo}\n')
            
    # Proceso de Búsqueda
    @staticmethod
    def __buscar(archivo: Archivo, atributo1=None, atributo2=None, talla=None):
        lineas = archivo.leerInfo()
        if talla is not None:
            pantalones = []
            for linea in lineas:
                datos = linea.split(", ")
                if datos[2] == talla:
                    pantalones.append(Pant(datos[0], datos[1], datos[2], datos[3], datos[4]))
            if pantalones:
                return pantalones
            else:
                print("No se encontraron pantalones disponibles en esa talla.")
                return
        for linea in lineas:
            datos = linea.rstrip("\n").split(", ")
            if (atributo1 == datos[0] and (atributo2 == datos[1] or atributo2 is None) and talla is None):
                return datos

    def buscar(self, archivo: Archivo, atributo1=None, atributo2=None, talla=None):
        # Variable que almacena los datos
        datos = None
        if archivo is None:
            print("El archivo no existe")
        # Busqueda de Cliente
        elif archivo.ruta == "Archivos/Registro de Clientes.txt":
            datos = self.__buscar(archivo, atributo1, atributo2)
            if datos is not None:
                return Cliente(datos[0], datos[1], datos[2])
        # Búsqueda de Pantalón
        elif archivo.ruta == "Archivos/Inventario.txt" and talla == None:
            datos = self.__buscar(archivo, atributo1, atributo2)
            if datos is not None:
                return Pant(datos[0], datos[1], datos[2], datos[3], datos[4])
        # Búsqueda de Proveedor
        elif archivo.ruta == "Archivos/Registro de Proveedores.txt":
            datos = self.__buscar(archivo, atributo1, atributo2)
            if datos is not None:
                return Proveedor(datos[0], datos[1], datos[2], datos[3])
        # Búsqueda por talla
        elif talla is not None:
            pants = self.__buscar(archivo, talla=talla)
            print("Pantalones Disponibles en Talla: ", talla)
            for pant in pants:
                print(pant.__str__())
                print("------------------------------------------------------\n")
            return
        return datos
            
    # Proceso de Actualización de registros
    def modificar_registro(self, archivo, atr1, atr2):
        # Variables para permitir la edición
        cadena = ""
        lineas = []
        # Búsqueda del objeto para obtener acceso a la función set.
        objeto = self.buscar(archivo, atr1, atr2)
        # Modificación del cliente
        if archivo.ruta == "Archivos/Registro de Clientes.txt":
            cadena = objeto.set_Cliente()
            lineas = archivo.leerInfo()
        # Modificación de un pantalón
        if archivo.ruta == "Archivos/Inventario.txt":
            cadena = objeto.set_Pant()
            lineas = archivo.leerInfo()
        # Modificación de un proveedor
        if archivo.ruta == "Archivos/Registro de Proveedores.txt":
            cadena = objeto.set_Proveedor()
            lineas = archivo.leerInfo()
        # Archivo sin registros
        if lineas == []:
            print("El archivo no existe!")
            return
        for i, linea in enumerate(lineas):
            datos = linea.split(", ")
            if datos[0] == atr1 and (datos[1] == atr2 or atr2 == None):
                lineas[i] = cadena.upper()
                print(objeto.__str__())
                break
        archivo.sobrescribirInfo(lineas)
        
    # Proceso de borrado de un registro
    def borrar(self, archivo: Archivo, atributo1, atributo2=None):
        lineas = archivo.leerInfo()
        for linea in lineas:
            datos = linea.rsplit(", ")
            if atributo1 == datos[0] and (atributo2 == datos[1] or atributo2 is None):
                lineas.remove(linea)
                break
            else:
                continue
        print("El objeto ha sido eliminado del archivo.")
        archivo.sobrescribirInfo(lineas)
        
    # Proceso de visualización
    def visualizar(self, archivo: Archivo):
        selector = input('Selecciona como quieres ver la infromación:\n'
                         '1) Jerárquica\n'
                         '2) Tabular\n')
        lineas = archivo.leerInfo()
        # Jerárquica
        if selector == '1':
            lineas.sort()
            for i, linea in enumerate(lineas):
                datos = linea.rstrip('\n').split(', ')
                obj = self.buscar(archivo, datos[0], datos[1])
                print('#',i)
                print(obj.__str__())
                print('---------------------------------------------\n')
                
        # Tabular
        if selector == '2':
            head = archivo.encabezados.split(', ')
            # Presentación de los pantalones
            if len(head) == 5:
                print('+--------------------+--------------------+----------+---------+-------------+')
                print('|{:<20}|{:<20}|{:<10}|{:<8}|{:<13}|'.format(head[0], head[1], head[2], head[3], head[4]))
                for linea in lineas:
                    datos = linea.rstrip('\n').split(', ')
                    print('+--------------------+--------------------+----------+---------+-------------+')
                    print('|{:<20}|{:<20}|{:<10}|${:<8}|{:<13}|'.format(datos[0], datos[1], datos[2], datos[3], datos[4]))
                print('+--------------------+--------------------+----------+---------+-------------+')
            # Presentación de los Proveedores
            elif len(head) == 4:
                print('+--------------------+--------------------+' + ('-'*30) + '+' + ('-'*30) + '+')
                print('|{:<20}|{:<20}|{:<30}|{:<30}|'.format(head[0], head[1], head[2], head[3]))
                for linea in lineas:
                    datos = linea.rstrip('\n').split(', ')
                    print('+--------------------+--------------------+' + ('-'*30) + '+' + ('-'*30) + '+')
                    print('|{:<20}|{:<20}|{:<30}|{:<30}|'.format(datos[0], datos[1], datos[2], datos[3]))
                print('+--------------------+--------------------+' + ('-'*30) + '+' + ('-'*30) + '+')
            # Presentación de los Clientes
            elif len(head) == 3:
                print('+--------------------+--------------------+' + ('-'*30) + '+')
                print('|{:<20}|{:<20}|{:<30}|'.format(head[0], head[1], head[2]))
                for linea in lineas:
                    datos = linea.rstrip('\n').split(', ')
                    print('+--------------------+--------------------+' + ('-'*30) + '+')
                    print('|{:<20}|{:<20}|{:<30}|'.format(datos[0], datos[1], datos[2]))
                print('+--------------------+--------------------+' + ('-'*30) + '+')
    
    # Registro de Ventas     
    def registrar_venta(self, archivo):
        inventario = Archivo("Archivos/Inventario.txt")
        cant = int(input('Cantidad de pantalones vendidos: '))
        pants = []
        monto = 0
        lineas = inventario.leerInfo()
        for i in range(cant):
            marca = input("Ingresa la marca del pantalón: ").upper()
            modelo = input("Ingresa el modelo del pantalón: ").upper()
            for i, linea in enumerate(lineas):
                datos = linea.rstrip('\n').split(', ')
                if datos[0] == marca and datos[1] == modelo:
                    pants.append(f'{marca} | {modelo}')
                    lineas[i] = f"{datos[0]}, {datos[1]}, {datos[2]}, {datos[3]}, {int(datos[4]) - 1}\n"
                    monto += int(datos[3])   
                    break
            if pants == []:
                print("No se encontro el pantalón en el inventario.")
        inventario.sobrescribirInfo(lineas)    
        x = Ventas(monto, pants)
        archivo.añadirInfo(x.__str__())
        
    # Proceso de Exportación
    def exportar(self, archivo: Archivo):
        selector = input('Selecciona como quieres exportar el archivo:\n'
                         '1) CSV\n'
                         '2) XML\n')
        if selector == '1':
            archivo.exportarCSV()
        elif selector == '2':
            archivo.exportarXML()
        else:
            print("Seleccione una opción válida.")
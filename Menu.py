from pathlib import Path
from os import system
from Archivo import Archivo
from Funciones import Main

def menu_principal():
    # Limpieza de terminal
    system("cls")
    
    # Crear el directorio junto a los archivos.
    Path("Archivos").mkdir(exist_ok=True)
    Path("ArchivosCSV").mkdir(exist_ok=True)
    Path("ArchivosXML").mkdir(exist_ok=True)
    
    # Variable que almacenará el archivo con el cual se opera
    file = None
    
    # Variables para realizar búsquedas, modificaciones y borrado de registro
    atr1 = None
    atr2 = None
    
    # Visual del menu principal
    Selector = input("Selecciona la operación ha realizar:\n"
                     "1) Registrar un nuevo pantalon, cliente o proveedor\n"
                     "2) Realizar una búsqueda de un registro\n"
                     "3) Actualizar o Modificar los registros existentes\n"
                     "4) Eliminar un registro existente\n"
                     "5) Ver la información dentro de los archivos\n"
                     "6) Registrar una venta\n"
                     "7) Exportar Archivo a csv o xml\n"
                     "8) Salir\n")
    
    # Cierre del programa
    if Selector == "8":
        print("Hasta luego")
        exit()
        
    # Registro de Venta
    if Selector == "6":
        file = Archivo("Archivos/Registro de Ventas.txt")
        input("Has entrado a la opción para registrar una venta. Presione [Enter] para continuar")
        # Función de registro de venta
        main.registrar_venta(file)
        return
    
    # Selección del archivo con el cual operar
    x = input("Selecciona el file con el que deseas operar:\n"
              "1) Registro de Clientes\n"
              "2) Inventario (Registro de Pantalones)\n"
              "3) Registro de Proveedores\n")
    
    if x == "1":
        file = Archivo("Archivos/Registro de Clientes.txt","Nombre, Celular, Direccion")
        if Selector != "5" and Selector != "7":
            atr1 = input("Ingresa el nombre del cliente: ").upper()
            atr2 = input("Ingresa el número celular del cliente: ")
    elif x == "2":
        file = Archivo("Archivos/Inventario.txt", "Marca, Modelo, Talla, Precio, Disponibles")
    elif x == "3":
        file = Archivo("Archivos/Registro de Proveedores.txt", "Nombre, Marcas, Celular, Correo")
        if Selector != "5" and Selector != "7":
            atr1 = input("Ingresa el nombre del proveedor: ").upper()
    else:
        print("No se ha podido realizar la operación")
        input("Presiona [Enter] para volver al menú principal")
        menu_principal()
            
    # Agregado de un nuevo registro
    if Selector == "1":
        # Función de registro
        main.registrar(file, atr1, atr2)
    
    # Realizar un busqueda
    elif Selector == "2":
        if x == "2":
            op = input("Deseas realizar la búsqueda por talla(1) o por marca y modelo(2): ")
            if op == "1":
                talla = input("Ingresa la talla a buscar: ")
                main.buscar(file, talla=talla)
            elif op == "2":
                atr1 = input("Ingresa la marca del pantalón: ").upper()
                atr2 = input("Ingresa el modelo del pantalón: ").upper()
        # Función de búsqueda
        print(main.buscar(file, atr1, atr2))
    
    # Actualizar registros
    elif Selector == "3":
        # Función de actualización
        main.modificar_registro(file, atr1, atr2)
        
    # Eliminar un registro
    elif Selector == "4":
        # Función de eliminación
        main.borrar(file, atr1, atr2)
    
    # Ver información de los archivos
    elif Selector == "5":
        # Función de información
        main.visualizar(file)
    
    #Exportación de información
    if Selector == "7":
        #Función de exportación
        main.exportar(file)   
    
    # Salir
    else:
        print("No se ha podido realizar la operación")
        input("Presiona [Enter] para volver al menú principal")
        menu_principal()
    
    input("Presiona [Enter] para volver al menú principal")
    menu_principal()
        
if __name__ == "__main__":
    main = Main()
    menu_principal()
class Archivo:

    def __init__(self, ruta, encabezados: str = None) -> None:
        self.ruta = ruta
        self.encabezados = encabezados
        try:
            self.File = open(self.ruta, "w")
            if self.encabezados is not None:
                self.File.write(self.encabezados)
            self.cerrarAchivo()
            print("archivo creado")
        except:
            print("Problemas para crear el archivo")

    def sobrescribirInfo(self, datos: list[str]):
        try:
            self.File = open(self.ruta, 'w')
        except:
            print("Error al tratar de sobrescribir la información del archivo")
        else:
            if self.encabezados is not None:
                self.File.write(self.encabezados)
            for linea in datos:
                self.File.write(linea)
            self.cerrarAchivo()

    def añadirInfo(self, datos: str):
        try:
            self.File = open(self.ruta, 'a')
        except:
            print("Error al tratar de añadir información al archivo")
        else:
            self.File.write(datos)
            self.cerrarAchivo()

    def leerInfo(self) -> list[str]:
        try:
            self.File = open(self.ruta, 'r')
        except:
            print("Error para leer la información del archivo")
        else:
            lineas = self.File.readlines()
            self.cerrarAchivo()
            return lineas

    def cerrarAchivo(self):
        self.File.close()

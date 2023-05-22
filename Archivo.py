class Archivo:

    def __init__(self, ruta: str, encabezados: str = None) -> None:
        self.ruta = ruta
        self.encabezados = encabezados
        self.rutacsv = ruta.split("/")[0] + "CSV/" + ruta.split("/")[1][0:-3] + "csv"
        self.rutaxml = ruta.split("/")[0] + "XML/" + ruta.split("/")[1][0:-3] + "xml"
        try:
            self.File = open(self.ruta, "a")
            self.cerrarArchivo()
        except:
            print("Problemas para crear el archivo")

    def sobrescribirInfo(self, datos: list[str]):
        try:
            self.File = open(self.ruta, 'w')
        except:
            print("Error al tratar de sobrescribir la información del archivo")
        else:
            for linea in datos:
                self.File.write(linea)
            self.cerrarArchivo()

    def añadirInfo(self, datos: str):
        try:
            self.File = open(self.ruta, 'a')
        except:
            print("Error al tratar de añadir información al archivo")
        else:
            self.File.write(datos)
            self.cerrarArchivo()

    def leerInfo(self) -> list[str]:
        try:
            self.File = open(self.ruta, 'r')
        except:
            print("Error para leer la información del archivo")
        else:
            lineas = self.File.readlines()
            self.cerrarArchivo()
            return lineas

    def cerrarArchivo(self):
        self.File.close()

    def exportarCSV(self):
        self.File = open(self.rutacsv, "w")
        self.File.write(self.encabezados.rstrip() + "\n")
        self.File.writelines(self.leerInfo())
        self.cerrarArchivo()
    
    def exportarXML(self):
        atrs = self.encabezados.split(", ")
        lineas = self.leerInfo()
        self.ruta = self.ruta.split("/")[1].replace(" ", "")
        self.File = open(self.rutaxml, "w")
        self.File.write(f"<{self.ruta[0:-4]}>\n")
        for e, linea in enumerate(lineas):
            self.File.write(f"<_{str(e)}_>\n")
            datos = linea.rstrip("\n").split(", ")
            for i, dato in enumerate(datos):
                self.File.write(f"<{atrs[i]}>")
                self.File.write(f"{dato}")
                self.File.write(f"</{atrs[i]}>\n")
            self.File.write(f"</_{str(e)}_>\n")
        self.File.write(f"</{self.ruta[0:-4]}>")
        self.cerrarArchivo()
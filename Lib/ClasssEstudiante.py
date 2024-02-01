class estudiante():
    def __int__(self, mat, nombre, apellido, edad, ) -> None: #int para enteros
        self.mat = mat
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.calificacion = []
        pass
    def  setCalif(self,calificacion):
        self.calificacion = calificacion.append(calificacion)
        pass
    def promedio(self):
        pass
class estGrad(estudiante):
    def __int__(self,mat,nombre, apellido, edad, fecha, tesis):
        super().__int__(mat, nombre,apellido, edad)
        self.fecha = fecha
        self.tesis = tesis
    pass

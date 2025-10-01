class Carrera:
    def __init__(self, nombre, duracion, id = -1):
        self.SetNombre(nombre)
        self.SetDuracion(duracion)
        self.SetId(id)
    
    def GetNombre(self):
        return self.__nombre
    
    def GetDuracion(self):
        return self.__duracion
    
    def GetId(self):
        return self.__id
    
    def SetNombre(self, nombre):
        self.__nombre = nombre
        
    def SetDuracion(self, duracion):
        self.__duracion = duracion
        
    def SetId(self, id):
        self.__id = id
        
    def __str__(self):
        return f'La carrera {self.GetId()} - {self.GetNombre()} dura {self.GetDuracion} años.'
        
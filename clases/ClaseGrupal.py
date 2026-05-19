class Clase_Grupal:
    id:int
    nombre:str
    descripcion: str
    fecha: str
    hora: str
    duracion: int
    cupo_maximo: int
    cant_usuarios_inscritos: int
    
    def __init__(self,id=0, nombre="N.A.", descripcion="N.A.", fecha="N.A.", hora="N.A.", duracion=0,cupo_maximo=0,cant_usuarios_inscritos=0):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.fecha= fecha
        self.hora= hora
        self.duracion= duracion
        self.cupo_maximo= cupo_maximo
        self.cant_usuarios_inscritos= cant_usuarios_inscritos
        self.usuarios_inscritos = []  # arreglo de usuarios inscritos


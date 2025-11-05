class PuntoCarga:
    def __init__(self, id_punto, ubicacion, disponible=True):
        self.id_punto = id_punto
        self.ubicacion = ubicacion
        self.disponible = disponible

    def cambiar_estado(self, nuevo_estado):
        self.disponible = nuevo_estado
from models.usuario import Usuario
from models.punto_carga import PuntoCarga
from models.reserva import Reserva

class ServicioCarga:
    def __init__(self):
        self.usuarios = []
        self.puntos = []
        self.reservas = []

    def crear_usuario(self, id_usuario, nombre, email):
        usuario = Usuario(id_usuario, nombre, email)
        self.usuarios.append(usuario)
        return usuario

    def crear_punto_carga(self, id_punto, ubicacion):
        punto = PuntoCarga(id_punto, ubicacion)
        self.puntos.append(punto)
        return punto

    def reservar_punto(self, id_reserva, usuario, punto):
        if punto.disponible:
            punto.cambiar_estado(False)
            reserva = Reserva(id_reserva, usuario, punto)
            self.reservas.append(reserva)
            return reserva
        else:
            return None
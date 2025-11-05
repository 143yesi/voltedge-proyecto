class Reserva:
    def __init__(self, id_reserva, usuario, punto_carga):
        self.id_reserva = id_reserva
        self.usuario = usuario
        self.punto_carga = punto_carga

    def __str__(self):
        return f"Reserva {self.id_reserva} - {self.usuario.nombre} en {self.punto_carga.ubicacion}"
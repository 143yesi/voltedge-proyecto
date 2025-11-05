from services.service import ServicioCarga

def main():
    servicio = ServicioCarga()

    usuario1 = servicio.crear_usuario(1, "Yésica", "yesica@example.com")
    punto1 = servicio.crear_punto_carga(101, "Vigo Centro")

    reserva = servicio.reservar_punto(1001, usuario1, punto1)

    if reserva:
        print("Reserva realizada con éxito:")
        print(reserva)
    else:
        print("Error: el punto de carga no está disponible.")

if __name__ == "__main__":
    main()
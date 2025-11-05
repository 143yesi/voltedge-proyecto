from .session import Session

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.active_session = None

    def start_session(self, charger):
        """Inicia una sesión si el cargador está disponible"""
        if charger.status == "disponible":
            charger.start_charge()
            self.active_session = Session(self, charger)
            print(f"{self.name} comenzó una sesión en el cargador {charger.id}")
        else:
            print(f"El cargador {charger.id} no está disponible.")

    def end_session(self):
        """Finaliza la sesión activa"""
        if self.active_session:
            self.active_session.end()
            self.active_session.charger.stop_charge()
            print(f"{self.name} terminó su sesión.")
            self.active_session = None
        else:
            print(f"{self.name} no tiene ninguna sesión activa.")
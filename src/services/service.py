from models.station import Station
from models.charger import Charger
from models.user import User
from models.maintenance import Maintenance, PreventiveMaintenance, CorrectiveMaintenance


class ChargingService:
    def __init__(self):
        self.stations = []
        self.users = []
        self.maintenances = []  # <- lista de mantenimientos


    # ---------- Gestión de estaciones ----------
    def create_station(self, id, name, location):
        station = Station(id, name, location)
        self.stations.append(station)
        print(f"Estación '{name}' creada en {location}")
        return station

    def add_charger_to_station(self, station_id, charger_id, charger_type):
        station = next((s for s in self.stations if s.id == station_id), None)
        if station:
            charger = Charger(charger_id, charger_type)
            station.add_charger(charger)
            print(f"⚡ Cargador {charger_id} añadido a {station.name}")
            return charger
        else:
            print("Estación no encontrada.")

    # ---------- Gestión de usuarios ----------
    def register_user(self, id, name, email):
        user = User(id, name, email)
        self.users.append(user)
        print(f"Usuario '{name}' registrado.")
        return user

    # ---------- Reservas / sesiones ----------
    def start_charging(self, user_id, station_id):
        user = next((u for u in self.users if u.id == user_id), None)
        station = next((s for s in self.stations if s.id == station_id), None)

        if not user or not station:
            print("Usuario o estación no encontrados.")
            return

        available = station.get_available_chargers()
        if not available:
            print(f"No hay cargadores disponibles en {station.name}.")
            return

        charger = available[0]
        user.start_session(charger)

    def end_charging(self, user_id):
        user = next((u for u in self.users if u.id == user_id), None)
        if user:
            user.end_session()
        else:
            print("Usuario no encontrado.")
            
    # -------- MANTENIMIENTO ----------
    def programar_mantenimiento_preventivo(self, id_mantenimiento, station_id, fecha, tecnico, frecuencia):
        m = PreventiveMaintenance(id_mantenimiento, fecha, tecnico, frecuencia)
        m.asignar_estacion(station_id)
        self.maintenances.append(m)
        print(m.programar())
        return m

    def programar_mantenimiento_correctivo(self, id_mantenimiento, station_id, fecha, tecnico, descripcion_fallo):
        m = CorrectiveMaintenance(id_mantenimiento, fecha, tecnico, descripcion_fallo)
        m.asignar_estacion(station_id)
        self.maintenances.append(m)
        print(m.programar())
        return m

    def iniciar_mantenimiento(self, id_mantenimiento):
        m = next((x for x in self.maintenances if x.id_mantenimiento == id_mantenimiento), None)
        if not m:
            print("Mantenimiento no encontrado.")
            return None
        print(m.iniciar())
        return m

    def completar_mantenimiento(self, id_mantenimiento, notas=""):
        m = next((x for x in self.maintenances if x.id_mantenimiento == id_mantenimiento), None)
        if not m:
            print("Mantenimiento no encontrado.")
            return None
        print(m.marcar_completado(notas))
        return m

    def listar_mantenimientos(self, station_id=None):
        if station_id:
            return [m for m in self.maintenances if m.estacion_id == station_id]
        return list(self.maintenances)
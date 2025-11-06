# ⚡ VOLTEDGE – Sistema de Gestión de Carga de Vehículos Eléctricos

## Descripción
VoltEdge es una aplicación orientada a la gestión de **puntos de carga para vehículos eléctricos**.  
Permite **registrar usuarios**, **reservar cargadores**, **iniciar sesiones de carga**, y **programar mantenimientos** de las estaciones.

Proyecto realizado para la asignatura **Arquitectura de Software**, Universidad Intercontinental de la Empresa.

--

## Estructura del proyecto

1. voltedge-proyecto/src/
2. voltedge-proyecto/src/models
3. voltedge-proyecto/src/services
4. voltedge-proyecto/src/main,py
5. voltedge-proyecto/README.md         

--

## Clases principales

- `User` – Representa un usuario que puede reservar e iniciar sesiones de carga.  
- `Station` – Agrupa varios cargadores y su estado.  
- `Charger` – Cargador individual (normal, rápido, etc.).  
- `Session` – Controla la carga activa de un vehículo.  
- `Maintenance` – Base para mantenimientos preventivos o correctivos.

## ChargingService

Contiene la lógica de negocio principal:
- Crear estaciones y usuarios.
- Reservar puntos de carga.
- Iniciar y finalizar sesiones.
- Programar mantenimientos.

---

## Ejecución
Clonar el repositorio:
   ```bash
   git clone https://github.com/143yesi/voltedge-proyecto.git
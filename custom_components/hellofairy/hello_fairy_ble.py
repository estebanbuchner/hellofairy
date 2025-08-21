import asyncio
import logging
from bleak import BleakClient

_LOGGER = logging.getLogger(__name__)

class HelloFairyBLE:
    def __init__(self, mac):
        self._mac = mac
        self._client = BleakClient(mac)
        self._connected = False

    async def connect(self):
        try:
            # Fase 0.1.1: Intentar conectar con timeout
            await asyncio.wait_for(self._client.connect(), timeout=20)
            self._connected = self._client.is_connected  # En HA es propiedad, no coroutine
            _LOGGER.info(f"Conectado a {self._mac}: {self._connected}")

            # Fase 0.1.2: Validar servicios disponibles
            if self._connected:
                services = self._client.services  # En HA ya está poblado tras connect()
                if not services or not hasattr(services, "services") or len(services.services) == 0:
                    _LOGGER.warning(f"{self._mac} conectado pero sin servicios disponibles")
                    self._connected = False
                    return False

                # Validar que al menos un servicio tenga características
                has_characteristics = any(
                    hasattr(s, "characteristics") and len(s.characteristics) > 0
                    for s in services.services.values()
                )
                if not has_characteristics:
                    _LOGGER.warning(f"{self._mac} conectado pero sin características en los servicios")
                    self._connected = False
                    return False

            return self._connected

        except asyncio.TimeoutError:
            _LOGGER.warning(f"Fase 0.1.1: Timeout al conectar con {self._mac}")
            self._connected = False
            return False

        except Exception:
            _LOGGER.exception(f"Fase 0.1.2: Error general al conectar con {self._mac}")
            self._connected = False
            return False

    async def disconnect(self):
        try:
            if self._client.is_connected:  # En HA es propiedad booleana
                await self._client.disconnect()
                _LOGGER.info(f"Desconectado de {self._mac}")
            self._connected = False
        except Exception:
            _LOGGER.exception(f"Error al desconectar de {self._mac}")
            self._connected = False

    def is_connected(self):
        return self._connected

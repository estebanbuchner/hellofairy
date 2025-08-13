import asyncio
import logging
from bleak import BleakClient

_LOGGER = logging.getLogger(__name__)

class HelloFairyBLE:
    def __init__(self, mac_address: str):
        self._mac = mac_address
        self._client = BleakClient(mac_address)
        self._connected = False

    async def connect(self):
        try:
            await self._client.connect()
            self._connected = await self._client.is_connected()
            _LOGGER.info(f"Conectado a {self._mac}: {self._connected}")
        except Exception as e:
            _LOGGER.error(f"Error al conectar a {self._mac}: {e}")
            self._connected = False

    async def disconnect(self):
        try:
            await self._client.disconnect()
            self._connected = False
            _LOGGER.info(f"Desconectado de {self._mac}")
        except Exception as e:
            _LOGGER.warning(f"Error al desconectar: {e}")

    def is_connected(self):
        return self._connected

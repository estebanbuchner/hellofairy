import logging
from .const import DOMAIN, DEFAULT_MAC
from .hello_fairy_ble import HelloFairyBLE

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    """Inicializa la integración Hello Fairy BLE."""
    conf = config.get(DOMAIN, {})
    mac = conf.get("mac_address", DEFAULT_MAC)

    _LOGGER.info(f"[HelloFairy] MAC configurada: {mac}")

    controller = HelloFairyBLE(mac)
    hass.data[DOMAIN] = controller

    await controller.connect()

    if controller.is_connected():
        _LOGGER.info(f"[HelloFairy] Conexión BLE exitosa con {mac}")
    else:
        _LOGGER.warning(f"[HelloFairy] No se pudo conectar a {mac}")

    return True

async def async_setup_entry(hass, entry, async_add_entities):
    controller = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([HelloFairyConnectionSensor(controller)])

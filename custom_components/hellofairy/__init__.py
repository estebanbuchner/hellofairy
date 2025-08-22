import logging
from .const import DOMAIN, DEFAULT_MAC
from .hello_fairy_ble import HelloFairyBLE
from .binary_sensor import HelloFairyConnectionSensor

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    """Inicializa la integración Hello Fairy BLE."""
    conf = config.get(DOMAIN, {})
    mac = conf.get("mac_address", DEFAULT_MAC)

    _LOGGER.info(f"[HelloFairy] MAC configurada: {mac}")

    controller = HelloFairyBLE(mac)
    hass.data.setdefault(DOMAIN, {})["controller"] = controller

    # Lanzar conexión BLE en segundo plano
    async def connect_ble():
        await controller.connect()
        if controller.is_connected():
            _LOGGER.info(f"[HelloFairy] Conexión BLE exitosa con {mac}")
        else:
            _LOGGER.warning(f"[HelloFairy] No se pudo conectar a {mac}")

    hass.async_create_task(connect_ble())

    return True

async def async_setup_entry(hass, entry, async_add_entities):
    """Registra entidades asociadas al controller."""
    controller = hass.data[DOMAIN].get("controller")

    if not controller:
        _LOGGER.error("[HelloFairy] Controller no disponible en setup_entry")
        return False

    async_add_entities([HelloFairyConnectionSensor(controller)])
    _LOGGER.info("[HelloFairy] Sensor binario registrado correctamente")

    return True

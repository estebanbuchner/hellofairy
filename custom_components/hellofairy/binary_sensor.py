from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup_platform(hass: HomeAssistant, config, async_add_entities: AddEntitiesCallback, discovery_info=None):
    controller = hass.data[DOMAIN]
    async_add_entities([HelloFairyBLEConnected(controller)], update_before_add=True)

class HelloFairyBLEConnected(BinarySensorEntity):
    def __init__(self, controller):
        self._controller = controller
        self._attr_name = "Hello Fairy BLE Connected"
        self._attr_device_class = "connectivity"

    @property
    def is_on(self):
        return self._controller.is_connected()

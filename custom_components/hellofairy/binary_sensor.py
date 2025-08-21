from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers.entity import EntityCategory

class HelloFairyConnectionSensor(BinarySensorEntity):
    def __init__(self, controller):
        self._controller = controller
        self._attr_name = "Hello Fairy BLE Connected"
        self._attr_unique_id = f"hellofairy_ble_connected"
        self._attr_device_class = "connectivity"
        self._attr_entity_category = EntityCategory.DIAGNOSTIC

    @property
    def is_on(self):
        return self._controller.is_connected()


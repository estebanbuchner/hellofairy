import logging

_LOGGER = logging.getLogger(__name__)
DOMAIN = "hellofairy"

async def async_setup(hass, config):
    _LOGGER.info("[HelloFairy] Integración lógica iniciada")

    async def handle_modo_fiesta(call):
        _LOGGER.info("[HelloFairy] Activando modo fiesta")
        await hass.services.async_call("number", "set_value", {
            "entity_id": "number.preset",
            "value": 58
        })
        await hass.services.async_call("light", "turn_on", {
            "entity_id": "light.string"
        })

    async def handle_apagar(call):
        _LOGGER.info("[HelloFairy] Apagando luces")
        await hass.services.async_call("light", "turn_off", {
            "entity_id": "light.string"
        })
        await hass.services.async_call("switch", "turn_off", {
            "entity_id": "switch.power"
        })

    hass.services.async_register(DOMAIN, "modo_fiesta", handle_modo_fiesta)
    hass.services.async_register(DOMAIN, "apagar", handle_apagar)

    return True

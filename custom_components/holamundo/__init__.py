import logging
from .const import DOMAIN


_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
    conf = config.get(DOMAIN)
    valor = conf.get("dato")

    hass.data[DOMAIN] = {
        "dato": valor,

    }

    return True



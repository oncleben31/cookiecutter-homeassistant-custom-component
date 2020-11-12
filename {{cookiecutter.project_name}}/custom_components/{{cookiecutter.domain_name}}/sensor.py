"""Sensor platform for {{cookiecutter.friendly_name}}."""
from .const import DEFAULT_NAME, DOMAIN, ICON, SENSOR
from .entity import {{cookiecutter.class_name_prefix}}Entity

from homeassistant.util import slugify


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([{{cookiecutter.class_name_prefix}}Sensor(coordinator, entry)])


class {{cookiecutter.class_name_prefix}}Sensor({{cookiecutter.class_name_prefix}}Entity):
    """{{cookiecutter.domain_name}} Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}"

    @property
    def state(self):
        """Return the state of the sensor."""
        # slugify the state to allow translation
        return slugify(self.coordinator.data.get("static"))

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

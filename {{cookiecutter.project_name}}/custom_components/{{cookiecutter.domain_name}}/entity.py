"""{{cookiecutter.class_name_prefix}}Entity class"""
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .const import NAME
from .const import VERSION


class {{cookiecutter.class_name_prefix}}Entity(CoordinatorEntity):
    def __init__(self, coordinator, config_entry):
        super().__init__(coordinator)
        self.config_entry = config_entry

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return self.config_entry.entry_id

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": NAME,
            "model": VERSION,
            "manufacturer": NAME,
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            "time": str(self.coordinator.data.get("time")),
            "static": self.coordinator.data.get("static"),
        }

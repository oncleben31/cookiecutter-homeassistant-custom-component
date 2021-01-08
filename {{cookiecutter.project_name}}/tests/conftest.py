"""Global fixtures for {{cookiecutter.friendly_name}} integration."""
import pytest
from pytest_homeassistant_custom_component.async_mock import patch

pytest_plugins = "pytest_homeassistant_custom_component"

# This fixture is used to prevent HomeAssistant from attempting to create and dismiss persistent
# notifications. These calls would fail without this fixture since the persistent_notification
# integration is never loaded during a test.
@pytest.fixture(name="skip_notifications", autouse=True)
def skip_notifications_fixture():
    """Skip notification calls."""
    with patch("homeassistant.components.persistent_notification.async_create"), patch(
        "homeassistant.components.persistent_notification.async_dismiss"
    ):
        yield


@pytest.fixture(name="bypass_get_data")
def bypass_get_data_fixture():
    """Skip calls to get data from API."""
    with patch(
        "custom_components.{{cookiecutter.domain_name}}.{{cookiecutter.class_name_prefix}}ApiClient.async_get_data"
    ):
        yield


@pytest.fixture(name="error_on_get_data")
def error_get_data_fixture():
    """Simulate error when retrieving data from API."""
    with patch(
        "custom_components.{{cookiecutter.domain_name}}.{{cookiecutter.class_name_prefix}}ApiClient.async_get_data",
        side_effect=Exception,
    ):
        yield

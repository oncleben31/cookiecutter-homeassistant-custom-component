"""Tests for {{cookiecutter.project_name}} api."""
import asyncio

import aiohttp
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from custom_components.{{cookiecutter.project_name}}.api import {{cookiecutter.class_name_prefix}}ApiClient


async def test_ap(hass, aioclient_mock, caplog):
    """Test API calls."""

    api = {{cookiecutter.class_name_prefix}}ApiClient("test", "test", async_get_clientsession(hass))

    aioclient_mock.get(
        "https://jsonplaceholder.typicode.com/posts/1", json={"test": "test"}
    )
    assert await api.async_get_data() == {"test": "test"}

    aioclient_mock.patch("https://jsonplaceholder.typicode.com/posts/1")
    assert await api.async_set_title("test") is None

    caplog.clear()
    aioclient_mock.put(
        "https://jsonplaceholder.typicode.com/posts/1", exc=asyncio.TimeoutError
    )
    assert (
        await api.api_wrapper("put", "https://jsonplaceholder.typicode.com/posts/1")
        is None
    )
    assert (
        len(caplog.record_tuples) == 1
        and "Timeout error fetching information from" in caplog.record_tuples[0][2]
    )

    caplog.clear()
    aioclient_mock.post(
        "https://jsonplaceholder.typicode.com/posts/1", exc=aiohttp.ClientError
    )
    assert (
        await api.api_wrapper("post", "https://jsonplaceholder.typicode.com/posts/1")
        is None
    )
    assert (
        len(caplog.record_tuples) == 1
        and "Error fetching information from" in caplog.record_tuples[0][2]
    )

    caplog.clear()
    aioclient_mock.post("https://jsonplaceholder.typicode.com/posts/2", exc=Exception)
    assert (
        await api.api_wrapper("post", "https://jsonplaceholder.typicode.com/posts/2")
        is None
    )
    assert (
        len(caplog.record_tuples) == 1
        and "Something really wrong happened!" in caplog.record_tuples[0][2]
    )

    caplog.clear()
    aioclient_mock.post("https://jsonplaceholder.typicode.com/posts/3", exc=TypeError)
    assert (
        await api.api_wrapper("post", "https://jsonplaceholder.typicode.com/posts/3")
        is None
    )
    assert (
        len(caplog.record_tuples) == 1
        and "Error parsing information from" in caplog.record_tuples[0][2]
    )

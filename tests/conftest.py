import pytest

from dependency_injection.dependency_injector_example.containers import Container


@pytest.fixture
def container():
    container = Container()
    yield container

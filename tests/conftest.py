import pytest

from dependency_injection.dependency_injector_library.containers import Container


@pytest.fixture
def container() -> Container:
    return Container()

from unittest.mock import MagicMock, create_autospec

from assertpy import assert_that

from dependency_injection.dependency_injector_library.assets import KeyValuePair, Reader
from dependency_injection.dependency_injector_library.containers import Container


def create_mock_reader() -> MagicMock:
    mock_reader = create_autospec(spec=Reader, spec_set=True, instance=True)
    mock_reader.read.return_value = [KeyValuePair("a_key", "a_value")]
    return mock_reader


def test_create_a_new_container_instance() -> None:
    mock_reader = create_mock_reader()
    container = Container(reader=mock_reader)  # overwrite
    reader: Reader = container.reader()

    actual = reader.read("a_non_existing_path")

    assert_that(actual).is_equal_to([KeyValuePair("a_key", "a_value")])


def test_use_an_existing_container_as_a_fixture(container: Container) -> None:
    mock_reader = create_mock_reader()
    with container.override_providers(reader=mock_reader):  # overwrite
        reader: Reader = container.reader()

        actual = reader.read("a_non_existing_path")

        assert_that(actual).is_equal_to([KeyValuePair("a_key", "a_value")])

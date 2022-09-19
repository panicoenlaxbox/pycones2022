from unittest.mock import MagicMock, create_autospec

from assertpy import assert_that

from dependency_injection.dependency_injector_example.assets import KeyValuePair, Reader
from dependency_injection.dependency_injector_example.containers import Container


def create_mock_reader() -> MagicMock:
    return create_autospec(spec=Reader, spec_set=True, instance=True)


def test_create_a_new_container_instance() -> None:
    mock_reader = create_mock_reader()
    mock_reader.read.return_value = [KeyValuePair("a_key", "a_value")]
    container = Container(reader=mock_reader)
    reader: Reader = container.reader()

    actual = reader.read("a_non_existing_path")

    assert_that(actual).is_equal_to([KeyValuePair("a_key", "a_value")])


def test_use_an_existing_container_as_a_fixture(container: Container) -> None:
    mock_reader = create_mock_reader()
    mock_reader.read.return_value = [KeyValuePair("a_key", "a_value")]
    with container.override_providers(reader=mock_reader):
        reader: Reader = container.reader()

        actual = reader.read("a_non_existing_path")

        assert_that(actual).is_equal_to([KeyValuePair("a_key", "a_value")])

from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration

from dependency_injection.dependency_injector_library.assets import (
    JsonFileReader,
    JsonSchemaValidator,
    Reader,
    ResourceLoader,
    YamlFileReader,
)


def _create_reader(config: Configuration) -> Reader:
    if config["reader"] == "json":
        return JsonFileReader(
            JsonSchemaValidator(ResourceLoader("dependency_injection.dependency_injector_library.resources"))
        )
    else:
        return YamlFileReader()


class Container(DeclarativeContainer):
    _config = providers.Configuration(json_files=["config.json"])
    resource_loader = providers.Factory(
        ResourceLoader, providers.Object("dependency_injection.dependency_injector_library.resources")
    )
    json_schema_validator = providers.Factory(JsonSchemaValidator, resource_loader)
    json_file_reader = providers.Factory(JsonFileReader, json_schema_validator)
    yaml_file_reader = providers.Factory(YamlFileReader)
    reader = providers.Selector(
        _config.reader,
        json=json_file_reader,
        yaml=yaml_file_reader,
    )
    # reader = providers.Factory(_create_reader, _config)
    path = _config.path

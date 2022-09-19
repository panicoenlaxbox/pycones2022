from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from dependency_injection.dependency_injector_example.assets import (
    JsonFileReader,
    JsonSchemaValidator,
    ResourceLoader,
    YamlFileReader,
)


class Container(DeclarativeContainer):
    _config = providers.Configuration(json_files=["config.json"])
    resource_loader = providers.Factory(
        ResourceLoader, providers.Object("dependency_injection.dependency_injector_example.resources")
    )
    json_schema_validator = providers.Factory(JsonSchemaValidator, resource_loader)
    reader = providers.Selector(
        _config.reader,
        json=providers.Factory(JsonFileReader, json_schema_validator),
        yaml=providers.Factory(YamlFileReader),
    )
    path = _config.path

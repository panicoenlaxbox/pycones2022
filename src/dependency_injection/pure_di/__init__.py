import abc
import json
from abc import abstractmethod
from dataclasses import dataclass
from pprint import pprint
from typing import Iterable

import fastjsonschema
import importlib_resources
import yaml


@dataclass
class KeyValuePair:
    key: str
    value: str


class Reader(abc.ABC):
    @abstractmethod
    def read(self, path: str) -> Iterable[KeyValuePair]:
        pass


class ResourceLoader:
    def __init__(self, package: str) -> None:
        self._package = package

    def load(self, name: str) -> str:
        return importlib_resources.files(self._package).joinpath(name).read_text(encoding="utf-8")


class JsonSchemaValidator:
    def __init__(self, resource_loader: ResourceLoader) -> None:
        self._resource_loader = resource_loader

    def validate(self, path: str) -> None:
        definition = json.loads(self._resource_loader.load("schema.json"))
        with (open(path)) as f:
            data = json.load(f)
            fastjsonschema.validate(definition, data)


class JsonFileReader(Reader):
    def __init__(self, json_schema_validator: JsonSchemaValidator) -> None:
        self._json_schema_validator = json_schema_validator

    def read(self, path: str) -> Iterable[KeyValuePair]:
        self._json_schema_validator.validate(path)

        with (open(path)) as f:
            return [KeyValuePair(**item) for item in (json.load(f))]


class YamlFileReader(Reader):
    def read(self, path: str) -> Iterable[KeyValuePair]:
        with (open(path)) as f:
            return [KeyValuePair(**item) for item in (yaml.safe_load(f))]


def main(reader: Reader, path: str) -> None:
    pprint(reader.read(path))


if __name__ == "__main__":
    main(YamlFileReader(), "../../../data/key_value.yaml")

    # main(
    #     JsonFileReader(
    #         JsonSchemaValidator(ResourceLoader("dependency_injection.dependency_injector_library.resources"))
    #     ),
    #     "../../../data/key_value.json",
    # )

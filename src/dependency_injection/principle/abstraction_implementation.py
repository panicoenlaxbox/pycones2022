from abc import ABC, abstractmethod


class Reader(ABC):  # Abstraction
    @abstractmethod
    def read(self) -> str:
        ...


class FileReader(Reader):  # Implementation
    def __init__(self, path: str) -> None:
        self._path = path

    def read(self) -> str:
        with (open(self._path, "r")) as f:
            return f.read()

    @property
    def path(self) -> str:
        return self._path


def main() -> None:
    reader: Reader = FileReader("../../../data/key_value.json")  # I'm working with an abstraction
    print(reader.read())
    # It works but mypy doesn't like it
    print(reader.path)  # type: ignore


if __name__ == "__main__":
    main()

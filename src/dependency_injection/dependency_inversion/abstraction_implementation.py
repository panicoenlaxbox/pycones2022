from abc import ABC, abstractmethod

import requests


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


class UrlReader(Reader):  # Implementation
    def __init__(self, url: str, user_name: None | str = None, password: None | str = None) -> None:
        self._url = url
        self._user_name = user_name
        self._password = password

    def read(self) -> str:
        auth: None | tuple[str, str] = None
        if self._user_name is not None and self._password is not None:
            auth = (self._user_name, self._password)
        return requests.get(self._url, auth=auth).text


def main() -> None:
    reader: Reader = FileReader("../../../data/key_value.json")
    # reader: Reader = UrlReader("https://www.google.es/")
    print(reader.read())

    print(reader.path)  # type: ignore


if __name__ == "__main__":
    main()

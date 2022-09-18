from typing import Any


class Order:
    ...


class DbOrdersRepository:  # No longer inherits from a base class
    def save(self, order: Order) -> None:
        ...


class ShopCartService:
    def __init__(self, repository: Any) -> None:  # I can't specify parameter type
        self._repository = repository

    def checkout(self) -> None:
        order = Order()

        # We assume that self._repository has a save method with a parameter of type Order...
        self._repository.save(order)

        # region Workarounds
        try:
            self._repository.save(order)
        except:  # noqa: E722
            ...

        if hasattr(self._repository, "save"):
            self._repository.save(order)
        else:
            ...
        # endregion

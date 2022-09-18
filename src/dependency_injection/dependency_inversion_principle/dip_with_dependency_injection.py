import abc


class Order:
    ...


class OrdersRepository(abc.ABC):  # Abstraction
    @abc.abstractmethod
    def save(self, order: Order) -> None:
        ...


class DbOrdersRepository(OrdersRepository):  # Low-level module depends on abstraction
    def save(self, order: Order) -> None:
        ...


class ShopCartService:
    # High-level module depends on abstraction
    def __init__(self, repository: OrdersRepository) -> None:  # Dependency injection
        self._repository = repository

    def checkout(self) -> None:
        order = Order()

        self._repository.save(order)

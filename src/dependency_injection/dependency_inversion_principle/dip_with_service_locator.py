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


class Container:
    @staticmethod
    def create_repository() -> OrdersRepository:
        return DbOrdersRepository()


class ShopCartService:
    def __init__(self) -> None:
        # High-level module depends on abstraction
        self._repository = Container.create_repository()  # Service locator

    def checkout(self) -> None:
        order = Order()

        self._repository.save(order)

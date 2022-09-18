import abc


class Order:
    ...


class OrdersRepository(abc.ABC):
    @abc.abstractmethod
    def save(self, order: Order) -> None:
        ...


class DbOrdersRepository(OrdersRepository):
    def save(self, order: Order) -> None:
        ...


class FileOrdersRepository(OrdersRepository):
    def save(self, order: Order) -> None:
        ...


class ShopCartService:
    def __init__(self, repository: OrdersRepository) -> None:
        self._repository = repository

    def checkout(self) -> None:
        order = Order()

        self._repository.save(order)


service_using_files = ShopCartService(FileOrdersRepository())
service_using_a_db = ShopCartService(DbOrdersRepository())

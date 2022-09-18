import abc
import time
from typing import Callable


class ShopCartServiceBase(abc.ABC):
    @abc.abstractmethod
    def checkout(self) -> None:
        ...


class ShopCartService(ShopCartServiceBase):
    def checkout(self) -> None:
        print("Checkout is in progress...")
        time.sleep(3)


class TimedShopCartService(ShopCartServiceBase):  # Decorator pattern
    def __init__(self, shop_cart_service: ShopCartService) -> None:
        self._shop_cart_service = shop_cart_service

    @staticmethod
    def _timed_operation(func: Callable) -> None:
        tic = time.perf_counter()

        func()

        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")

    def checkout(self) -> None:
        self._timed_operation(self._shop_cart_service.checkout)


service = TimedShopCartService(ShopCartService())
service.checkout()

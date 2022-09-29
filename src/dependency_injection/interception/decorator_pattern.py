import time
from typing import Callable

from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer


class ShopCartService:
    def checkout(self) -> None:
        print("Checkout is in progress...")
        time.sleep(3)


class TimedShopCartService(ShopCartService):
    def __init__(self, shop_cart_service: ShopCartService) -> None:
        self._shop_cart_service = shop_cart_service

    @staticmethod
    def _timer(func: Callable) -> None:
        tic = time.perf_counter()

        func()

        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")

    def checkout(self) -> None:
        self._timer(self._shop_cart_service.checkout)


class Container(DeclarativeContainer):
    shop_cart_service = providers.Factory(ShopCartService)
    # shop_cart_service = providers.Factory(TimedShopCartService, providers.Factory(ShopCartService))


if __name__ == "__main__":
    container = Container()
    container.shop_cart_service().checkout()

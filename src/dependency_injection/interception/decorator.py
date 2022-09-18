import time
import typing
from functools import wraps


@typing.no_type_check
def timer(func):
    @wraps(func)
    def _(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return value

    return _


class ShopCartService:
    @timer
    def checkout(self) -> None:
        print("Checkout is in progress...")
        time.sleep(3)


service = ShopCartService()
service.checkout()

import pytest

from praktikum.bun import Bun
from data import BUN_TEST_DATA, BUN_NAME_TEST_DATA, BUN_PRICE_TEST_DATA


class TestBun:
    @pytest.mark.parametrize("name,price", BUN_TEST_DATA)
    def test_init(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    @pytest.mark.parametrize("name,price", BUN_NAME_TEST_DATA)
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name,price", BUN_PRICE_TEST_DATA)
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price


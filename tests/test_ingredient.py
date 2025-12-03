import pytest

from praktikum.ingredient import Ingredient
from data import (
    INGREDIENT_INIT_TEST_DATA,
    INGREDIENT_PRICE_TEST_DATA,
    INGREDIENT_NAME_TEST_DATA,
    INGREDIENT_TYPE_TEST_DATA,
)


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type,name,price", INGREDIENT_INIT_TEST_DATA)
    def test_init(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    @pytest.mark.parametrize("ingredient_type,name,price", INGREDIENT_PRICE_TEST_DATA)
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type,name,price", INGREDIENT_NAME_TEST_DATA)
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type,name,price", INGREDIENT_TYPE_TEST_DATA)
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type


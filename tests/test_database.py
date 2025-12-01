import pytest

from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import DATABASE_BUNS_DATA, DATABASE_INGREDIENTS_DATA, DATABASE_INGREDIENTS_PRICES


class TestDatabase:
    def test_init(self, database):
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

    def test_init_buns(self, database):
        assert isinstance(database.buns[0], Bun)
        assert isinstance(database.buns[1], Bun)
        assert isinstance(database.buns[2], Bun)
        assert database.buns[0].get_name() == "black bun"
        assert database.buns[1].get_name() == "white bun"
        assert database.buns[2].get_name() == "red bun"
        assert database.buns[0].get_price() == 100
        assert database.buns[1].get_price() == 200
        assert database.buns[2].get_price() == 300

    def test_init_ingredients(self, database):
        assert isinstance(database.ingredients[0], Ingredient)
        assert database.ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert database.ingredients[0].get_name() == "hot sauce"
        assert database.ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert database.ingredients[3].get_name() == "cutlet"

    @pytest.mark.parametrize("index,expected_name,expected_price", DATABASE_BUNS_DATA)
    def test_available_buns(self, database, index, expected_name, expected_price):
        buns = database.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == 3
        assert buns[index].get_name() == expected_name
        assert buns[index].get_price() == expected_price

    def test_available_buns_returns_list(self, database):
        buns = database.available_buns()
        assert isinstance(buns, list)
        assert all(isinstance(bun, Bun) for bun in buns)

    @pytest.mark.parametrize("index,expected_type,expected_name", DATABASE_INGREDIENTS_DATA)
    def test_available_ingredients(self, database, index, expected_type, expected_name):
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        assert ingredients[index].get_type() == expected_type
        assert ingredients[index].get_name() == expected_name

    def test_available_ingredients_returns_list(self, database):
        ingredients = database.available_ingredients()
        assert isinstance(ingredients, list)
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)

    def test_available_ingredients_prices(self, database):
        ingredients = database.available_ingredients()
        expected_prices = DATABASE_INGREDIENTS_PRICES
        for i, ingredient in enumerate(ingredients):
            assert ingredient.get_price() == expected_prices[i]


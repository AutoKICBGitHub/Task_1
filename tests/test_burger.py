import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import BURGER_PRICE_PARAMETRIZED_DATA, INGREDIENT_NAMES, INGREDIENT_PRICES, MOCK_BUN_PRICE, MOCK_INGREDIENT_PRICES


class TestBurger:
    def test_init(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_set_buns_with_mock(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, ingredient_sauce):
        burger.add_ingredient(ingredient_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_sauce

    def test_add_multiple_ingredients(self, burger, ingredient_sauce, ingredient_filling):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        assert len(burger.ingredients) == 2
        assert burger.ingredients[0] == ingredient_sauce
        assert burger.ingredients[1] == ingredient_filling

    def test_remove_ingredient(self, burger, ingredient_sauce, ingredient_filling):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient_filling

    def test_remove_ingredient_last(self, burger, ingredient_sauce):
        burger.add_ingredient(ingredient_sauce)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger, ingredient_sauce, ingredient_filling):
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_filling
        assert burger.ingredients[1] == ingredient_sauce

    def test_move_ingredient_to_beginning(self, burger):
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAMES["sauce1"], INGREDIENT_PRICES["sauce1"])
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_NAMES["filling1"], INGREDIENT_PRICES["filling1"])
        ingredient3 = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAMES["sauce2"], INGREDIENT_PRICES["sauce2"])
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(2, 0)
        assert burger.ingredients[0] == ingredient3
        assert burger.ingredients[1] == ingredient1
        assert burger.ingredients[2] == ingredient2

    def test_get_price_with_bun_only(self, burger, bun):
        burger.set_buns(bun)
        expected_price = bun.get_price() * 2
        assert burger.get_price() == expected_price

    def test_get_price_with_bun_and_ingredients(self, burger, bun, ingredient_sauce, ingredient_filling):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        expected_price = bun.get_price() * 2 + ingredient_sauce.get_price() + ingredient_filling.get_price()
        assert burger.get_price() == expected_price

    def test_get_price_with_mock(self, burger, mock_bun):
        mock_ingredient1 = Mock(spec=Ingredient)
        mock_ingredient1.get_price.return_value = MOCK_INGREDIENT_PRICES["ingredient1"]
        mock_ingredient2 = Mock(spec=Ingredient)
        mock_ingredient2.get_price.return_value = MOCK_INGREDIENT_PRICES["ingredient2"]
        
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        price = burger.get_price()
        expected_price = MOCK_BUN_PRICE * 2 + MOCK_INGREDIENT_PRICES["ingredient1"] + MOCK_INGREDIENT_PRICES["ingredient2"]
        assert price == expected_price
        mock_bun.get_price.assert_called()
        assert mock_ingredient1.get_price.called
        assert mock_ingredient2.get_price.called

    @pytest.mark.parametrize("bun_name,bun_price,ingredient_count", BURGER_PRICE_PARAMETRIZED_DATA)
    def test_get_price_parametrized(self, burger, bun_name, bun_price, ingredient_count):
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        for i in range(ingredient_count):
            ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, f"sauce{i}", 50.0 * (i + 1))
            burger.add_ingredient(ingredient)
        expected_price = bun_price * 2 + sum(50.0 * (i + 1) for i in range(ingredient_count))
        assert burger.get_price() == expected_price

    def test_get_receipt_with_bun_only(self, burger, bun):
        burger.set_buns(bun)
        receipt = burger.get_receipt()
        assert f'(==== {bun.get_name()} ====)' in receipt
        assert f'Price: {burger.get_price()}' in receipt
        assert receipt.count(f'(==== {bun.get_name()} ====)') == 2

    def test_get_receipt_with_ingredients(self, burger, bun, ingredient_sauce, ingredient_filling):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        burger.add_ingredient(ingredient_filling)
        receipt = burger.get_receipt()
        assert f'(==== {bun.get_name()} ====)' in receipt
        assert f'= {str(ingredient_sauce.get_type()).lower()} {ingredient_sauce.get_name()} =' in receipt
        assert f'= {str(ingredient_filling.get_type()).lower()} {ingredient_filling.get_name()} =' in receipt
        assert f'Price: {burger.get_price()}' in receipt

    def test_get_receipt_with_mock(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()
        mock_bun.get_name.assert_called()
        mock_ingredient.get_name.assert_called()
        mock_ingredient.get_type.assert_called()
        assert 'Price:' in receipt

    def test_get_receipt_format(self, burger, bun, ingredient_sauce):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_sauce)
        receipt = burger.get_receipt()
        lines = receipt.split('\n')
        assert lines[0] == f'(==== {bun.get_name()} ====)'
        assert lines[1] == f'= {str(ingredient_sauce.get_type()).lower()} {ingredient_sauce.get_name()} ='
        assert lines[2] == f'(==== {bun.get_name()} ====)'
        assert lines[3] == ''
        assert lines[4] == f'Price: {burger.get_price()}'


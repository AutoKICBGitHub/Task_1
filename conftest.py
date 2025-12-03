import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun():
    return Bun("black bun", 100.0)


@pytest.fixture
def ingredient_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)


@pytest.fixture
def ingredient_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100.0)


@pytest.fixture
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_name.return_value = "test bun"
    mock.get_price.return_value = 50.0
    return mock


@pytest.fixture
def mock_ingredient():
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = "test ingredient"
    mock.get_price.return_value = 25.0
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def database():
    return Database()


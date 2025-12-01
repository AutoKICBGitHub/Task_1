from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


BUN_TEST_DATA = [
    ("black bun", 100.0),
    ("white bun", 200.0),
    ("red bun", 300.0),
    ("test bun", 50.5),
]

BUN_NAME_TEST_DATA = [
    ("black bun", 100.0),
    ("white bun", 200.0),
    ("red bun", 300.0),
]

BUN_PRICE_TEST_DATA = [
    ("black bun", 100.0),
    ("white bun", 200.0),
    ("red bun", 300.0),
    ("test bun", 0.0),
    ("test bun", 999.99),
]

INGREDIENT_NAMES = {
    "hot_sauce": "hot sauce",
    "sour_cream": "sour cream",
    "chili_sauce": "chili sauce",
    "cutlet": "cutlet",
    "dinosaur": "dinosaur",
    "sausage": "sausage",
    "sauce1": "sauce1",
    "filling1": "filling1",
    "sauce2": "sauce2",
}

INGREDIENT_PRICES = {
    "hot_sauce": 100.0,
    "sour_cream": 200.0,
    "chili_sauce": 300.0,
    "cutlet": 100.0,
    "dinosaur": 200.0,
    "sausage": 300.0,
    "sauce1": 100.0,
    "filling1": 200.0,
    "sauce2": 300.0,
}

INGREDIENT_INIT_TEST_DATA = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200.0),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100.0),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200.0),
]

INGREDIENT_PRICE_TEST_DATA = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100.0),
]

INGREDIENT_NAME_TEST_DATA = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
    (INGREDIENT_TYPE_SAUCE, "sour cream", 200.0),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100.0),
    (INGREDIENT_TYPE_FILLING, "dinosaur", 200.0),
]

INGREDIENT_TYPE_TEST_DATA = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100.0),
]

BURGER_PRICE_PARAMETRIZED_DATA = [
    ("black bun", 100.0, 0),
    ("white bun", 200.0, 1),
    ("red bun", 300.0, 2),
]

DATABASE_BUNS_DATA = [
    (0, "black bun", 100),
    (1, "white bun", 200),
    (2, "red bun", 300),
]

DATABASE_INGREDIENTS_DATA = [
    (0, INGREDIENT_TYPE_SAUCE, "hot sauce"),
    (1, INGREDIENT_TYPE_SAUCE, "sour cream"),
    (2, INGREDIENT_TYPE_SAUCE, "chili sauce"),
    (3, INGREDIENT_TYPE_FILLING, "cutlet"),
    (4, INGREDIENT_TYPE_FILLING, "dinosaur"),
    (5, INGREDIENT_TYPE_FILLING, "sausage"),
]

DATABASE_INGREDIENTS_PRICES = [100, 200, 300, 100, 200, 300]

MOCK_INGREDIENT_PRICES = {
    "ingredient1": 25.0,
    "ingredient2": 30.0,
}

MOCK_BUN_PRICE = 50.0


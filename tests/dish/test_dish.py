from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    price = 30.00
    dish1 = Dish("dish1", price)
    dish2 = Dish("dish2", price)
    ing_queijo = Ingredient("queijo parmesão")
    mount = 5

    dish1.add_ingredient_dependency(ing_queijo, mount)

    assert hash(dish1) != hash(dish2)
    assert hash(dish2) == hash(Dish("dish2", price))
    assert dish1 == Dish("dish1", price)
    assert repr(dish1) == "Dish('dish1', R$30.00)"
    assert dish1.get_ingredients() == {ing_queijo}
    assert dish1.name == "dish1"
    assert dish1.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE,
    }
    assert dish2.get_restrictions() == set()

    with pytest.raises(TypeError):
        assert Dish("dish3", "30")

    with pytest.raises(ValueError):
        assert Dish("dish3", -30)

    with pytest.raises(ValueError):
        assert Dish("dish4", 0)

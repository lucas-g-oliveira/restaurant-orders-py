from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    queijo = Ingredient("queijo mussarela")
    agua = Ingredient("água")
    frango = Ingredient("frango")

    assert repr(agua) == "Ingredient('água')"
    assert repr(frango) != "Ingredient('água')"
    assert hash(queijo) == hash(Ingredient("queijo mussarela"))
    assert hash(queijo) != hash(Ingredient("queijo parmesão"))
    assert agua.restrictions == set()
    assert Restriction.ANIMAL_MEAT in frango.restrictions
    assert Restriction.ANIMAL_DERIVED in frango.restrictions
    assert frango == Ingredient("frango")
    assert frango.name == 'frango'

import pytest
from ACIT2911.modules.recipe import Recipe  # For local testing
# from modules.recipe import Recipe


@pytest.fixture
def rcp():
    """
    Creates a Recipe instance, has a name, ingredients, and instructions

    Returns:
        obj: Recipe instance
    """
    recipe = Recipe(
        name="A Recipe", ingredients=[], instructions="These are cooking instructions"
    )
    return recipe


def test_recipe(rcp):
    """
    Tests the Recipe class and ensures it has 3 attributes: name(str), ingredients(list), instructions(str)

    Args:
        rcp (obj): Recipe instance
    """
    assert rcp.name == "A Recipe"
    assert isinstance(rcp.ingredients, list) == True
    assert rcp.instructions == "These are cooking instructions"


def test_recipe_errors():
    """
    Checks the Recipe class for errors, ensures that name is a string, ingredients is a list, and instructions is a string
    """
    name, ingr, instr = "Recipe Name", ["apple", "orange"], "instructions"

    with pytest.raises(TypeError):
        recipe = Recipe(12345, ingr, instr)
    with pytest.raises(TypeError):
        recipe = Recipe(name, "not a list", instr)
    with pytest.raises(TypeError):
        recipe = Recipe(name, ingr, ("not instructions", 1234))


def test_recipe_methods(rcp):
    """
    Checks the Recipe class methods
    to_dict - Ensure that it properly translates the class's attributes into dictionary form

    Args:
        rcp (obj): Recipe instance
    """
    assert rcp.to_dict() == {
        "name": "A Recipe",
        "ingredients": [],
        "instructions": "These are cooking instructions",
    }

import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData
from models.dish import Dish

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        data: list[Dish] = self.menu_data.dishes
        result = []
        for d in data:
            if restriction not in d.get_restrictions() or restriction is None:
                temp = {
                    "dish_name": d.name,
                    "ingredients": d.get_ingredients(),
                    "price": d.price,
                    "restrictions": d.get_restrictions(),
                }
                result.append(temp)

        return pd.DataFrame(result)

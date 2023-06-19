from models.dish import Dish
from models.ingredient import Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        data = self._import_file(source_path)
        self.dishes = self._core_process(data)

    def _import_file(self, path: str):
        if path.split(".")[-1] != "csv":
            raise ValueError("Arquivo inválido")
        with open(path, "r") as file:
            return [*csv.DictReader(file)]

    def _core_process(self, dict: list):
        temp = {}

        for iten in dict:
            if iten["dish"] not in temp:
                p = float(iten["price"])
                temp[iten["dish"]] = Dish(iten["dish"], p)
            d: Dish = temp[iten["dish"]]
            i = Ingredient(iten["ingredient"])
            ra = int(iten["recipe_amount"])

            d.add_ingredient_dependency(i, ra)
        return set([temp[i] for i in temp])


ax = MenuData("data/menu_base_data.csv")
print(ax.dishes)

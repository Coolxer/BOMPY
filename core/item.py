import json


class Item:
    def __init__(
        self,
        identifier,
        name,
        quantity=1,
        unit="szt.",
        unit_cost=0,
        sub_parts=[],
    ):
        self.identifier = identifier
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.unit_cost = unit_cost
        self.total_cost = self.quantity * self.unit_cost
        self.sub_parts = sub_parts

    def toJSON(self):
        return json.dumps(
            self, default=lambda o: o.__dict__, sort_keys=False, indent=4
        )

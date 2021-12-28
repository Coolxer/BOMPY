import json


class Item:
    name = ""
    identifier = ""
    quantity = 1
    unit = "szt."
    unit_cost = 0
    total_cost = 0
    sub_parts = None

    def __init__(
        self,
        name,
        identifier,
        quantity=1,
        unit="szt.",
        unit_cost=0,
        sub_parts=[],
    ):
        self.name = name
        self.identifier = identifier
        self.quantity = quantity
        self.unit = unit
        self.unit_cost = unit_cost
        self.total_cost = self.quantity * self.unit_cost
        self.sub_parts = sub_parts

    def toJSON(self):
        return json.dumps(
            self, default=lambda o: o.__dict__, sort_keys=False, indent=4
        )


"""
element = Element("metal", "#0123", 0.5, "kg", 57.59)
el = Element("drozdo", "#asdasdasd")
element2 = Element("nakretka", "#015672", 5, "szt.", 0.50, [element])
element3 = Element("sruba", "#0153472", 3, "szt.", 2.50, [element2, el])


with open("data.json", "w") as outfile:
    outfile.write(element3.toJSON())

# print(element.toJSON())
"""

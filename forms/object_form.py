from config import PALETTE, FONTS
from core.units import UNITS
import core.store as store

from components.text import NormalText
from components.button import Button
from components.input import Input
from components.select import Select

from forms.modal import Modal
from forms.message_box import MessageBox

# klasa reprezentująca formularz obiektu
class ObjectForm(Modal):
    def __init__(self, window, title, size, message, confirm_text):
        super().__init__(
            window=window,
            title=title,
            size=size,
            message=message,
            confirm_text=confirm_text,
            confirm_auto_destroy=False,
            hide_buttons=True,
            lookup=True,
            rows=[0, 1, 2, 3, 4, 5, 6],
            columns=[0, 1, 2, 3],
        )

        self.create_widgets()

    # metoda tworzy poszczególne etykiety i pola interaktywne odnośnie parametrów obiektu
    def create_widgets(self):
        identifier_label = NormalText(
            window=super().get_frame(), text="Identyfikator"
        )
        name_label = NormalText(window=super().get_frame(), text="Nazwa")
        quantity_label = NormalText(window=super().get_frame(), text="Ilość")
        unit_label = NormalText(window=super().get_frame(), text="Jednostka")
        unit_cost_label = NormalText(
            window=super().get_frame(), text="Cena jedn."
        )

        identifier_label.grid(row=1, column=1)
        name_label.grid(row=2, column=1)
        quantity_label.grid(row=3, column=1)
        unit_label.grid(row=4, column=1)
        unit_cost_label.grid(row=5, column=1)

        self.identifier_input = Input(
            window=super().get_frame(),
            input_name="Identyfikator",
            content_type="int",
            min_length=6,
            max_length=6,
        )
        self.name_input = Input(
            window=super().get_frame(),
            input_name="Nazwa",
            content_type="string",
            min_length=3,
            max_length=10,
        )
        self.quantity_input = Input(
            window=super().get_frame(),
            input_name="Ilość",
            content_type="int",
            min_length=1,
            max_length=6,
        )
        self.unit_select = Select(window=super().get_frame(), values=UNITS)
        self.unit_cost_input = Input(
            window=super().get_frame(),
            input_name="Cena jedn.",
            content_type="float",
            min_length=1,
            max_length=9,
        )

        self.identifier_input.grid(row=1, column=2)
        self.name_input.grid(row=2, column=2)
        self.quantity_input.grid(row=3, column=2)
        self.unit_select.grid(row=4, column=2)
        self.unit_cost_input.grid(row=5, column=2)

        super().show_buttons((6, 0), (6, 3))

    # metoda waliduje dane, wywoływana po potwierdzeniu formularza
    def confirm(self, el=None, item=None, result=None):
        identifier_output = self.identifier_input.validate()
        name_output = self.name_input.validate()
        quantity_output = self.quantity_input.validate()
        unit_cost_output = self.unit_cost_input.validate()

        if (
            len(identifier_output)
            or len(name_output)
            or len(quantity_output)
            or len(unit_cost_output)
        ):
            msg = ""
            if len(identifier_output):
                msg = identifier_output
            elif len(name_output):
                msg = name_output
            elif len(quantity_output):
                msg = quantity_output
            else:
                msg = unit_cost_output

            msg_box = MessageBox(
                window=self,
                title="Nieprawidłowe dane",
                size=(700, 150),
                message=msg,
            )
        else:
            print("here")
            self.submit_action(el, item, result)
            super().get_frame().destroy()

    # metoda ustawia dane w poszczególnych polach interaktywnych na starcie
    def init_values(self):
        values = store.instance.get_item()["values"]

        self.identifier_input.insert(0, values[0])
        self.name_input.insert(0, values[1])
        self.quantity_input.insert(0, values[2])
        self.unit_select.set_value(values[3])
        self.unit_cost_input.insert(0, values[4])

    # metoda ustawia akcję potwierdzenia formularza
    def set_submit_action(self, submit_action):
        self.submit_action = submit_action

    # metoda zwraca obiekt z danymi formularza
    def get_form_values(self):
        obj = {
            "identifier": self.identifier_input.get_value(),
            "name": self.name_input.get_value(),
            "quantity": int(self.quantity_input.get_value()),
            "unit": self.unit_select.get_value(),
            "unit_cost": float(self.unit_cost_input.get_value()),
        }

        return obj

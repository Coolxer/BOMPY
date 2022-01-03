from forms.object_form import ObjectForm
import core.store as store

# klasa formularza edytowania elementu
class EditForm(ObjectForm):
    def __init__(self, window):
        super().__init__(
            window=window,
            title="Edytowanie obiektu",
            size=(600, 400),
            message="Edytowanie obiektu",
            confirm_text="Zapisz",
        )

        super().init_values()
        super().set_submit_action(self.submit)

    # metoda edytuje dany element drzewa
    def submit(self, el, item, result):
        it = super().get_form_values()
        el["identifier"] = it["identifier"]
        el["name"] = it["name"]
        el["quantity"] = it["quantity"]
        el["unit"] = it["unit"]
        el["unit_cost"] = it["unit_cost"]

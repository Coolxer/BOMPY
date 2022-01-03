from forms.object_form import ObjectForm
import core.store as store


class EditForm(ObjectForm):
    def __init__(self, window, edit_callback):
        super().__init__(
            window=window,
            title="Edytowanie obiektu",
            size=(600, 400),
            message="Edytowanie obiektu",
            confirm_text="Zapisz",
        )

        self.edit_callback = edit_callback

        super().init_values()
        super().set_accept_action(self.accept)

    def accept(self):
        self.recursive_lookup(store.instance.get_data())
        store.instance.get_file_manager().save()
        self.edit_callback()

    def recursive_lookup(self, item, index=0):
        if (
            "identifier" in item
            and item["identifier"] == store.instance.get_identifier()
        ):
            return index

        index = 0
        for el in item["sub_parts"]:
            result = self.recursive_lookup(el, index)
            if result >= 0:
                it = super().get_form_values()
                el["identifier"] = it["identifier"]
                el["name"] = it["name"]
                el["quantity"] = it["quantity"]
                el["unit"] = it["unit"]
                el["unit_cost"] = it["unit_cost"]
                break

            index += 1

        return -1

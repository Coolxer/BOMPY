from forms.modal import Modal
import core.store as store


class RemoveDialog(Modal):
    def __init__(self, window, remove_callback):
        super().__init__(
            window=window,
            title="Usuwanie obiektu",
            size=(500, 100),
            message="Czy chcesz usunąć ten obiekt?",
            confirm_text="Usuń",
        )

        self.remove_callback = remove_callback

    def confirm(self):
        self.recursive_lookup(store.instance.get_data())
        store.instance.get_file_manager().save()
        self.remove_callback()

    def recursive_lookup(self, item, index=0):
        if (
            "identifier" in item
            and item["identifier"] == store.instance.get_item()
        ):
            return index

        index = 0
        for el in item["sub_parts"]:
            result = self.recursive_lookup(el, index)
            if result >= 0:
                item["sub_parts"].pop(result)
                break

            index += 1

        return -1

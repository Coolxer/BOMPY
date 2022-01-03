from forms.modal import Modal
from components.button import Button
from config import FONTS

# klasa okna informacyjnego typu modalnego
class MessageBox(Modal):
    def __init__(
        self,
        window,
        title,
        size,
        message,
        confirm_callback=None,
        confirm_args=None,
    ):
        super().__init__(
            window=window,
            title=title,
            size=size,
            message=message,
            confirm_text="OK",
            hide_buttons=True,
        )

        self.confirm_callback = confirm_callback
        self.confirm_args = confirm_args

        super().get_buttons()[0].grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
        )

    # metoda wywoływana w celu potwierdzenia i zamknięcia okna
    def confirm(self):
        if self.confirm_callback is not None:
            self.confirm_callback(self.confirm_args)

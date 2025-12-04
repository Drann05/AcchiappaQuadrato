from breezypythongui import EasyFrame, EasyCanvas
from wrappers.easierpythongui import EasierFrame
from acchiappa_quadrato import AcchiappaQuadrato
import os

class UserInput:
    def __init__(self, parent):
        self.parent = parent
        self.widgets = []


        self.BACKGROUND_COLOR = "#1f3d99"
        self.ACCENT_COLOR = "#78E3FD"
        self.GENERAL_FONT = ("Futura", 15, "bold")

        self.parent.setBackground(self.BACKGROUND_COLOR)
        self.parent.grid_init(12, 12)

        self.build_ui()


    def style(self, widget):
        widget["font"] = self.GENERAL_FONT
        widget["foreground"] = self.ACCENT_COLOR
        widget["background"] = self.BACKGROUND_COLOR

    def build_ui(self):
        title = self.parent.addLabel(text="Inserisci un nickname(massimo 10 caratteri)", row=1, column=0, columnspan=12, sticky="NSEW")
        title["foreground"] = "White"
        title["background"] = self.BACKGROUND_COLOR
        title["font"] = ("Arial", 30, "bold")
        self.widgets.append(title)

        self.nickname_field = self.parent.addTextField(text="",row=3,column=4,width=15, columnspan=4, sticky="EW")
        self.nickname_field["font"] = ("Arial", 16)
        self.widgets.append(self.nickname_field)

        btn_start = self.parent.addButton("Start Game", row=4, column=0, columnspan=12, command=self.save_and_start)
        self.style(btn_start)
        self.widgets.append(btn_start)

        self.parent.error_label = self.parent.addLabel(
            text="Messaggio di errore",
            row=5,
            column=4,
            columnspan=6,
        )
        self.parent.error_label["foreground"] = "red"
        self.parent.error_label["background"] = self.BACKGROUND_COLOR
        self.parent.error_label["font"] = ("Arial", 14, "italic")

        self.parent.error_label.grid_remove()

    def save_and_start(self):
        self.parent.username = self.nickname_field.getText()
        is_user_correct=self.check_user_error()
        if is_user_correct:
            self.parent.show_game()

    def check_user_error(self):
        nickname = self.nickname_field.getText().strip()

        if not nickname:
            self.parent.error_label["text"] = "Devi inserire un nome!"
            self.parent.error_label.grid()
            return False

        if len(nickname) > 10:
            self.parent.error_label["text"] = "Il nickname non può superare i 10 caratteri!"
            self.parent.error_label.grid()
            return False
        self.parent.error_label.grid_remove()

        return True








"""Creato da Culotta Sonia, Farina Silvia, Spanò Gioele <3"""
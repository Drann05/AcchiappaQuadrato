from breezypythongui import EasyFrame, EasyCanvas
from wrappers.easierpythongui import EasierFrame
from acchiappa_quadrato import AcchiappaQuadrato
import os

class User_input:
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
        title = self.parent.addLabel("Inserisci un nickname(massimo 10 caratteri)", row=0, column=6, columnspan=2)
        title["foreground"] = "White"
        title["background"] = self.BACKGROUND_COLOR
        title["font"] = ("Arial", 30, "bold")
        self.widgets.append(title)

        nickname_field = self.parent.addTextField(
            text="",
            row=1,
            column=1,
            width=15)
        nickname_field["font"] = ("Arial", 16)

        print(nickname_field.getText())
        self.parent.username = nickname_field.getText()


        btn_start = self.parent.addButton("Start Game", row=4, column=4, columnspan=4, command=self.parent.show_game)
        self.style(btn_start)
        self.widgets.append(btn_start)

        self.parent.error_label.grid_remove()


    def cambia_finestra(self):
        nickname = self.parent.nickname_field.getText().strip()

        if not nickname:
            self.parent.error_label["text"] = "Devi inserire un nome!"
            self.parent.error_label.grid()
            return

        if len(nickname) > 10:
            self.parent.error_label["text"] = "Il nickname non può superare i 10 caratteri!"
            self.parent.error_label.grid()
            return


        self.parent.error_label.grid_remove()

        self.parent.destroy()
        game_window = AcchiappaQuadrato()
        game_window.parent.mainloop()





"""Creato da Culotta Sonia, Farina Silvia, Spanò Gioele <3"""
from breezypythongui import EasyFrame, EasyCanvas
from wrappers.easierpythongui import EasierFrame
from acchiappa_quadrato import AcchiappaQuadrato

class User_input(EasierFrame):
    def __init__(self, title="Acchiappa Quadrato", width=None, height=None, resizable=True):
        super().__init__(self,title,width,height,resizable)

        self.BACKGROUND_COLOR = "#1f3d99"
        self.ACCENT_COLOR = "#78E3FD"
        self.GENERAL_FONT = ("Futura", 15, "bold")
        self.TITLE_FONT = ("Futura", 40, "bold")
        self.BUTTON_FONT = ("Futura", 40, "bold")

        self.setBackground(self.BACKGROUND_COLOR)

        self.titolo = self.addLabel(
            text="Inserisci un nickname:",
            row=0,
            column=0,
            columnspan=12,
            rowspan=2,
            sticky="NSEW"
        ).col_center()

        self.titolo["foreground"] = "White"
        self.titolo["background"] = self.BACKGROUND_COLOR
        self.titolo["font"] = ("Arial", 30, "bold")


        self.label_start = self.addButton(
            text="Start Game",
            row=2,
            column=0,
            command=self.cambia_finestra
        ).col_center()
        self.label_start["font"] = self.GENERAL_FONT
        self.label_start["foreground"] = self.ACCENT_COLOR
        self.label_start["background"] = self.BACKGROUND_COLOR

    def cambia_finestra(self):
        self.destroy()
        game_window = AcchiappaQuadrato()
        game_window.mainloop()


if __name__ == "__main__":
    app = User_input()
    app.mainloop()



"""Creato da Culotta Sonia, Farina Silvia, Spanò Gioele <3"""
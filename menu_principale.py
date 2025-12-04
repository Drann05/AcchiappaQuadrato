from breezypythongui import EasyFrame, EasyCanvas
from wrappers.easierpythongui import EasierFrame
from acchiappa_quadrato import AcchiappaQuadrato
import random
from random import randint

class Menu_principale(EasierFrame):
    def __init__(self, title="Acchiappa Quadrato", width=None, height=None, resizable=True):
        super().__init__(self, title, width, height, resizable)

        self.BACKGROUND_COLOR = "#1f3d99"
        self.ACCENT_COLOR = "#78E3FD"
        self.GENERAL_FONT = ("Futura", 15, "bold")
        self.TITLE_FONT = ("Futura", 40, "bold")
        self.BUTTON_FONT = ("Futura", 40, "bold")

        self.label_start = self.addButton(
            text="Start Game",
            row=11,
            column=0,
            columnspan=2,
            command=self.cambia_finestra
        ).col_center()
        self.label_start["font"] = self.GENERAL_FONT
        self.label_start["foreground"] = self.ACCENT_COLOR
        self.label_start["background"] = self.BACKGROUND_COLOR

        self.setBackground(self.BACKGROUND_COLOR)

        self.label_start = self.addButton(
            text="Rankings",
            row=14,
            column=0,
            columnspan=2,
            command=self.cambia_finestra
        ).col_center()
        self.label_start["font"] = self.GENERAL_FONT
        self.label_start["foreground"] = self.ACCENT_COLOR
        self.label_start["background"] = self.BACKGROUND_COLOR


        self.label_start = self.addButton(
            text="Quit",
            row=16,
            column=0,
            columnspan=2,
            command=self.quit_program
        ).col_center()
        self.label_start["font"] = self.GENERAL_FONT
        self.label_start["foreground"] = self.ACCENT_COLOR
        self.label_start["background"] = self.BACKGROUND_COLOR


        self.titolo = self.addLabel(
            text="MAIN MENU",
            row=0,
            column=0,
            columnspan=12,
            rowspan=2,
            sticky="NSEW"
        ).col_center()



        self.titolo["foreground"] = "White"
        self.titolo["background"] = self.BACKGROUND_COLOR
        self.titolo["font"] = ("Arial", 30, "bold")

    def cambia_finestra(self):
        self.destroy()
        game_window = AcchiappaQuadrato()
        game_window.mainloop()

    def quit_program(self):
        self.quit()

if __name__ == "__main__":
    app = Menu_principale()
    app.mainloop()
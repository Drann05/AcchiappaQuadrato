from breezypythongui import EasyFrame, EasyCanvas
from wrappers.easierpythongui import EasierFrame
from acchiappa_quadrato import AcchiappaQuadrato
from user_input import User_input


class Menu_principale:
    def __init__(self, parent):
        self.parent = parent
        self.widgets=[]


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

        self.grid_init(12, 12)
        self.setSize(1000, 600)
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
        game_window = User_input()
        game_window.mainloop()

    def quit_program(self):
        self.quit()

    def grid_init(self, row, column):
        for r in range(row):
            self.rowconfigure(r, weight=1)
        for c in range(column):
            self.columnconfigure(c, weight=1)

    def build_ui(self):

if __name__ == "__main__":
    app = Menu_principale()
    app.mainloop()
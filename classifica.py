from breezypythongui import EasyFrame, EasyCanvas
from wrappers.easierpythongui import EasierFrame
from acchiappa_quadrato import AcchiappaQuadrato
from menu_iniziale import Menu_principale

class Schermata_classifica(EasierFrame):
    def __init__(self, title="Acchiappa Quadrato", width=None, height=None, resizable=True):
        super().__init__(self, title, width, height, resizable)

        self.widgets=[]

        self.menu()

        self.BACKGROUND_COLOR = "#1f3d99"
        self.ACCENT_COLOR = "#78E3FD"
        self.GENERAL_FONT = ("Futura", 15, "bold")
        self.TITLE_FONT = ("Futura", 40, "bold")
        self.BUTTON_FONT = ("Futura", 40, "bold")

        self.grid_init(12, 12)
        self.setSize(1000, 600)
        self.setBackground(self.BACKGROUND_COLOR)

        self.titolo = self.addLabel(
            text="LEADERBOARD",
            row=0,
            column=0,
            columnspan=12,
            rowspan=2,
            sticky=""
        ).col_center()

        self.titolo["background"] = self.BACKGROUND_COLOR
        self.titolo["foreground"] = self.ACCENT_COLOR
        self.titolo["font"] = ("Arial", 30, "bold")

    def menu(self):
        self.menuBar = self.addMenuBar(row=0, column=0, columnspan=3)
        self.filemenu = self.menuBar.addMenu(text='Gioco')
        self.filemenu.addMenuItem(text='Menù Principale', command=self.go_to_menu)
        self.filemenu.addMenuItem(text="Torna al gioco", command=self.cambia_finestra)
        self.filemenu.addMenuItem(text='Esci', command=self.quit_game)


    def new(self):
        return

    def quit_game(self):
        self.quit()

    def cambia_finestra(self):
        self.destroy()
        game_window = AcchiappaQuadrato()
        game_window.mainloop()

    def go_to_menu(self):
        self.destroy()
        game_window = Menu_principale()
        game_window.mainloop()

    def grid_init(self, row, column):
        for r in range(row):
            self.rowconfigure(r, weight=1)
        for c in range(column):
            self.columnconfigure(c, weight=1)

if __name__ == "__main__":
    app = Schermata_classifica()
    app.mainloop()
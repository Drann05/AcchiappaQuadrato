from breezypythongui import EasyFrame, EasyCanvas
from wrappers.easierpythongui import EasierFrame
from acchiappa_quadrato import AcchiappaQuadrato
from menu_iniziale import Menu_principale

class Schermata_classifica:
    def __init__(self, parent):
        self.parent = parent
        self.widgets = []

        self.BACKGROUND_COLOR = "#1f3d99"
        self.ACCENT_COLOR = "#78E3FD"
        self.GENERAL_FONT = ("Futura", 15, "bold")

        self.parent.setBackground(self.BACKGROUND_COLOR)
        self.parent.grid_init(12, 12)

        self.build_ui()
        self.build_menu()

    def style(self, widget):
        widget["font"] = self.GENERAL_FONT
        widget["foreground"] = self.ACCENT_COLOR
        widget["background"] = self.BACKGROUND_COLOR

    def build_ui(self):
        title = self.parent.addLabel("LEADERBOARD", row=0, column=6, columnspan=2)
        title["foreground"] = "White"
        title["background"] = self.BACKGROUND_COLOR
        title["font"] = ("Arial", 30, "bold")
        self.widgets.append(title)

    def build_menu(self):
        self.menuBar = self.parent.addMenuBar(row=0, column=0, columnspan=3)
        self.filemenu = self.menuBar.addMenu(text='Gioco')
        self.filemenu.addMenuItem(text='Menù Principale', command=self.return_to_menu)
        self.filemenu.addMenuItem(text='Torna al gioco', command=self.go_to_game)
        self.filemenu.addMenuItem(text='Esci', command=self.quit_game)


    def return_to_menu(self):
        self.parent.show_menu()

    def go_to_game(self):
        self.parent.show_game()

    def quit_game(self):
        self.parent.quit()

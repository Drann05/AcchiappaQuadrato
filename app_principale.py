from acchiappa_quadrato import AcchiappaQuadrato
from menu_iniziale import Menu_principale
from user_input import UserInput
from wrappers.easierpythongui import EasierFrame
from breezypythongui import EasyFrame, EasyCanvas
from leaderboard import Leaderboard


class Main_app(EasierFrame):
    def __init__(self, title="Acchiappa Quadrato", width=1000, height=600, resizable=True):
        super().__init__(title=title, width=width, height=height, resizable=resizable)

        self.leaderboard = Leaderboard(self)
        self._my_widgets = []
        self.show_menu()
        self.username = None

    def show_menu(self):
        self.clear()
        self.menu = Menu_principale(self)

    def show_game(self):
        self.clear()
        self.game = AcchiappaQuadrato(self)

    def show_user(self):
        self.clear()
        self.user = UserInput(self)

    def show_leaderboard(self):
        self.clear()
        self.leaderboard = Leaderboard(self)

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = Main_app()
    app.mainloop()


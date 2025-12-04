from acchiappa_quadrato import AcchiappaQuadrato
from menu_iniziale import Menu_principale
from user_input import User_input
from wrappers.easierpythongui import EasierFrame
from breezypythongui import EasyFrame, EasyCanvas
from classifica import Schermata_classifica


class Main_app(EasierFrame):
    def __init__(self, title="Acchiappa Quadrato", width=None, height=None, resizable=True):
        super().__init__(self, title, width, height, resizable)

        self._my_widgets=[]

        self.show_menu()

    def show_menu(self):
        self.clear()
        self.menu = Menu_principale(self)
        self._my_widgets.extend(self.menu.widgets)


    def show_game(self):
        self.clear()
        self.game= AcchiappaQuadrato(self)
        self._my_widgets.extend(self.game.widgets)

    def show_leaderboard(self):
        self.clear()
        self.leaderboard = Schermata_classifica(self)
        self._my_widgets.extend(self.leaderboard.widgets)

    def show_user(self):
        self.clear()
        self.user= User_input(self)
        self._my_widgets.extend(self.user.widgets)

    def clear(self):
        for widget in self._my_widgets:
            widget.destroy()

        self._my_widgets=[]

if __name__ == "__main__":
    app = Main_app()
    app.mainloop()


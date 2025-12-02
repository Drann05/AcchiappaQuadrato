from breezypythongui import EasyFrame, EasyCanvas
from wrappers.gioelepythongui import GioeleFrame
from acchiappa_quadrato import AcchiappaQuadrato
import random
from random import randint

class menu_principale(GioeleFrame):
    def __init__(self, title="Acchiappa Quadrato", width=None, height=None, resizable=True):
        super().__init__(self, title, width, height, resizable)
        self.label_start = self.addButton(
            text="Start Game",
            row=11,
            column=0,
            columnspan=2,
            command=self.cambia_finestra
        ).col_center()

    def cambia_finestra(self):
        self.destroy()
        game_window = AcchiappaQuadrato()
        game_window.mainloop()

if __name__ == "__main__":
    app = menu_principale()
    app.mainloop()
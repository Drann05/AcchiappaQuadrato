from breezypythongui import EasyFrame, EasyCanvas
from wrappers.gioelepythongui import GioeleFrame
from random import randint


class AcchiappaQuadrato(GioeleFrame):
    def __init__(self, title="Acchiappa Quadrato", width=None, height=None, resizable=True):
        super().__init__(self, title, width, height, resizable)

        # --- Colori e Font ---
        self.BACKGROUND_COLOR = "#1A1A3C"
        self.ACCENT_COLOR = "#00FFFF"
        self.SQUARE_COLOR = "pink"
        self.GENERAL_FONT = ("Courier New", 15, "bold")
        self.TITLE_FONT = ("Arial", 40, "bold")
        self.BUTTON_FONT = ("Arial", 40, "bold")

        # --- Variabili di Gioco ---
        self.score = 0
        self.starting_time = 60
        self.clicks_counter = 0
        self.time_left = self.starting_time
        self.starting_percentage = 100
        self.percentage = self.starting_percentage
        self.game_started = False

        self.grid_init(12, 12)
        self.setSize(1000, 600)
        self.setBackground(self.BACKGROUND_COLOR)

        # --- Titolo ---
        self.titolo = self.addLabel(
            text="Acchiappa Quadrato",
            row=0,
            column=0,
            columnspan=12,
            rowspan=2,
            sticky="NSEW"
        ).col_center()

        self.titolo["background"] = self.BACKGROUND_COLOR
        self.titolo["foreground"] = self.ACCENT_COLOR
        self.titolo["font"] = ("Arial", 30, "bold")

        # --- Riquadro di Gioco ---
        self.box = self.addPanel(
            row=2,
            column=1,
            columnspan=8,
            rowspan=8,
            background=self.BACKGROUND_COLOR
        ).col_center()
        self.box["relief"] = "flat"

        self.square = Square(self.box, self, background='white', square_color=self.SQUARE_COLOR)
        self.square.pack(fill="both", expand=True)

        # --- Statistiche e Timer ---
        self.label_score = self.addLabel(text=f"Score: {self.score}", row=10, column=1, columnspan=3, sticky="EW")
        self.label_score["font"] = self.GENERAL_FONT
        self.label_score["foreground"] = self.ACCENT_COLOR
        self.label_score["background"] = self.BACKGROUND_COLOR

        self.label_percentage = self.addLabel(text=f"Percentage: {self.percentage}%", row=10, column=5, columnspan=2,
                                              sticky="EW")
        self.label_percentage["font"] = self.GENERAL_FONT
        self.label_percentage["foreground"] = self.ACCENT_COLOR
        self.label_percentage["background"] = self.BACKGROUND_COLOR

        self.label_timer = self.addLabel(text=f"Time: {self.time_left}", row=10, column=8, columnspan=3, sticky="EW")
        self.label_timer["font"] = self.GENERAL_FONT
        self.label_timer["foreground"] = self.ACCENT_COLOR
        self.label_timer["background"] = self.BACKGROUND_COLOR

        # Pulsanti Start/End (condividono le stesse coordinate)

        # 1. START (Visibile all'inizio)
        self.label_start = self.addButton(
            text="Start Game",
            row=11,
            column=0,
            columnspan=2,
            command=self.start_game
        ).col_center()
        self.label_start["font"] = self.GENERAL_FONT
        self.label_start["foreground"] = self.ACCENT_COLOR
        self.label_start["background"] = self.BACKGROUND_COLOR

        # 2. END (Nascosto all'inizio)
        self.label_end = self.addButton(
            text="End Game",
            row=11,
            column=0,
            columnspan=2,
            command=self.end_game
        ).col_center()
        self.label_end["font"] = self.GENERAL_FONT
        self.label_end["foreground"] = self.ACCENT_COLOR
        self.label_end["background"] = self.BACKGROUND_COLOR

        self.label_end.grid_remove()

    def update_score(self):
        self.score += 1
        self.label_score["text"] = f"Score: {self.score}"

    def reset_game(self):
        self.score = 0
        self.percentage = self.starting_percentage
        self.time_left = self.starting_time
        self.clicks_counter = 0
        self.label_score["text"] = f"Score: {self.score}"
        self.label_timer["text"] = f"Time: {self.time_left}"
        self.label_percentage["text"] = f"Percentage: {self.starting_percentage}%"
        self.square.delete_all()

    def start_game(self):
        self.reset_game()
        self.game_started = True

        self.label_start.grid_remove()
        self.label_end.grid()

        self.square.start_square()
        self.start_timer()

    def end_game(self):
        self.game_started = False
        self.reset_game()

        self.label_end.grid_remove()
        self.label_start.grid()
        self.square.grid_remove()

    def start_timer(self):
        if self.game_started and self.time_left > 0:
            self.time_left -= 1
            self.label_timer["text"] = f"Time: {self.time_left}"
            self.after(1000, self.start_timer)
            if self.time_left == 0:
                self.game_started = False

    def calculate_percentage(self):
        if self.clicks_counter > 0:
            self.percentage = int(self.score * 100 / self.clicks_counter)
            self.label_percentage["text"] = f"Percentage: {self.percentage}%"
        else:
            self.label_percentage["text"] = "Percentage: 100%"

    def grid_init(self, row, column):
        for r in range(row):
            self.rowconfigure(r, weight=1)
        for c in range(column):
            self.columnconfigure(c, weight=1)


class Square(EasyCanvas):
    def __init__(self, parent, game, width=0, height=0, background='white', square_color='red'):
        super().__init__(parent, width, height, background)
        self._game = game
        self._square_color = square_color
        self.q = None
        self.max_side = 100
        self._change = False

    def start_square(self):
        self.update()

    def update(self):

        canvas_width = self.winfo_width()
        canvas_height = self.winfo_height()

        x0 = randint(0, max(0, canvas_width - self.max_side))
        y0 = randint(0, max(0, canvas_height - self.max_side))
        side = randint(20, self.max_side)
        x1 = x0 + side
        y1 = y0 + side

        if self.q:
            self.delete(self.q)
        self.q = self.drawRectangle(
            x0=x0,
            y0=y0,
            x1=x1,
            y1=y1,
            fill=self._square_color)

        self.bind("<Button-1>", self.manage_click)  # Click generale, su tutto il canvas
        self.tag_bind(self.q, "<Button-1>", self.clicked_square)  # Click sul quadrato

    def manage_click(self, event):
        if self._game.game_started:
            self._game.clicks_counter += 1
            self._game.calculate_percentage()
        # elements_clicked = self.find_overlapping(event.x, event.y, event.x, event.y)
        '''
        if self.q in elements_clicked:
            pass
        else:
            self.missed_square()
        '''

    # def missed_square(self):

    def test_function(self):
        print("Test function")
        return True

    def clicked_square(self, event):
        if self._game.game_started:
            self.update()
            self._game.update_score()

    def delete_all(self):
        if self.q:
            self.delete(self.q)


if __name__ == "__main__":
    app = AcchiappaQuadrato()
    app.mainloop()
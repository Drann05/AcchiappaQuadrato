from breezypythongui import EasyFrame, EasyCanvas
from wrappers.easierpythongui import EasierFrame
import random
from random import randint
from classifica import Classifica
import os


class AcchiappaQuadrato(EasierFrame):
    def __init__(self, title="Acchiappa Quadrato", width=None, height=None, resizable=True):
        super().__init__(self, title, width, height, resizable)

        if not os.path.exists("leaderboard.txt"):
            self.create_leaderboard()

        self.menu()

        self.username = "Gioele"

        # --- Colori e Font ---
        self.BACKGROUND_COLOR = "#1f3d99"
        self.ACCENT_COLOR = "#78E3FD"
        self.GENERAL_FONT = ("Futura", 15, "bold")
        self.TITLE_FONT = ("Futura", 40, "bold")
        self.BUTTON_FONT = ("Futura", 40, "bold")

        # --- Variabili velocità Quadrato ---
        self.STARTING_SQUARE_DELAY = 1000
        self.SQUARE_SPEED_INCREMENT = 20
        self.SPEED_INCREASE_INTERVAL = 5000

        self.square_delay_ms = self.STARTING_SQUARE_DELAY

        # --- Variabili di Gioco ---
        self.score = 0
        self.starting_time = 5
        self.clicks_counter = 0
        self.time_left = self.starting_time
        self.starting_percentage = 100
        self.percentage = self.starting_percentage
        self.game_started = False
        self.leaderboard = {}

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
            sticky=""
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

        self.square = Square(self.box, self, background='white')
        self.square.pack(fill="both", expand=True)

        # --- Statistiche e Timer ---
        self.label_score = self.addLabel(text=f"Score: {self.score}", row=10, column=1, columnspan=3, sticky="EW")
        self.label_score["font"] = self.GENERAL_FONT
        self.label_score["foreground"] = self.ACCENT_COLOR
        self.label_score["background"] = self.BACKGROUND_COLOR

        self.label_percentage = self.addLabel(text=f"Accuracy: {self.percentage}%", row=10, column=5, columnspan=2,
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

    def menu(self):
        self.menuBar = self.addMenuBar(row=0, column=0, columnspan=3)
        self.filemenu = self.menuBar.addMenu(text='Gioco')
        self.filemenu.addMenuItem(text='Nuova partita', command=self.new)
        self.filemenu.addMenuItem(text='Esci', command=self.new)
        self.filemenu = self.menuBar.addMenu(text='Classifica')
        self.filemenu.addMenuItem(text='Mostra classifica', command=self.new)
        self.filemenu.addMenuItem(text='Salva', command=self.save_score)

    def new(self):
        return

    def load_leaderboard(self):
        with open("leaderboard.txt", "r") as f:
            content = f.read()
        start = content.find("{")
        end = content.rfind("}") + 1

        dict_text = content[start:end]

        self.leaderboard = eval(dict_text)
    def create_leaderboard(self):
        with open("leaderboard.txt", "w") as f:
            f.write("leaderboard: {\n}")

    def save_score(self):
        self.leaderboard[f"{self.username}"] = self.final_score
        with open("leaderboard.txt", "r") as f:
            content = f.readlines()
        content = content[:-1]

        content.append(f"\t{self.username}: {self.final_score},\n")
        content.append("}")
        with open("leaderboard.txt", "w") as f:
            f.writelines(content)



    def show_leaderboard(self):
        Classifica(self).activate()

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
        self.label_percentage["text"] = f"Accuracy: {self.starting_percentage}%"
        self.square.delete_all()

    def start_game(self):
        self.reset_game()
        self.game_started = True

        self.label_start.grid_remove()
        self.label_end.grid()

        self.square.start_square()
        self.start_timer()
        self.start_speed_increase()

    def end_game(self):

        self.game_started = False

        if self.speed_timer_id:
            self.after_cancel(self.speed_timer_id)
            self.speed_timer_id = None

        self.final_score = self.score
        final_percentage = self.percentage

        self.reset_game()

        self.label_end.grid_remove()
        self.label_start.grid()
        self.square.grid_remove()

        self.messageBox(
            title="Game Over!",
            message=f"Il tuo punteggio finale è: {self.final_score}\nPrecisione: {final_percentage}%"
        )

        print(self.leaderboard)

    def start_timer(self):
        if self.game_started and self.time_left > 0:
            self.time_left -= 1
            self.label_timer["text"] = f"Time: {self.time_left}"
            self.after(1000, self.start_timer)
            if self.time_left == 0:
                self.end_game()

    def start_speed_increase(self):
        if self.game_started:
            self.speed_timer_id = self.after(self.SPEED_INCREASE_INTERVAL, self.increase_speed_action)


    def increase_speed_action(self):
        if self.game_started:
            new_delay = self.square_delay_ms - self.SQUARE_SPEED_INCREMENT
            self.square_delay_ms = new_delay
            print(new_delay)

            self.speed_timer_id = self.after(self.SPEED_INCREASE_INTERVAL, self.increase_speed_action)


    def calculate_percentage(self):
        if self.clicks_counter > 0:
            self.percentage = int(self.score * 100 / self.clicks_counter)
            self.label_percentage["text"] = f"Accuracy: {self.percentage}%"
        else:
            self.label_percentage["text"] = "Accuracy: 100%"

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

        self._COLOR_OPTIONS = [
            "red",
            "green",
            "blue",
            "orange",
            "purple",
            "yellow",
            "cyan",
            "magenta"
        ]

    def start_square(self):
        self.update()
        self.run_square_loop()

    def run_square_loop(self):
        if self._game.game_started:
            self.update()
            current_delay = self._game.square_delay_ms
            self.current_delay_id = self.after(current_delay, self.run_square_loop)

    def stop_square(self):
        if self.current_delay_id:
            self.after_cancel(self.current_delay_id)
            self.current_delay_id = None
        self.delete_all()

    def update(self):

        canvas_width = self.winfo_width()
        canvas_height = self.winfo_height()

        x0 = randint(0, max(0, canvas_width - self.max_side))
        y0 = randint(0, max(0, canvas_height - self.max_side))
        side = randint(20, self.max_side)
        x1 = x0 + side
        y1 = y0 + side

        random_color = random.choice(self._COLOR_OPTIONS)

        if self.q:
            self.delete(self.q)
        self.q = self.drawRectangle(
            x0=x0,
            y0=y0,
            x1=x1,
            y1=y1,
            fill=random_color)

        self.bind("<Button-1>", self.manage_click)  # Click generale, su tutto il canvas
        self.tag_bind(self.q, "<Button-1>", self.clicked_square)  # Click sul quadrato

    def manage_click(self, event):
        if self._game.game_started:
            self._game.clicks_counter += 1
            self._game.calculate_percentage()

    def clicked_square(self, event):
        if self._game.game_started:
            self.after_cancel(self.current_delay_id)
            self.run_square_loop()
            self._game.update_score()

    def delete_all(self):
        if self.q:
            self.delete(self.q)


if __name__ == "__main__":

    app = AcchiappaQuadrato()
    app.mainloop()

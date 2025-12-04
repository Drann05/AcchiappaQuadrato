from breezypythongui import EasyFrame, EasyCanvas
import os

class Leaderboard:
    def __init__(self, parent, filepath="leaderboard.txt"):
        self.filepath = filepath
        self.scores = self.load_scores()
        self.parent = parent
        self.widgets = []

        self.BACKGROUND_COLOR = "#1f3d99"
        self.ACCENT_COLOR = "#78E3FD"
        self.GENERAL_FONT = ("Futura", 15, "bold")

        self.parent.setBackground(self.BACKGROUND_COLOR)
        self.parent.grid_init(12, 12)

        self.build_ui()
        self.build_menu()

    def load_scores(self):
        scores = {}
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and ":" in line:
                        try:
                            name, score = line.split(":")
                            scores[name.strip()] = int(score.strip())
                        except ValueError:
                            continue
        return scores

    def save_scores(self):
        sorted_items = sorted(self.scores.items(), key=self.sort_by_score, reverse=True)
        with open(self.filepath, "w") as f:
            for name, score in sorted_items:
                f.write(f"{name}: {score}\n")


    def sort_by_score(self, item):
        return item[1]  # sort by score


    def add_score(self, name, score):
        self.scores[name] = score
        self.save_scores()

    # Return the top N players
    def get_top(self, n=10):
        sorted_items = sorted(self.scores.items(), key=self.sort_by_score, reverse=True)
        return sorted_items[:n]


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

        top_players = self.get_top(10)

        start_row = 2

        for i, (name, score) in enumerate(top_players, start=1):
            name_label = self.parent.addLabel(f"{i}. {name}", row=start_row + i - 1, column = 2, columnspan  = 5, sticky = "W")
            score_label = self.parent.addLabel(f"{score}", row=start_row + i - 1, column = 7, columnspan = 3, sticky = "E")

            self.style(name_label)
            self.style(score_label)

            self.widgets.append(name_label)
            self.widgets.append(score_label)

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

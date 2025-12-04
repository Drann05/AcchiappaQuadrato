from breezypythongui import EasyFrame, EasyCanvas


class Menu_principale:
    def __init__(self, parent):
        self.parent = parent
        self.widgets = []

        self.BACKGROUND_COLOR = "#1f3d99"
        self.ACCENT_COLOR = "#78E3FD"
        self.GENERAL_FONT = ("Futura", 15, "bold")

        self.parent.setBackground(self.BACKGROUND_COLOR)
        self.parent.grid_init(12, 12)

        self.build_ui()

    def style(self, widget):
        widget["font"] = self.GENERAL_FONT
        widget["foreground"] = self.ACCENT_COLOR
        widget["background"] = self.BACKGROUND_COLOR

    def build_ui(self):
        title = self.parent.addLabel("MAIN MENU", row=0, column=6, columnspan=2)
        title["foreground"] = "White"
        title["background"] = self.BACKGROUND_COLOR
        title["font"] = ("Arial", 30, "bold")
        self.widgets.append(title)

        btn_start = self.parent.addButton("Start Game", row=4, column=4, columnspan=4, command=self.parent.show_game)
        self.style(btn_start)
        self.widgets.append(btn_start)

        btn_rank = self.parent.addButton("Rankings", row=6, column=4, columnspan=4, command=self.parent.show_leaderboard)
        self.style(btn_rank)
        self.widgets.append(btn_rank)

        btn_quit = self.parent.addButton("Quit", row=8, column=4, columnspan=4, command=self.parent.quit)
        self.style(btn_quit)
        self.widgets.append(btn_quit)

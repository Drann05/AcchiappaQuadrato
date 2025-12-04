from breezypythongui import EasyFrame, EasyCanvas
from wrappers.easierpythongui import EasierFrame
from acchiappa_quadrato import AcchiappaQuadrato
import os

class User_input(EasierFrame):
    def __init__(self, title="Acchiappa Quadrato", width=None, height=None, resizable=True):
        super().__init__(self,title,width,height,resizable)

        self.widgets=[]
        self.username={}
        if not os.path.exists("username.txt"):
            self.create_username()

        self.BACKGROUND_COLOR = "#1f3d99"
        self.ACCENT_COLOR = "#78E3FD"
        self.GENERAL_FONT = ("Futura", 15, "bold")
        self.TITLE_FONT = ("Futura", 40, "bold")
        self.BUTTON_FONT = ("Futura", 40, "bold")

        self.grid_init(12, 12)
        self.setSize(1000, 600)
        self.setBackground(self.BACKGROUND_COLOR)


        self.titolo = self.addLabel(
            text="Inserisci un nickname (max 10 caratteri):",
            row=0,
            column=0,
            columnspan=1,
            sticky="NSEW"
        ).col_center()

        self.titolo["foreground"] = "White"
        self.titolo["background"] = self.BACKGROUND_COLOR
        self.titolo["font"] = ("Arial", 18, "bold")

        self.nickname_field = self.addTextField(
            text="",
            row=1,
            column=0,
            width=15,
        ).col_center()
        self.nickname_field["font"] = ("Arial", 16)

        self.label_start = self.addButton(
            text="Start Game",
            row=10,
            column=0,
            command=self.cambia_finestra
        ).col_center()
        self.label_start["font"] = self.GENERAL_FONT
        self.label_start["foreground"] = self.ACCENT_COLOR
        self.label_start["background"] = self.BACKGROUND_COLOR

        self.error_label = self.addLabel(
            text="Messaggio di errore",
            row=2,
            column=0,
            sticky="NSEW"
        ).col_center()
        self.error_label["foreground"] = "red"
        self.error_label["background"] = self.BACKGROUND_COLOR
        self.error_label["font"] = ("Arial", 14, "italic")

        self.error_label.grid_remove()

    def load_username(self):
        with open("username.txt", "r") as f:
            content = f.read()

        start_index = content.find("{")
        end_index = content.rfind("}") + 1

        if start_index != -1 and end_index != 0:
            dict_text = content[start_index:end_index]
            try:
                self.username = eval(dict_text)
            except Exception as e:
                print(f"Errore nel caricamento di username.txt: {e}")
                self.username = {}
        else:
            self.username = {}

    def create_username(self):
        with open("username.txt", "w") as f:
            f.write("usernames: {\n}")

    def save_username(self):
        with open("username.txt", "w") as f:
            f.write(f"usernames: {self.username}\n")

    def cambia_finestra(self):
        nickname = self.nickname_field.getText().strip()

        if not nickname:
            self.error_label["text"] = "Devi inserire un nome!"
            self.error_label.grid()
            return

        if len(nickname) > 10:
            self.error_label["text"] = "Il nickname non può superare i 10 caratteri!"
            self.error_label.grid()
            return


        self.error_label.grid_remove()


        self.load_username()

        if nickname not in self.username:
            self.username[nickname] = 0

        self.save_username()

        self.destroy()
        game_window = AcchiappaQuadrato()
        game_window.mainloop()

    def grid_init(self, row, column):
        for r in range(row):
            self.rowconfigure(r, weight=1)
        for c in range(column):
            self.columnconfigure(c, weight=1)

if __name__ == "__main__":
    app = User_input()
    app.mainloop()



"""Creato da Culotta Sonia, Farina Silvia, Spanò Gioele <3"""
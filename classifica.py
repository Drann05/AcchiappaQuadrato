from breezypythongui import EasyDialog

class Classifica(EasyDialog):
    def __init__(self, parent):
        super().__init__(parent, "Classifica di Gioco")

        classifica_dati = {
            "Gioele": 60,
            "Silvia": 70,
            "Sonia": 80
        }

        # 🏆 Titolo della classifica
        self.addLabel(text="Classifica Migliori Punteggi", row=0, column=0, sticky="N")

        # 📝 Aggiunta dinamica dei dati
        r = 1
        for nome, punteggio in classifica_dati.items():
            # Nota: 'sticky' aiuta nell'allineamento.
            self.addLabel(text=f"{nome}: {punteggio}", row=r, column=0, sticky="W")
            r += 1

        # 🔚 Pulsante per chiudere
        self.addButton(text="OK", row=r + 1, column=0, command=self.destroy)
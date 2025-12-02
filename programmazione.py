class Nodo:

    def __init__(self, valore):
        self.valore = valore
        self.sinistro = None
        self.destro = None

    def add_child(self, valore_figlio):
        if valore_figlio < self.valore:
            self.sinistro = Nodo(valore_figlio)
        else:

            self.destro = Nodo(valore_figlio)

    def __str__(self):
        return str(self.valore)

PRECEDENZE = {
    '<->': 1,
    '->': 2,
    '|': 3,
    '&': 4,
    '~': 5
}
OPERATORI_BINARI = ['<->', '->', '|', '&']
OPERATORI_UNARI = ['~']

class Proposizione:

    def __init__(self, radice=None):
        self.radice = radice

    @classmethod
    def da_stringa(cls, proposizione_str):

        token = Proposizione._tokenizza(proposizione_str)
        if not token:
            return cls()

        stack_nodi = []
        stack_operatori = []

        def applica_operatore():
            op = stack_operatori.pop()
            if op in OPERATORI_BINARI:
                if len(stack_nodi) < 2:
                    raise ValueError(f"Errore di sintassi: operatore binario '{op}' senza abbastanza operandi.")
                destro = stack_nodi.pop()
                sinistro = stack_nodi.pop()
                nuovo_nodo = Nodo(op)
                nuovo_nodo.sinistro = sinistro
                nuovo_nodo.destro = destro
                stack_nodi.append(nuovo_nodo)
            elif op == '~':
                if not stack_nodi:
                    raise ValueError("Errore di sintassi: operatore unario '~' senza operando.")
                destro = stack_nodi.pop()
                nuovo_nodo = Nodo(op)
                nuovo_nodo.destro = destro
                stack_nodi.append(nuovo_nodo)
            else:
                raise ValueError(f"Operatore sconosciuto: {op}")
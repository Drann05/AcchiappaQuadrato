from breezypythongui import EasyFrame, EasyCanvas
from wrappers.gioelepythongui import GioeleFrame
from acchiappa_quadrato import AcchiappaQuadrato
import random
from random import randint


class Classifica(GioeleFrame):
    def __init__(self, title="Acchiappa Quadrato", width=None, height=None, resizable=True):
        super().__init__(self, title, width, height, resizable)

from breezypythongui import EasyFrame
from .widgetwrapper import WidgetWrapper

class EasierFrame (EasyFrame):
    def __getattribute__(self, name):
        if name.startswith("add"):
            original = super().__getattribute__(name)

            def wrapped(*args, **kwargs):
                widget = original(*args, **kwargs)


                return WidgetWrapper(widget, self)
            return wrapped

        return super().__getattribute__(name)

    def grid_init(self, row, column):
        for r in range(row):
            self.rowconfigure(r, weight=1)
        for c in range(column):
            self.columnconfigure(c, weight=1)
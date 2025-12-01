from breezypythongui import EasyFrame
from .widgetwrapper import WidgetWrapper

class GioeleFrame (EasyFrame):
    def __getattribute__(self, name):
        if name.startswith("add"):
            original = super().__getattribute__(name)

            def wrapped(*args, **kwargs):
                widget = original(*args, **kwargs)


                return WidgetWrapper(widget, self)
            return wrapped

        return super().__getattribute__(name)
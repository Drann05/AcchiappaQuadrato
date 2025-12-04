class WidgetWrapper:
    def __init__(self, widget, frame):
        self._widget = widget
        self._frame = frame

    def __getattr__(self, name):
        return getattr(self._widget, name)

    def __setitem__(self, name, value):
        self._widget[name] = value
        return self._widget

    def __getitem__(self):
        return self._widget

    def col_left(self):
        self._widget.grid(column=0)
        return self._widget

    def col_center(self):
        total_cols = self._frame.grid_size()[0]
        colspan = int(self._widget.grid_info().get("columnspan", 1))

        center_col = total_cols // 2 - colspan // 2
        self._widget.grid(column=center_col)

        return self._widget

    def col_right(self):
        total_cols = self._frame.grid_size()[0]
        colspan = int(self._widget.grid_info().get("columnspan", 1))
        right_col = max(0, total_cols - colspan)
        self._widget.grid(column=right_col)
        return self._widget


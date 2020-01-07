import textwrap

class Level:
    """ An AQI Level """
    def __init__(self, index, label, description, rgb, min_aqi, max_aqi):
        self._index = index
        self._label = label
        self._description = textwrap.dedent(description)
        self._rgb = rgb
        self._min_aqi = min_aqi
        self._max_aqi = max_aqi

    @property
    def index(self):
        return self._index

    @property
    def label(self):
        return self._label

    @property
    def description(self):
        return self._description

    @property
    def rgb(self):
        return self._rgb

    @property
    def min_aqi(self):
        return self._min_aqi

    @property
    def max_aqi(self):
        return self._max_aqi

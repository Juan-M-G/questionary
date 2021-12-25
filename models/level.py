class Level:
    def __init__(self, level_number, points):
        self._level_number = level_number
        self._points = points

    
    @property
    def get_level_number(self):
        return self._level_number
    @get_level_number.setter
    def set_level_number(self, level_number):
       self._level_number = level_number

    @property
    def get_points(self):
        return self._points
    @get_points.setter
    def set_points(self, points):
       self._points = points
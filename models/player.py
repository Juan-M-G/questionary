class Player:
    def __init__(self, name, level, score ):
       self._name = name
       self._level = level
       self._score = score

    @property.getter
    def get_name(self):
        return self._name
    @property.setter
    def set_name(self, name):
       self._name = name

    @property.getter
    def get_level(self):
        return self._level
    @property.setter
    def set_level(self, level):
       self._level = level

    @property.getter
    def get_score(self):
        return self._score
    @property.setter
    def set_score(self, score):
       self._score = score
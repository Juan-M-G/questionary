class Player:
    def __init__(self, name, level, score ):
       self._name = name
       self._level = level
       self._score = score

    @property
    def get_name(self):
        return self._name
    @get_name.setter
    def set_name(self, name):
       self._name = name

    @property
    def get_level(self):
        return self._level
    @get_level.setter
    def set_level(self, level):
       self._level = level

    @property
    def get_score(self):
        return self._score
    @get_score.setter
    def set_score(self, score):
       self._score = score
class Level:
    def __init__(self, name, level_number, prize):
        self._name = name
        self._level_number = level_number
        self._prize = prize

    @property.getter
    def get_name(self):
        return self._name
    @property.setter
    def set_name(self, name):
       self._name = name

    @property.getter
    def get_level_number(self):
        return self._level_number
    @property.setter
    def set_level_number(self, level_number):
       self._level_number = level_number

    @property.getter
    def get_prize(self):
        return self._prize
    @property.setter
    def set_prize(self, prize):
       self._prize = prize
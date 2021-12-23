class Prize:
    def __init__(self, name):
        self._name = name
    @property.getter
    def get_name(self):
        return self._name
    @property.setter
    def set_name(self, name):
       self._name = name
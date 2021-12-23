class Question:
    def __init__(self, statement, op1, op2, op3, op4, answer, difficulty):
        self.statement = statement
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.op4 = op4
        self.answer = answer
        self.difficulty = difficulty

    @property.getter
    def get_statement(self):
        return self._statement
    @property.setter
    def set_statement(self, statement):
       self._statement = statement

    @property.getter
    def get_op1(self):
        return self._op1
    @property.setter
    def set_op1(self, op1):
       self._op1 = op1

    @property.getter
    def get_op2(self):
        return self._op2
    @property.setter
    def set_op2(self, op2):
       self._op2 = op2

    @property.getter
    def get_op3(self):
        return self._op3
    @property.setter
    def set_op3(self, op3):
       self._op3 = op3

    @property.getter
    def get_op4(self):
        return self._op4
    @property.setter
    def set_op4(self, op4):
       self._op4 = op4

    @property.getter
    def get_answer(self):
        return self._answer
    @property.setter
    def set_answer(self, answer):
       self._answer = answer

    @property.getter
    def get_difficulty(self):
        return self._difficulty
    @property.setter
    def set_difficulty(self, difficulty):
       self._difficulty = difficulty
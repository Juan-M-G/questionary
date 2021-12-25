from models.category import Category

class Question(Category):
    def __init__(self, statement, op1, op2, op3, op4, answer, difficulty):
        self._statement = statement
        self._op1 = op1
        self._op2 = op2
        self._op3 = op3
        self._op4 = op4
        self._answer = answer
        self._difficulty = difficulty
        super().__init__(name =  "category")

    @property
    def get_statement(self):
        return self._statement
    @get_statement.setter
    def set_statement(self, statement):
       self._statement = statement

    @property
    def get_op1(self):
        return self._op1
    @get_op1.setter
    def set_op1(self, op1):
       self._op1 = op1

    @property
    def get_op2(self):
        return self._op2
    @get_op2.setter
    def set_op2(self, op2):
       self._op2 = op2

    @property
    def get_op3(self):
        return self._op3
    @get_op3.setter
    def set_op3(self, op3):
       self._op3 = op3

    @property
    def get_op4(self):
        return self._op4
    @get_op4.setter
    def set_op4(self, op4):
       self._op4 = op4

    @property
    def get_answer(self):
        return self._answer
    @get_answer.setter
    def set_answer(self, answer):
       self._answer = answer

    @property
    def get_difficulty(self):
        return self._difficulty
    @get_difficulty.setter
    def set_difficulty(self, difficulty):
       self._difficulty = difficulty
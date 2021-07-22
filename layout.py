
class layout:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
        # ._ used to make variable private
        self._score = 0
        self._life = 3
        self.level = 1

    def get_score(self):
        return self._score
    def get_life(self):
        return self._life
    def decrease_life(self):
        self._life -=1
        return self._life
    def increase_life(self):
        self._life +=1
        return self._life
    def increase_score(self,p):
        self._score +=p
        return self._score
    def print_navbar(self):
        str = ""
        str += " SCORE : %s          "%(self._score)
        str += " LIFE : %s         "%(self._life)
        str += " LEVEL : %s         "%(self.level)
        return str


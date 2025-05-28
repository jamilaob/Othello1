"""class Pawn:
    def __init__(self, color):
        self.color = color"""


class Pawn:
    def __init__(self, color="whit"):
        if color in ["white", "black"]:
            self_color = color
        else:
            raise ValueError(f"{color} is not a valid value ase : white, black")
@property
def color(self, color):
    if color in ["white", "black"]:
        self_color = color
    else:
        raise ValueError(f"{color} is not a valid value ase : white, black")
def swapColor(self):
    if self.color == "white" :
        self.color == "black"
    else:
        self.color == "white"
def __repr__(self):
    if self.color == "white" :
        return "0"
    else:
        return "x"
import inspect


class Utils:
    def display(self, item: object) -> None:
        if inspect.ismethod(item.__repr__):
            print(item)
        else:
            print(str(item))

    def __repr__(self):
        return "dasdsa"


class Coordinates:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"


u = Utils()
num = 65
msg = "A string"
c = Coordinates(21.0, 68.0)
u.display(num)
u.display(msg)
u.display(c)

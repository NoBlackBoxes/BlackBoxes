# Token Class
class Token:
    def __init__(self, type, name, value, line):
        self.type = type
        self.name = name
        self.value = value
        self.line = line

    def __repr__(self):
        if self.value is not None:
            return f"{self.line:04d}:Token({self.type}:{self.name}, {repr(self.value)})"
        else:
            return f"{self.line:04d}:Token({self.type}:{self.name})"

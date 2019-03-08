class Direction:
    def __init__(self, l, r, m, c):
        self.left = l
        self.right = r
        self.move = m
        self.char = c

    def __str__(self):
        return self.char


def get_directions():
    return {"S": Direction("E", "W", (0, -1), "S"),
            "N": Direction("W", "E", (0, 1), "N"),
            "E": Direction("N", "S", (1, 0), "E"),
            "W": Direction("S", "N", (-1, 0), "W")}

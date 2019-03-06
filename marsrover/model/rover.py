class Rover:
    def __init__(self, x, y, h):
        self.x = x
        self.y = y
        self.heading = h

    def _move(self, movement):
        # TODO check if move legal (plateau)
        if movement is movement.L:
            pass

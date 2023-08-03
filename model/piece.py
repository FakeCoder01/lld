from model.position import Position

class Piece:
    def __init__(self, name, position:Position):
        self.name = name
        self.position = position
    
    def update_position(self, new_position:Position):
        self.position = new_position


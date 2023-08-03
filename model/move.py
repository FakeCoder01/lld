from model.piece import Piece
from model.position import Position

class DiagonalMove:
    def __init__(self, name:str):
        self.name = name

    def can_move(self, piece:Piece, destination:Position):
        if abs(piece.position.x - destination.x) == abs(piece.position.y - destination.y):
            return True
        return False

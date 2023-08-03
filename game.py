from model.piece import Piece
from model.position import Position
from model.move import DiagonalMove



bishop = Piece(name="Bishop", position=Position(0, 2))
bishop_move = DiagonalMove("Bishop")


while True:
    x, y = map(int, input("Enter : ").split())
    new_position = Position(x, y)
    if bishop_move.can_move(piece=bishop, destination=new_position):
        print("Moved")
        bishop.update_position(new_position=new_position)
    else:
        print("Wrong")

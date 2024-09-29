from gameparts import Board


game = Board()
game.display()
game.make_move(1, 1, '0')
print('Ход сделан!')
game.display()
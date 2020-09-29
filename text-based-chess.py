class Pawn:
	def __init__(self, x, y):
		self.xaxis = x
		self.yaxis = y
	def cord(self):
		cord = [self.xaxis, self.yaxis]
		print(cord)

	def movePawn(self, x, y):
		if x != self.xaxis:
			print("Can't move there")
		else: 
			self.yaxis = y		 
		
pawnTest = Pawn('A', 2)
print(pawnTest.xaxis, pawnTest.yaxis)
pawnTest.cord()
pawnTest.movePawn('A',10)
pawnTest.movePawn('B',2)
pawnTest.cord()
"""
pawn = ['a',1]

print(pawn)
def updatePos(piece, x, y):
	if (x != pawn[0]):
		print("Pawn does not move there")
	if ((turn != 0) and (y == y + 2)):
		print("Pawn can only move up one")
	else: 
		piece[0] = x
		piece[1] = y
	

updatePos(pawn, 'b', 3)
print(pawn)
turn = 4
print("turn = ", turn)
updatePos(pawn, 'a', 4)
print(pawn)

"""
		 

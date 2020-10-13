#Classes and Definitions
letters = ['A','B','C','D','E','F','G','H'] 
numbers = [1,2,3,4,5,6,7,8]

class ChessPiece:
      self.xaxis = x
      self.yaxis = y
      print([self.xaxis,self.yaxis])
	
   def cord(self):
	
   def onBoard(self, x, y):
      if (x in letters) and (y in numbers):
         return True
      else:
         print([x,y],"is not valid")
class Movement(ChessPiece):
   def latMov(self, x, y): 
         self.yaxis = y
         self.cord() 

   #Diagonal movement
   def diagMov(self, x, y):
      if x == self.xaxis or y == self.yaxis:
         return False 
      else:         
         self.xaxis = x
         self.yaxis = y
         self.cord()
   
   def moveRook(self, x, y):
      if self.onBoard(x,y) == True:
class Bishop(Movement):
   def moveBishop(self, x, y):
      else: 
         print("Bishop cannot move to",[x,y]) 

class Queen(Movement): 
   def moveQueen(self, x, y):   
      else:
         self.moveDiag(x,y)

class Pawn(ChessPiece): 
   def movePawn(self, x, y):
      if (x != self.xaxis) or (self.onBoard(x,y) == False):
         print("The pawn can't move there")
      else: 
         self.yaxis = y		 
         self.cord()

def rookTest():
   print("------Rook-----")

rookTest()

def bishopTest():
   print("------Bishop-----")
   bTest.moveBishop('F', 1) 
   bTest.moveBishop('D', 6)
   bTest.moveBishop('A', 8)

   bTest.moveBishop('C', 1) #c












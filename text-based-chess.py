#Classes and Definitions
letters = ['A','B','C','D','E','F','G','H'] 
numbers = [1,2,3,4,5,6,7,8]

class ChessPiece:
   def __init__(self, x, y):
      self.xaxis = x
      self.yaxis = y
      print([self.xaxis,self.yaxis])
	
   def cord(self):
      cord = [self.xaxis, self.yaxis]
      print(cord)
	
   def onBoard(self, x, y):
      if (x in letters) and (y in numbers):
         return True
      else:
         print([x,y],"is not valid")

class Movement(ChessPiece):
   #lateral movement
   def latMov(self, x, y): 
      if x == self.xaxis:
         self.yaxis = y
         self.cord() 
      elif y == self.yaxis:
         self.xaxis = x
         self.cord()

   #Diagonal movement
   def diagMov(self, x, y):
      if x == self.xaxis or y == self.yaxis:
         return False 
      else:         
         self.xaxis = x
         self.yaxis = y
         self.cord()
   
   #check + movement
   def moveDiag(self, x, y):
      if self.onBoard(x,y) == True:
         self.diagMov(x,y)
      else:
         return False
   
   def moveUDLR(self, x, y):
      if self.onBoard(x,y) == True:
         self.latMov(x,y)
      else:
         return False
      
class Rook(Movement):	
   def moveRook(self, x, y):
      if self.onBoard(x,y) == True:
         self.moveUDLR(x,y)
      else:   
         print("Rook cannot move to",[x,y])
 
class Rook_old(Movement):	
   def moveRook(self, x, y):
      if self.moveUDLR(x,y) == True:
         self.moveUDLR(x,y)
      else:   
         print("Rook cannot move to",[x,y])
 
class Bishop(Movement):
   def moveBishop(self, x, y):
      if self.moveDiag(x,y) == True:   
         self.moveDiag(x,y)
      else: 
         print("Bishop cannot move to",[x,y]) 

class Queen(Movement): 
   def moveQueen(self, x, y):   
      if self.moveDiag(x,y) == False:
         print("queen cannot move there")
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
   bTest = Rook('E', 1) 

   bTest.moveRook('E', 2)
   bTest.moveRook('F', 1) 

   bTest.moveRook('D', 2)

   bTest.moveRook('D', 6)
   bTest.moveRook('2', 6)

   bTest.moveRook('H', 6) 
   bTest.moveRook('F', 8) 
   bTest.moveRook('A', 3) 

   bTest.moveRook('A', 8)

   bTest.moveRook('C', 1) 

rookTest()

def bishopTest():
   print("------Bishop-----")
   bTest = Bishop('E', 1) #c

   bTest.moveBishop('E', 2) #did not give me bishop DNMT
   bTest.moveBishop('F', 1) 

   bTest.moveBishop('D', 2) #c

   bTest.moveBishop('D', 6)
   bTest.moveBishop('2', 6) #i get the error but i think i think i get two: the location dne and BDNMT 

   bTest.moveBishop('H', 6) #c
   bTest.moveBishop('F', 8) #c
   bTest.moveBishop('A', 3) #c

   bTest.moveBishop('A', 8)

   bTest.moveBishop('C', 1) #c












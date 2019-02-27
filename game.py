from random import shuffle

class Desk():
	ulist = None
	my_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
	def __init__(self):
		self.ulist = self.my_numbers.copy()
		shuffle(self.ulist)
		
	def get_desk(self):
        	return self.ulist
	
	def set_desk(self,x,y):
		self.ulist[x],self.ulist[y] = self.ulist[y],self.ulist[x]

	def print_desk(self):
        	desk = self.get_desk()
        	for i in range(0,len(desk),4):
                	print( desk[i:i+4])


	def get_zero(self):
		desk = self.get_desk()
		for x in desk:
                	if 0 == desk[x]:
                        	return x
	def check_move(self,move):
		l_bound = [0,4,8,12]
		r_bound = [3,7,11,15]
		u_bound = [0,1,2,3]
		d_bound = [16,15,14,13]
		g_bonds = {'w':[0,1,2,3],'s':[16,15,14,13],'a':[0,4,8,12],'d':[3,7,11,15]}
		if self.get_zero() in g_bonds[move]:
			raise Exception("Dont break game!")
		else:
			self.make_move(move)
	
	def make_move(self,move):
		zero = self.get_zero()
		if move == 'w':
			self.set_desk(zero,zero-4)
		elif move == 's':
			self.set_desk(zero,zero+4)
		elif move == 'a':
			self.set_desk(zero,zero-1)
		elif move == 'd':
			self.set_desk(zero,zero+1)
		else:
			raise Exception("""Game controls - w=up,s=down,a=left,d=right""")	
	
	def check_winner(self):
		if self.my_numbers == self.ulist:
			return False
		else:
			return True
		

game = Desk()

while game.check_winner():
	game.print_desk()
	move = input("Enter your move - w=up,s=down,a=left,d=right: ")
	try:
		game.check_move(move)
	except Exception as e:
		print("Are you going to break game?")




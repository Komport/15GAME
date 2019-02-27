from random import shuffle
from terminaltables import SingleTable


class Desk():
	ulist = None
	my_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15," "]
	def __init__(self):
		self.ulist = self.my_numbers.copy()
		shuffle(self.ulist)
		
	def get_desk(self):
        	return self.ulist
	
	def set_desk(self,x,y):
		self.ulist[x],self.ulist[y] = self.ulist[y],self.ulist[x]

	def print_desk(self):
		desk = self.get_desk()
		t_desk = list()
		for i in range(0,len(desk),4):
			clist = (desk[i:i+4])
			t_desk.append(clist)
		table_instance = SingleTable(t_desk)
		table_instance.outer_border = True
		table_instance.inner_heading_row_border = True
		table_instance.inner_column_border = True
		table_instance.inner_row_border = True
		print(table_instance.table)


	def get_zero(self):
		desk = self.get_desk()
		for x in range (0,len(desk)):
                	if " " == desk[x]:
                        	return x
	def check_move(self,move):
		g_bonds = {'s':[0,1,2,3],'w':[16,15,14,13],'d':[0,4,8,12],'a':[3,7,11,15]}
		if self.get_zero() in g_bonds[move]:
			raise Exception("Dont break game!")
		else:
			self.make_move(move)
	
	def make_move(self,move):
		zero = self.get_zero()
		if move == 'w':
			self.set_desk(zero,zero+4)
		elif move == 's':
			self.set_desk(zero,zero-4)
		elif move == 'a':
			self.set_desk(zero,zero+1)
		elif move == 'd':
			self.set_desk(zero,zero-1)
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




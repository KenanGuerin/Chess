def reset(): # should be able to remplace the pieces by their unicode emojii
	A=['RW','pW',None,None,None,None,'pB','RB']
	B=['NW','pW',None,None,None,None,'pB','NB']
	C=['BW','pW',None,None,None,None,'pB','BB']
	D=['QW','pW',None,None,None,None,'pB','QB']
	E=['KW','pW',None,None,None,None,'pB','KB']
	F=['BW','pW',None,None,None,None,'pB','BB']
	G=['NW','pW',None,None,None,None,'pB','NB']
	H=['RW','pW',None,None,None,None,'pB','RB']
	Board=[A,B,C,D,E,F,G,H]
	return Board

def show(Board):
	print(Board[0])
	print(Board[1])
	print(Board[2])
	print(Board[3])
	print(Board[4])
	print(Board[5])
	print(Board[6])
	print(Board[7])

def winW(Board):
	for i in Board:
		for j in i:
			if j== 'KB':
				return False
	return ("Black as won")
	
def winB(Board):
	for i in Board:
		for j in i:
			if j== 'KW':
				return False
	return (" White as won")

def move(src_col,src_row,dst_col,dst_row):
	global Board
	dst_col[dst_row]=src_col[src_row]
	src_col[src_row]=None
	
def letter(Board):
	global A,B,C,D,E,F,G,H
	A=Board[0]
	B=Board[1]
	C=Board[2]
	D=Board[3]
	E=Board[4]
	F=Board[5]
	G=Board[6]
	H=Board[7]

def tab(A,B,C,D,E,F,G,H):
	global Board
	Board[0]=A
	Board[1]=B
	Board[2]=C
	Board[3]=D
	Board[4]=E
	Board[5]=F
	Board[6]=G
	Board[7]=H
	





Board=reset()
show(Board)
while winB(Board)==False and winW(Board)==False:
	letter(Board)
	src_col=str(input(" Enter the column of the piece you want to move (A-H) "))
	src_row=int(input(" Enter the row of the piece you want to move (1-8) "))-1
	dst_col=(input(" Enter destination column (A-H) "))
	dst_row=int(input(" Enter destination row (1-8) "))-1
	name={'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H}
	move(name[src_col],src_row,	name[dst_col],dst_row)
	tab(A,B,C,D,E,F,G,H)
	show(Board)
	print("")
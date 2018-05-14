ans=set()
def wordBoggle(board, words):
	for y in range(len(board)):
		for x in range(len(board[0])):
			DFSFromPosition(board[y][x],(y,x),set(),board,words)
	return sorted(ans)

def DFSFromPosition(cstr,pos,prev,board,words):
	nprev=set()
	nprev=nprev.union(prev)
	nprev.add(pos)
	d=[-1,0,1]
	for y in d:
		for x in d:
			iy,ix=pos
			iy+=y
			ix+=x
			print(pos,(iy,ix))
			if (0<=ix<len(board[0]) and 0<=iy<len(board)) and ((iy,ix) not in nprev):
				ns=cstr+board[iy][ix]
				print(ns)
				nwords=[]
				for e in words:
					if ns in e:
						if ns==e:
							ans.add(e)
						nwords.append(e)
				if len(nwords)>0:
					DFSFromPosition(ns,(iy,ix),nprev,board,nwords)


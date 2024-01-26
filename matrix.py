def matrix(row,col):
	mat=[]
	if row==2 and col==2:
		for i in range(2):
			join=[]
			for j in range(2):
				join.append(int(input()))
			mat.append(join)
		print("\n")
		for i in range(2):
			for j in range(2):
				print(mat[i][j],end="   ")
			print("\n")
		
		
	
#Division of two integers
n=input("Enter a number")
m=input("Enter another number")
if (type(n)==int or float): 
	if (type(m)==int or float):
		div=(float(n)/float(m))
		print("div=",div)
else:
	print("Error")



# dot product of two vectors	
l=[]
m=[]
s=0
n=int(input("length of vector"))
for i in range(n):
	a=int(input("Enter a num"))
	b=int(input("Enter a num"))
	l.append(a)
	m.append(b)
print("list l=",l)
print("list m=",m)

for i in range(len(l)):
	s=s+l[i]*m[i]
print(s);


		
#det of a matrix... check whether it is a square matrix.if it is, find det.
A=int(input("Enter a number"))
B=int(input("Enter another number"))
matrix=[]
print("Enter the entries row wise")
for i in range (A):
	a=[]
	for j in range (A):
		a.append(a)
	matrix.append(a)
for i in range of (A):
	for j in range(B):
		print(matrix[i][j], end=" ")
	print()
det=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
print("det of matrix=",det)		
	
	
	
	
	
	
	
	

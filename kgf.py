size8=int(input())
ara3=[]
for i in range(size8):
	sur=input()
	sur=list(map(int,sur.split(" ")))
	lit=len(sur)
	for j in range(lit):
		ara3.append(sur[j])
ara3.sort()
print(*ara3,sep=" ")	

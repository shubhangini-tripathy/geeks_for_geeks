def sumterm(nth):
	row = 1
	count = 0
	lst=[]
	for j in range(1, nth+1):
		sublst=[]
		for k in range(1, j+1):
			sublst.append(row)
			sublst.append(row+1)
			row +=2
		lst.append(sublst)

	for l in lst[-1]:
		count = count + l
	return count

test_case = int(input())
for i in range(0, test_case):
	nth = int(input())
	ans = sumterm(nth)
	print(ans)

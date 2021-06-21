sortNum=[2,5,6,1,2,8,33,77,12]

for idx in range(0,len(sortNum)-1):
	for idx2 in range(idx+1,len(sortNum)):
		if sortNum[idx]>sortNum[idx2]:
			temp=sortNum[idx]
			sortNum[idx]=sortNum[idx2]
			sortNum[idx2]=temp
			
		else:
			sortNum[idx]=sortNum[idx]
			sortNum[idx2]=sortNum[idx2]

print(sortNum)


sortNum2=[2,5,6,1,2,8,33,77,12]

for i in range(0,len(sortNum2)-1):
	for j in range(i+1,len(sortNum2)):
		if sortNum2[i]<sortNum2[j]:
			temp=sortNum2[i]
			sortNum2[i]=sortNum2[j]
			sortNum2[j]=temp

		else:
			sortNum2[i]=sortNum2[i]
			sortNum2[j]=sortNum2[j]

print(sortNum2)


sortNum3=[8,56,41,10,1,0,12,23]

for a in range(0,len(sortNum3)-1):
	for b in range(a+1,len(sortNum3)):
		if sortNum3[a]>sortNum3[b]:
			temp=sortNum3[a]
			sortNum3[a]=sortNum3[b]
			sortNum3[b]=temp
		else:
			sortNum3[a]=sortNum3[a]
			sortNum3[b]=sortNum3[b]

print(sortNum3)
print(sortNum3.reverse())

sortNum3.reverse()
print(sortNum3)

'''
reverse는 반환값이 없다. 
단순히 순서를 바꿔주는 역할만 할뿐
따라서 반환값을 얻고싶다면 단순히 reverse만 사용하지말고
reverse적용한 리스트 등을 프린트 시켜줄 것

'''
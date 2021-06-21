'''
input()함수 이용
결과: 4인이상의 이름을 입력하세요.(SB로 구분)
     4인 이상이 아니면->명수를 확인하세요
	 4인 이상이라면-> '이름1 이름2 이름3 이름4' 입력되었습니다.

'''
'''
4인 이상일 경우 len()사용하여 인원수 반환
random.randint() ->1~n
중복없이 반환

*재귀함수 : recursive()나 자신을 반복적으로 호출하는 함수
'''
#nList=[]
import random

nList=[]

def recursive(a):
	if (chk==len(nList)):
		return

	for i in range(a):
		num=random.randint(1,len(name))
		if num not in nList:
			nList.append(num)
		else:
			recursive(chk-len(nList))

while True:
	name=input('\t4인 이상의 이름을 입력하세요\n  (이름은 스페이스바로 구분해주세요) : ').split(' ')
	if len(name)>=4:
		for i in name:
			print(i, end=' ')
		print('')

		chk=len(name)

		nList=[]

		recursive(chk)
		print(nList)


'''
while True:
	nList=[]

	name=input('\t4인 이상의 이름을 입력하세요\n  (이름은 스페이스바로 구분해주세요) : ')

	nameList=name.split(' ')

	if len(nameList)>=4:
		print(name,'입력되었습니다')
		for i in range(0,len(nameList)):
			for j in range(i+1,len(nameList)+1):
				n=random.randint(1,len(nameList))
				if n not in nList:
					nList.append(n)
				else:
					continue
				
					if len(nameList)==len(nList):
						break

				
				print(n,end='    ')

				
		print('\n\n')
'''
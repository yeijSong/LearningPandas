menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 4. 합격생목록 ',' 9. 메뉴종료 ']
menuChk = ['1','2','3','4','9']
itemList = ['ID','필기점수','실기점수','인성점수']
MenuList = ["ID", "필기", "실기" ,"인성","합계","평균","합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85],[12, 75, 84],[57, 75, 84],[36, 86, 87],
      [89, 67, 46],[45, 86, 46],[68, 47, 98]];

dic = {}
deleteIDList = []
idx = 0;
NewScoreList=[]
scoreList=scoreList+NewScoreList


'''
문제1.dic에 idList를 key값, scoreList를 value값으로 할당
문제2.3번을 선택한 경우 dic의 값을 출력

'''


def inputData():
	for a in range(0,len(idList)):
		dic[idList[a]]=scoreList[a]
inputData()

def printlist():
	print('-'*80)
	print(' 학생관리시스템v01')
	print('-'*80)
	for i in range(0,len(menu)):
		print(menu[i],end='   ')
	print()
	print('-'*80)

printlist()

def Mainpg():
	n=int(input(' 번호 입력 : '))
	print()

	if n==9:
		exit('종료합니다')
		print()

	elif n==1:
		print(menu[0])
		ID=input('ID를 입력해주세요 :')
		'''
		delIDcol=[]
		'''
		if ID in idList:
			deleteIDList.append(ID)
			del dic[ID]
			'''
			print(dic)
			
			print(deleteIDList)
			
			delIDcol=delIDcol+deleteIDList
			print(delIDcol)
			'''

		else:
			print('해당 아이디 없음')

	elif n==2:
		print(menu[1])
		print()

		ID=input('ID를 입력해주세요 : ')
		print()

		if ID in dic:
			print('중복 아이디가 있습니다')
		elif ID in deleteIDList:
			print('탈퇴한 회원입니다.\n" 회원 가입 불가 "\n')
		else:
			NewUserList=[]
			NewScoreList=[]
			NewID=input('%d. %s : '%(1,itemList[0]))
			NewUserList.append(NewID)
			for i in range(1,len(itemList)):			
				NewScore=int(input('%d. %s : '%(i+1,itemList[i])))
				NewScoreList.append(NewScore)
			dic[NewID]=NewScoreList
			'''
			print(dic)
			'''

		

	elif n==3:
		print('{0:^60}'.format('학생목록'))
		print()
		for b in range(0,len(MenuList)):
			print(MenuList[b],end='\t')
		print()
		print('-'*60)
		for k in dic.keys():
			print(k,'\t',dic[k][0],'\t',dic[k][1],'\t',dic[k][2],'\t',sum(dic[k]),'\t','%0.2f'%(sum(dic[k])/3),end='\t')
			
			if (sum(dic[k])/3) >= 70:
				print('합격')
			elif (sum(dic[k])/3) < 70:
				print('불합격')
	elif n==4:
		print(menu[3])
		for k in dic.keys():
			if (dic[k][0]+dic[k][1]+dic[k][2])/3 >= 70:
				print(k)
	
	else:
		print('번호를 다시 확인해주세요')
		print()

while True:
	Mainpg()
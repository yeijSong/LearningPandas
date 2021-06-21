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

'''
문제1.dic에 idList를 key값, scoreList를 value값으로 할당
문제2.3번을 선택한 경우 dic의 값을 출력

'''



for a in range(0,len(idList)):
	dic[idList[a]]=scoreList[a]


print('-'*80)
print(' 학생관리시스템v01')
print('-'*80)
for i in range(0,len(menu)):
	print(menu[i],end='   ')
print()
print('-'*80)

while True:
	n=int(input(' 번호 입력:'))

	if n==9:
		print('메뉴를 종료합니다')
		break
	elif n==3:
		print('{0:^60}'.format('학생목록'))
		print()
		for b in range(0,len(MenuList)):
			print(MenuList[b],end='\t')
		print()
		print('-'*60)
		for k in dic.keys():
			print(k,'\t',dic[k][0],'\t',dic[k][1],'\t',dic[k][2],end='')
			print()
			


	elif n in range(0,len(menuChk)):
		print(menu[n-1],'Algorithm Chk')
		
		

	else:
		print('번호를 다시 확인해주세요')
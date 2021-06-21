

menuList=['가위','바위','보','횟수입력','종료']
nList=[1,2,3,4,9]
UserWinList=[]
ComWinList=[]
TieList=[]
UserWin=1
ComWin=-1
Tie=0

def MainPg():
	print('-'*60)
	print()
	for i in range(len(menuList)):
		print('%d. %s'%(nList[i],menuList[i]),end='    ')
	print('\n')

import random

def game():

	nCom=random.randint(1,3)


	if n-nCom==0:
		Tie
		TieList.append(Tie)
		print('게임에서 비겼습니다.')
	elif (n-nCom)%3==2:
		ComWin
		ComWinList.append(ComWin)
		print('Com : %s / User : %s'%(menuList[nCom-1],menuList[n-1]),end='\t')
		print('Com Win! 컴퓨터가 이겼습니다!')
	elif (n-nCom)%3==1:
		UserWin
		UserWinList.append(UserWin)
		print('Com : %s / User : %s'%(menuList[nCom-1],menuList[n-1]),end='\t')
		print('You Win! 당신이 이겼습니다!')

	print()




while True:
	MainPg()
	n=int(input('번호를 선택하세요 : '))

	print()

	if n in range(1,4):
		game()
		print('=> 현재 스코어 %d : %d (컴퓨터 : 당신) 입니다.'%(len(ComWinList),len(UserWinList)))
		print()

	elif n==4:
		num=int(input('게임횟수를 입력하세요 : '))
		print('='*30)
		print('%d회의 게임을 시작합니다'%num)
		print()

		for j in range(num):
			
			n=int(input('번호를 선택하세요 : '))
			game()
		
		print('='*30)
		print()
		print('총 %d회의 게임 중 컴퓨터가 %d회, 당신이 %d회 이겼습니다.'%(num,len(ComWinList),len(UserWinList)))
		print()
		break
	
	elif n==9:
		print('='*60)
		print('총 %d회의 게임 중 컴퓨터가 %d회, 당신이 %d회 이겼습니다.'%(len(UserWinList+ComWinList+TieList),len(ComWinList),len(UserWinList)))
		print()
		print('따라서 최종 스코어 %d : %d (컴퓨터 : 당신)로 '%(len(ComWinList),len(UserWinList)),end='')
		if len(ComWinList)>len(UserWinList):
			print('컴퓨터의 승리입니다')
		elif len(ComWinList)<len(UserWinList):
			print('당신의 승리입니다')
		else:
			print('게임에서 비겼습니다')
		print()
		break

	else:
		print('번호를 다시 확인하세요')
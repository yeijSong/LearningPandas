menuList=['가위','바위','보','횟수입력','종료']
nList=[1,2,3,4,9]
UserWinList=[]
ComWinList=[]
TieList=[]
UserWin=1
ComWin=-1
Tie=0


print('-'*60)
for i in range(len(menuList)):
	print('%d. %s'%(nList[i],menuList[i]),end='    ')
print()

import random

def game():
	
	n=int(input('번호를 선택하세요 : '))
	print()
	nCom=random.randint(1,3)

	if n==1:
		if nCom==1:
			Tie
			TieList.append(Tie)
			print('Com : %s / User : %s'%(menuList[n-1],menuList[n-1]))
			print('게임에서 비겼습니다.')
		elif nCom==2:
			ComWin
			ComWinList.append(ComWin)
			print('Com : %s / User : %s'%(menuList[n],menuList[n-1]))
			print('Com Win! 컴퓨터가 이겼습니다!')
		elif nCom==3:
			UserWin
			UserWinList.append(UserWin)
			print('Com : %s / User : %s'%(menuList[n+1],menuList[n-1]))
			print('You Win! 당신이 이겼습니다!')
		print('-'*30)


	if n==2:
		if nCom==1:
			UserWin
			UserWinList.append(UserWin)
			print('Com : %s / User : %s'%(menuList[n-2],menuList[n-1]))
			print('You Win! 당신이 이겼습니다!')
		elif nCom==2:
			Tie
			TieList.append(Tie)
			print('Com : %s / User : %s'%(menuList[n-1],menuList[n-1]))
			print('게임에서 비겼습니다.')
		elif nCom==3:
			ComWin
			ComWinList.append(ComWin)
			print('Com : %s / User : %s'%(menuList[n],menuList[n-1]))
			print('Com Win! 컴퓨터가 이겼습니다!')
		print('-'*30)


	if n==3:
		if nCom==1:
			ComWin
			ComWinList.append(ComWin)
			print('Com : %s / User : %s'%(menuList[n-3],menuList[n-1]))
			print('Com Win! 컴퓨터가 이겼습니다!')
		elif nCom==2:
			UserWin
			UserWinList.append(UserWin)
			print('Com : %s / User : %s'%(menuList[n-2],menuList[n-1]))
			print('You Win! 당신이 이겼습니다!')
		elif nCom==3:
			Tie
			TieList.append(Tie)
			print('Com : %s / User : %s'%(menuList[n-1],menuList[n-1]))
			print('게임에서 비겼습니다.')
		print('-'*30)



while True:
	n=int(input('번호를 선택하세요 : '))
	print()

	if n==9:
		print('총 %d회의 게임 중 컴퓨터가 %d회, 당신이 %d회 이겼습니다.'%(len(UserWinList+ComWinList+TieList),len(ComWinList),len(UserWinList)))
		print('따라서 최종 스코어 %d : %d (컴퓨터 : 당신)로 '%(len(ComWinList),len(UserWinList)),end='')
		if len(ComWinList)>len(UserWinList):
			print('컴퓨터의 승리입니다')
		elif len(ComWinList)<len(UserWinList):
			print('당신의 승리입니다')
		else:
			print('게임에서 비겼습니다')
		break

	elif n==4:
		num=int(input('게임횟수를 입력하세요 : '))
		print('='*30)
		print('%d회의 게임을 시작합니다'%num)
		print()

		for j in range(num):
			game()
		
		print('총 %d회의 게임 중 컴퓨터가 %d회, 당신이 %d회 이겼습니다.'%(num,len(ComWinList),len(UserWinList)))
		print()

	elif n in range(1,4):
		game()
		print('현재 스코어 %d : %d (컴퓨터 : 당신) 입니다.'%(len(ComWinList),len(UserWinList)))


	else:
		print('번호를 다시 확인하세요')
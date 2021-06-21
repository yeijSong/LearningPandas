'''
# 매개변수에 초기값 미리 설정하기

	say_myself 함수는 3개의 매개변수를 받아서
	마지막 인수인 man이 True이면 남자, False면 여자 출력
	default값이 man이므로 아무 것도 적지 않으면 man으로 인식
'''

def say_myself(name,old,man=True):
	print('나의 이름은 %s입니다.'%name)
	print('나이는 %d살입니다.'%old)

	if man:
		print('남자입니다')
	else:
		print('여자입니다')

say_myself('소나무',27)
print()
say_myself('오렌지',25,False)
print()

'''
say_myself('오렌지',22,man)
이렇게 하면 오류가 뜸
man이 정의되지 않았다고 함
위에서 man을 참으로 정의했기 때문에
참, 거짓으로만 입력해야하는 것으로 보임
'''
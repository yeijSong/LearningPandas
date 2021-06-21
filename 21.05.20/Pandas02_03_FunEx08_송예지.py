'''
### 함수 안에서 선언한 변수의 효력 범위

 # 전역변수(global variable)
	- 함수 외에 선언
	- 모든 함수와 공유
 # 지역변수(local variable)
	- 함수 내에 선언
	- 함수와 생명력을 같이한다.

 # 함수 안에서 사용하는 매개변수는 지역변수이다.

'''

a=1
def vartest(a):
	a=a+1
	print(a)
	print()

vartest(a)
print(a)

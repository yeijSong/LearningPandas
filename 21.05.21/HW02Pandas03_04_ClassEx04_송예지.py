'''
  ## 생성자 ##
  - 함수(매서드)이지만 클래스 이름과 동일한 함수(매서드). 주로 초기화에 사용된다.
  - 아무것도 안써있으면 기본 세팅되어있는 생성자(매개변수X)를 가져온다.
  - 오버로드 : 같은 클래스에 같은 이름의 매서드가 두 개 이상 존재할 때(매개변수의 개수로 구분)
  - 오버라이드 : 상속받은 곳에서 같은 이름의 매서드가 존재하는 경우
'''

class FourCal:
	def __init__(self):
		pass
	def __init__(self,first,second):
		self.first=first
		self.second=second

	def sum(self):
		result=self.first+self.second
		return result
	
	def sub(self):
		result=self.first-self.second
		return result

	def mul(self):
		result=self.first*self.second
		return result

	def div(self):
		result=self.first/self.second
		return result
		
#a=FourCal()

a=FourCal(4,2)


# print(a.sum())
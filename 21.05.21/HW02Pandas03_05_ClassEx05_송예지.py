'''

## 생성자(Constructor) ##
  - 상속 : 일반화된 재사용
  - 주로 초기화에 사용된다.
  - 클래스를 상속하기 위해서는 다음의 형식을 따르면 된다
  - 형식 : class 클래스 이름(상속할 클래스 이름)

'''

class FourCal:

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

class MoreFourCal(FourCal):
	def pow(self,su01):
		result=su01**2
		return result

a=MoreFourCal(4,2)
print(a.pow(5))
print(a.div())
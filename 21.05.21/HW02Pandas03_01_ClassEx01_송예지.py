'''
## 클래스 ##
  - 거푸집(틀), 구조
  - 클래스 내에는 '함수 + 속성(변수)'이 포함된다.
  - 거푸집(클래스)으로부터 생성된 것들을 '객체'라고 한다.
  - 생성자 : 함수이지만 클래스 이름과 동일한 함수. 주로 초기화에 사용된다.

## 클래스 사용 ##
  - 객체 생성 후 사용
  - 사용 형식 : 객체.속성 / 객체.함수 ...
'''

class Fourcal:
	def setdata(self,first,second):
		self.first=first
		self.second=second

a=Fourcal()
a.setdata(4,2)

print(a.first)
print(a.second)
print(type(a))


'''
## 예제 풀이 ##
self는 현재 객체를 의미한다.
first,second는 속성(변수)이다.
클래스는 객체를 생성한 후 사용해야하므로 'a'라는 객체를 생성한 후 사용한다.
클래스의 형식은 객체.속성 / 객체.함수이므로
self.first / a.setdata(4,2)의 형식을 이용했다.
'''
'''
## 함수 ##
  - 재사용
  - 형식 : 함수명()
  - 클래스 안의 함수는 '매소드(매서드)'

## 메서드의 또 다른 호출 방법 ##
  - 클래스를 통해 메서드를 호출하는 것도 가능
  - '클래스 이름.메서드' 형태로 호출할 때는 
    객체 a를 첫 번째 매개변수 self에 꼭 전달해주어야 한다.
  - 반면에 다음처럼 '객체.메서드' 형태로 호출할 때는 
    self를 반드시 생략해서 호출해야 한다
'''

class FourCal:
	def setdata(self,first,second):
		self.first=first
		self.second=second

a=FourCal()

FourCal.setdata(a,2,3)
print(a.first,a.second)
print()

a.setdata(4,5)
print(a.first,a.second)

'''
## 예제풀이 ##
1) 클래스 이름에서 바로 호출할 때에는 클래스 내의 많은 객체들 중
   어떤 객체인지를 지정해야하기 때문에 a,2,3형태로 써야한다. 
2) 처음 배웠던대로 객체.함수로 호출하는 방법이다.

'''

class FourCal:
	def setdata(self,first,second):
		self.first=first
		self.second=second

a=FourCal()

FourCal.setdata(a,2,3)
print(a.first,a.second)
print(a.first*a.second)
print()

a.setdata(4,5)
print(a.first,a.second)
# 현재 메서드 우선!

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

class SafeFourCal(FourCal):
	def div(self):
		if self.second==0:
			return 0
		else:
			return super().div()

a=SafeFourCal(4,2)

print(a.first,'+',a.second,'=',a.sum())
print(a.first,'-',a.second,'=',a.sub())
print(a.first,'X',a.second,'=',a.mul())
print(a.first,'/',a.second,'=',a.div())

'''
## 예제 풀이 ##

class SafeFourCal이 현재의 메서드가 된다.

'''
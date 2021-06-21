'''
# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
1. readline() 함수 이용하기
	- 첫 번째 줄 읽어 출력
2. readlines 함수 사용하기
	- 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 돌려준다.
3. read 함수 사용하기
	- 파일의 내용 전체를 문자열로 돌려준다.
'''


# 2. readlines 함수 사용하기

f=open('파일생성하기 연습.txt','r')
lines=f.readlines()
print(lines)

for line in lines:
	print(line)
f.close()
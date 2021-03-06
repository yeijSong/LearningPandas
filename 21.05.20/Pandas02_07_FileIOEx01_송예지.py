'''
04-3 파일 읽고 쓰기

** 파일 생성하기
형식 ] 파일 객체 = open(경로/ 파일 이름, 파일 열기 모드)

파일열기모드	설명
-------------------------------------------------------
   r		읽기모드 - 파일을 읽기만 할 때 사용
   w		쓰기모드 - 파일에 내용을 쓸 때 사용
   a		추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

파일을 쓰기 모드(w)로 열면 해당 파일이 이미 존재할 경우 원래 있던 내용이 사라지고 덮어쓰기 된다.
해당 파일이 존재하지 않으면 새로운 파일이 생성된다.
f.close() : 파일 객체를 닫아주는 역할
'''

# 파일을 쓰기 모드로 열어 출력값 적기
# 기존 print 대신 파일 객체f의 write함수를 사용

f=open('파일생성하기 연습.txt','w')
for i in range(1,11):
	data='%d번째 줄입니다.\n'%i
	f.write(data)
f.close()
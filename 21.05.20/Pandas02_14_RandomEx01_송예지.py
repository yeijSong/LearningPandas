# 랜덤으로 숫자 불러오기

import random

for i in range(5):
	print('%f'%random.random(),end=' ')

print()

for i in range(5):
	print('%d'%random.randint(1,5),end=' ')

print()


for i in range(5):
	print('%d'%random.randint(0,50),end=' ')

print()

for i in range(5):
	print('%f'%random.random(),end=' ')

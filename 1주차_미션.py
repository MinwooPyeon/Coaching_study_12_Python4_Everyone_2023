# -*- coding: utf-8 -*-
"""1주차 미션

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cZ2IQd62TJGf-zR6or8ffcOW93EE9u4l

📌Q1. 강의 내용에 따르면 '파이썬'과 같은 프로그래밍 언어로 컴퓨터에게 우리가 원하는 일을
           시킬 수 있다고 배웠습니다. 파이썬으로 할 수 있는 일은 어떤 것들이 있고, 나는  그중에서
           무엇을 해보고 싶은지 적어봅시다. [난이도 : ⭐️/5]

파이썬 뿐만이 아니라 프로그래밍 언어는 개인적으로 컴퓨터와 대화하는 수단이라고 생각한다. 지금으로썬 파이썬을 통해 무엇을 해야겠다라는 생각은 없지만 내가 하고자 하는일엔 필요할 것이라고 생각한다. 코칭스터디를 통해 파이썬을 학습하며 진로를 정해야 겠다고 생각하고 있다.

📌Q2. 파이썬 코딩을 하기에 앞서 하드웨어를 이해하는 것이 중요하다고 배웠습니다.
           하드웨어 아키텍쳐에서 CPU와 Main Memory 그리고 Secondary Memory의 역할을
           간단하게 정리하여 봅시다. [난이도 : ⭐️/5]

CPU(중앙연산처리장치) : 하드웨어에서 는 뇌와 같은 기능

Main Memory(메인 메모리) : 정보를 저장하는 장치로써 명령이 저장되어있고 cpu에 필요한 명령을 전달하는 역할, 속도가 매우 빠르지만 전원을끄면 정보가 사라짐.

Secondary Memory(보조 기억장치) : 전원이 꺼져도 지우지 않는 이상 영구적으로 정보를 계속 보관.

📌Q3. 파이썬은 우리의 명령을 이해하지 못했을 때, 친절하게 Error Message 로
           어떤 명령을 이해하지 못했는지 알려줍니다. 이를 보고 코드의 버그를 수정해가는 과정을
           Debugging 이라고 하는데요, 이것은 코딩에 있어서 매우 중요합니다.
           따라서 이번 미션에서는 Error Message 에 대해 이해하는 시간을 가져봅시다.
           [난이도 : ⭐️/5]

SyntaxError
"""

12ab = []
for n in range(1,11):
  if n%2 ==0:
    12ab.append(n)
print(12ab)
# 변수명 에러
# 변수앞에 숫자로 시작

ab= []
for n in range(1,11):
  if n%2 ==0:
    ab.append(n)
print(n)

a = 1
if a < 9
  print("a<9")
  # 문법 오류
  # if문에 : 작성안함

a = 1
if a < 9:
  print("a<9")

"""ValueError"""

a = "공부"
print(int(a))
# 문자형을 정수형으로 변경 불가능

a = 1.23
print(int(a))

list1 = ['a', 'b', 'c', 'd', 'e']
print(list1.index('h'))
# list 내부에 없는 값 불러옴

list1 = ['a', 'b', 'c', 'd', 'e']
print(list1.index('e'))

"""TypeError"""

a = 1 + "1.23"
print(a)
# int와 str 연산 불가능

a = "1"+ "abc"
print(a)

i=0
while i < 11:
    print(i + "회")
    i = i + 1
# int와 str 연산 불가능

i=0
while i < 11:
    print(str(i) + "회")
    i = i + 1

"""IndexError"""

a = [1, 2, 3, 4, 5]
print(a[5])
# 인덱스의 범위 초과

a = [1, 2, 3, 4, 5]
print(a[4])

"""KeyError"""

a = {'A':'1','B':'2'}
print(a['C'])
# 딕셔너리에서 존재하지 않는 키에 접근

a = {'A':'1','B':'2'}
print(a['B'])

"""IndentationError"""

for i in range(5):
print(i)
# 들여쓰기 오류

for i in range(5):
    print(i)

"""📌Q4. 강의에서 나온 미국과 유럽의 엘리베이터 층수를 변환하는 프로그램을 기억하시나요?
           그와 비슷하게 법 개정 전 한국 나이를 미국 나이로 변환하는 프로그램을 코딩해봅시다.
           [난이도 : ⭐️⭐️/5]

hint: 미국 나이는 생일이 지났는지 안지났는지가 중요하죠!

birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
"""

kor_age = int(input("한국 나이 입력 "))
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
if birth == 0:
    print(kor_age-1)
elif birth == -1:
    print(kor_age+birth-1)
else:
    print("0 또는 1을 입력하세요")
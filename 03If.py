# 조건문
# 주어진 상황에 따라 적절한 명령문을 수행하는 문장
# 프로그래밍에서 조건을 판단하여 해당 조건에 맞는 상황을  수행하는데 사용.
# 조건문 작성시 반드시 들어쓰기에 따라 문장을 작성돠게되다.
#if 조건문:
# 수행할문장



#ex1) 총점이 90점보다 크면 '우수'라고 출력
total =85
if total >90:
    print('우수')

age=19
if(age >18 and age <=20):
    print('성년을  축하한다')



print('-=만 나이 계산 프로그램 =-')
print('이름,생년,월일 순으로 입력하세요')
name = input('이름 : ')
byear = int(input('생년: '))
bdate = input('월일 : ')

from datetime import datetime
year =  datetime.today().year
date = str(datetime.today().month) + \
    str(datetime.today().day)
age = year - byear

if date < bdate :
    age = age-1
print("%s님의 만 나이는 %d 입니다." %(name,age))

# 18
isMarried = input('결혼 여부를 입력하세요(Y/N)')
salary = int(input('연봉을 입력하세요(만 단위)'))
tax = 0

if isMarried.upper() == 'N':
    if salary < 3000:
        tax = salary * 0.1
    else:
        tax = salary * 0.25

elif isMarried.upper() == 'Y':
    if salary < 6000:
        tax = salary * 0.1
    else:
        tax = salary * 0.25

#else:
#   print('지시한 대로 입력해라 짜샤!')
1
#print('당신이 납부해야 하는 세금은', salary / 25, '만원입니다')
print(isMarried, salary, tax)

# 19 윤년 계산
year = int(input('윤년 여부를 알고 싶은 해를 입력하세요'))

if ((year % 4 == 0 and year / 100 != 0) or (year % 400 == 0)):
    print('%d년은 윤년입니다' % year)
else:
    print('%d년은 윤년이 아닙니다' % year)

# 20

import random
print('---------')
print('행운의 로또')
print('---------')

lotto = str(random.randint(100, 999))
lucky = input('복권 숫자 3자리를 입력하세요')
match = 0

if (lotto[0] == lucky[0] or
    lotto[0] == lucky[1] or
    lotto[0] == lucky[2]):
    match += 1

if (lotto[1] == lucky[0] or
    lotto[1] == lucky[1] or
    lotto[1] == lucky[2]):
    match += 1

if (lotto[2] == lucky[0] or
    lotto[2] == lucky[1] or
    lotto[2] == lucky[2]):
    match += 1

print(lotto, lucky, match)

if match == 3:
    print("모두 일치! 상금 백만 원!")
elif match == 2:
    print("2개 일치! 상금 만 원!")
elif match == 1:
    print("1개 일치! 상금 천 원!")
else:
    print("꽝!")

#21
# 숫자만 입력받기
# 문자 - ASCII 코드값: ord()
# ASCII 코드값 - 문자 : chr()
# 0: ASCII - 48, 9: ASCII - 57
dan = input('출력할 단을 입력하세요')
if ord(dan[0]) >= ord('0') \
        and ord(dan[0]) <= ord('9'):
        dan = int(dan)
        for i in range(1, 10):
            print('%d x %d = %d' % (dan, i, dan * i))
else:
    print("잘못 입력하셨습니다!")

#22
lower = input('소문자를 입력하세요')

if ord(lower[0]) >= ord('a') and ord(lower[0]) <= ord('z'):
    print(lower.upper())
else:
    print('소문자만 입력가능')

#23
import random
print('숫자 맞추기 게임')
num2 = random.randint(1,100)

while True:
    num1 = int(input('1-100 사이의 숫자를 입력하세요'))
    if num1 == num2:
        print("빙고! 숫자를 맞췄습니다")
        break
    elif num1 > num2:
        print('입력한 숫자가 더 큽니다')
    else:
        print('입력한 숫자가 더 작습니다')
print('게임 클리어')

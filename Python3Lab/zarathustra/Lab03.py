# 지금까지의 예제를 함수로 작성

#이름 짓기(되도록 소문자로)
# 파스칼 표기법: 첫 낱말을 대문자로 시작하는 작명(주로 클래스에 이용)
# ex) Employeesm, Departments
#     RegisterEmployees, JoinMember
# 카멜(낙타) 표기법: 첫 낱말을 소문자로 시작하는 작명
# ex) registerEmployees, joinMember
# 스네이크(뱀) 표기법: 소문자와 _ 기호를 이용하는 작명(주로 함수나 변수에 이용)
# ex) register_employees, join_member
# 헝가리언 표기법: 자료형을 의미하는 접두사를 이용하는 작명(특별한 경우가 아니면 쓰이지 않음)
# ex) strName, isMarried, boolMarried

import random

# QnA8
def compareRoom(width, height, price):
    return (width * height) / price

roomA = compareRoom(2.5, 3, 27)
roomB = compareRoom(4, 2, 30)

if (roomA > roomB):
    print('방A가 더 낫네요')
else:
    print('방B가 더 낫네요')


# QnA10
# constant capital, variable capital, surplus value
def computeProfit():
    c = int(input('불변자본을 입력하세요'))
    v = int(input('가변자본을 입력하세요'))
    s = int(input('잉여가치액을 입력하세요'))
    return s / (c /+ v)
print('이윤율:', computeProfit())

# QnA11
def getExchangeRate(country):
    rate = 0
    if country == 'us':
        rate = 1071
    elif country == 'euro':
        rate = 1309
    return rate

buyUS = 780 * getExchangeRate('us')
buyEU = 650 * getExchangeRate('euro')

if buyUS > buyEU:
    print('유로로 사는 게 더 싸네요')
elif buyUS < buyEU:
    print('달러로 사는 게 더 싸네요')

# QnA12
def howManyRun(radius):
    pi = 3.14
    return radius * pi

studentA = howManyRun(100)
studentB = howManyRun(95)

print('학생A는 학생B보다 %dM 더 달렸다' % (studentA - studentB))

# QnA17
def intcalu():
    num1 = int(input('좌변값을 입력하세요'))
    num2 = int(input('우변값을 입력하세요'))
    fmt = "%d + %d = %d\n%d - %d = %d\n"
    fmt += "%d * %d = %d\n%d / %d = %.5f\n"
    fmt += "%d ** %d = %d"
    print(fmt%(num1, num2, num1 + num2,\
               num1, num2, num1 - num2,\
               num1, num2, num1 * num2,\
               num1, num2, num1 / num2,\
               num1, num2, num1 ** num2))
intcalu()

# QnA18
def computeTax():
    salary = int(input('연봉을 입력하세요(만 단위)'))
    isMarried = input('결혼 여부를 입력하세요(Y/N)')
    tax = 0

    if isMarried == 'N':
        if salary < 3000:
            tax = salary * 0.1
        else:
            tax = salary * 0.25
        isMarried = "아니오"

    if isMarried == 'Y':
        if salary < 6000:
            tax = salary * 0.1
        else:
            tax = salary * 0.25
        isMarried = "예"
    else:
        print('제대로 입력하세요')

    fmt = "연봉: %d, 결혼여부: %s, 세금: %1f"
    print(fmt % (salary, isMarried , tax))

computeTax()

#QnA19 윤년 계산
def isLeapYear():
    year = int(input('윤년 여부를 알고 싶은 해를 입력하세요'))
    isLeap = '윤년이 아닙니다'

    if ((year % 4 == 0 and year / 100 != 0) or (year % 400 == 0)):

        isLeap = '윤년입니다'

    print("%d년은 %s" % (year, isLeap))

isLeapYear()

# QnA20
print('---------')
print('행운의 로또')
print('---------')

def rouletteLotto():
    lotto = str(random.randint(100, 999))
    lucky = input('복권 숫자 3자리를 입력하세요')
    match = 0   #일치 여부
    prize = "꽝!"

    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            if (lucky[i] == lotto[j]):
               match += 1

    if match == 3: prize = '1등 당첨! 삼금 백만 원!'
    elif match == 2: prize = '2개 일치! 상금 만 원!'
    elif match == 1: prize = '1개 일치! 상금 천 원!'

    print(lucky, lotto, prize)

rouletteLotto()
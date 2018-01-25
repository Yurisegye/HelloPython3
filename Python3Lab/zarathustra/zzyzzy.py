import random

# 계산기
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

# 윤년 여부
def isLeapYear():
    year = int(input('윤년 여부를 알고 싶은 해를 입력하세요'))
    isLeap = '윤년이 아닙니다'

    if ((year % 4 == 0 and year / 100 != 0) or (year % 400 == 0)):

        isLeap = '윤년입니다'

    print("%d년은 %s" % (year, isLeap))

# 복권 발행
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

# 성적 데이터 클래스
class SungJukVO:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

# 성적 처리용 클래스
class SungJukService:
    def getTotal(self, sj):
        tot = sj.kor + sj.eng + sj.mat
        return tot

    def getAverage(self, sj):
        avg = self.getTotal(sj) / 3
        return avg

    def getGrade(self, sj):
        grdlist = '가가가가가가미양우수수'
        var = int(self.getAverage(sj)/10)
        grd = grdlist[var]
        return grd
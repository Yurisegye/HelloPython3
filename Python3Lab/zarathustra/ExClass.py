# 클래스
# 변수와 그것과 관련된 한수를 하나의 이름으로 정의한 것
# 클래스는 메서드, 속성, 클래스변수, 인스턴스변수로 구성
# 더불어 생성자와 소멸자 등의 멤버도 있다.

# 클래스 정의
# class 이름:
#   클래스 변수
#   생성자
#   함수 정의(메서드)

# 파이썬에서는 생성자나 메서드 정의시
# 암시적으로 첫번째 매개 변수가 self로 지정되어 있다
# self는 항상 객체 자기 자신을 가리키는 의미로 사용한다

# 클래스의 멤버변수는 생성자를 통해서 정의
# 파이썬에서는 객체로 생성한 후에도 멤버 변수를 추가할 수 있다(비추)

class HelloPython:
    def sayhello(self):
        print('Hello, World!')

print(HelloPython)
print(type(HelloPython))

#HelloPython.sayhello()
py = HelloPython()
py.sayhello()

class Animal:
    type = '짐승' # 클래스 수준 변수

    def __init__(self, name, age): # 객체 자신을 가리키는 의미로써 self 사용
        self.name = name
        self.age = age

    def eat(self):
        print('먹는다, 우적우적!')

# 객체 선언 및 사용
# tiger = Animal()
tiger = Animal('', 0)
tiger.eat()         # 메서드 호출
print(tiger.type)   # 인스턴스 변수
print(Animal.type)  # 클래스 변수 (다른 클래스와 공유)

tiger.name = '호랑이'  # 생성자를 통해 정의한 인스턴스 변수들
tiger.age = 65
tiger.gender = '남'  # 실행 중 객체에 멤버변수 추가함

print(tiger.name)
print(tiger.age)
print(tiger.gender)

zebra = Animal('얼룩말', 45)
# print(zebra.gender)

# 클래스의 상속
# class 클래스명(부모 클래스명):
#    클래스 정의

class Tiger(Animal):
    def eat(seif):
        print('호랑이는 고기를 먹는다')

class Zebra(Animal):
    def eat(self):
        print('얼룩말은 풀을 뜯는다')

t1 = Tiger('혜교', 12)
t1.name
t1.eat()

z1 = Zebra('지현', 10)
z1.eat()

animals = [t1, z1]  # 객체지향의 다형성을 이용
for ani in animals:
    print(ani.name)
    ani.eat()

# 성적처리를 위한 클래스 작성
class SungJuk:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def getTotal(self):
        tot = self.kor + self.eng + self.mat
        return tot

    def getAverage(self):
        avg = self.getTotal() / 3
        return avg

    def getGrade(self):
        grdlist = '가가가가가가미양우수수'
        var = int(self.getAverage()/10)
        grd = grdlist[var]
        return grd

#성적 클래스를 이용해서 객체를 생성
sj = SungJuk('혜교', 99, 98, 99)
print(sj.getTotal())
print(sj.getAverage())
print(sj.getGrade())

class SungJukVO:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

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

sjsrv = SungJukService()
sj1 = SungJukVO('지현', 98, 99, 99)
print(sj1.name)
print(sj1.kor)
print(sj1.eng)
print(sj1.mat)
print(sjsrv.getTotal(sj1))
print(sjsrv.getAverage(sj1))
print(sjsrv.getGrade(sj1))
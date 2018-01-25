#1 print()를 이용하여 다음 내용이 출력하라
from builtins import print

print('*  *   **   ****   ****   *   *')
print('*  *  *  *  *   *  *   *  *   *')
print('**** *    * ****   ****    * * ')
print('*  * ****** *   *  *   *    *  ')
print('*  * *    * *    * *    *   *  ')

print('            +---+')
print('            |   |')
print('        +---+---+')
print('        |   |   |')
print('    +---+---+---+')
print('    |   |   |   |')
print('+---+---+---+---+')
print('|   |   |   |   |')
print('+---+---+---+---+')

print('  /////  ')
print(' | o o | ')
print('(|  ^  |)')
print(' | [ ] | ')
print('  -----  ')

print(' /\_/\ ')
print("( ' ' )")
print('(  -  )')
print(' | | | ')
print('(__|__)')

#2 이름, 나이, 몸무게
name = '박성현'
weight = 66
age = 19

#print('이름:', name, '몸무게:', weight, '나이:', age)
print('이름 {0}, 몸무게 {1}, 나이 {2}'.format(name, weight, age))

#3 수학식을 파이썬 표현식으로 작성
x = 2
y = 3
z = 4
print('3x = ', 3 * x)
print('3x + y = ', 3 * x + y)
print('(x + y)/7 = ', (x + y) / 7)
print('(3 x y) / ( z + 2) = ', (3 * x + y) / (z + 2))

#4 다음 표현식을 완성
x, y = 4, 8 # 별로 안 좋음
x *= y
print('x *= y : ', x)
x -= y
print('x -= y : ', x)

# 5. 다음 수식을 파이썬으로 작성
x = 3
print(x + 7 == 10)

# 6.
print((-32 + 95) * 12 / 3)
print((3 * 4 - ((-27 + 67)/ 4))**8)
print((512 + 1968 - 432)/2 **4 + 128)
print(256 == 2 **8)
print(50 + 50 <= 10 * 10)
print(99 != 10 **2 -1)

#7 연산자 수식 의미 파악
x = 2.5
y = -1.5
m =18
n =4
print(x + n * y - (x + n) * y)
print(m / n + m % n)
print(5 * x - n /5)
print(1 - (1 -(1 -(1 -(1 - n)))))

#8

a = (2.5 * 3) / 27
b = 4 * 2 / 30

print(a)
print(b)

i = 5
print(i)
i = i +1
print(i)

s ='''This is a multi-line string
This is the second line'''
print(s)

s = 'This is a string. \
this continues the string.'
print(s)

age = 20
name = 'Swaroop'

print("abc\nxyz\n123")

#9
print(3 + 4.5 * 2 + 27 / 8)
print(True or False and 3 < 4 or not(5 == 7))
print(True or (3 < 5 and c>= r  == 7))
print(True or (3 < 5 and  6 >= 2))
# print(not True > 'A') # 문자에 비교 연산자
# print(7 % 4 + 3 - 2 / 6 * 'Z') # 문자에 산술 연산자
# print('D' + 1 + 'M' % 2 / 3) # 문자에 비교 연산자
print(5.0 / 3 + 3 / 3)
print(53 % 21 < 45 / 18)
print((4 < 6) or True and False or False and (2 > 3))
print(7 - (3 + 8 * 6 + 3) - (2 + 5 * 2))

# 10
# 배경 지식 필요. - 이윤율 공식
가변자본 = 1500000000
불변자본 = 3000000000
잉여가치 = 4500000000
이윤율 = 잉여가치 / (불변자본 /+ 가변자본)
print('이윤율:', 이윤율)

# 11
달러노트북 = 1071 * 780
유로노트북= 1309 * 650
print('달러노트북: %d, 유로노트북: %d' \
      % (달러노트북, 유로노트북))

#12
pi = 3.14
바깥쪽 = pi * 100
안쪽 = pi * 95
distance = 바깥쪽 - 안쪽
print('바깥쪽 학생이 %dM 더 달렸다' % distance)

#13
print("Check out this line")
# print("//hello there " + '9' + 7) # 문자와 숫자 간 산술 연산
# print('H' + 'I'+ "is" + 1 + "more example") # 문자와 숫자 간 산술 연산
print('H' + '6.5' + 'I'+ "is" + '1' + "more example")
print("Print both of us", "Me too")
print("Reverse" + 'I' + 'T')
# print("Nonnot Here is" + 1 + "more example") # 문자와 숫자 간 산술 연산
# print("Here is " + 10 * 10) # 문자와 숫자 간 산술 연산
# print("Not x is" + True) # 문자와 블리언
print("Not x is" + "True")
print()
print
# print("How about this one" ++ '?' + ' Huh?') # 문자와 증가 연산자

# 15
print(27 / 13 + 4)
print(27 / 13 + 4.0)
print(42.7 % 3 + 18)
# print((3 < 4) and 5 / 8)
print(23 / 5 + 23 / 5.0)
# print(2.0 + 'a')
# print(2 + 'a')
# print('a' + 'b')
# print('a' / 'b')
# print('a' and not 'b')
# print((double)'a' / 'b') # float() 실수변환 함수

# 16
# 파이썬에서는 증감연산자 ++, -- 미지원
#n = 3
# print(++n)      # +(+n)
# print(--n)      # -(-n)
# print("n == " + n)
n = 3
n += 1
print(n)
n = 3
n -= 1
print(n)

# 17
num1 = int(input('첫 번째 정수를 입력하세요'))
num2 = int(input('두 번째 정수를 입력하세요'))
print('%d + %d = %d' % (num1, num2, num1 + num2))
print('%d - %d = %d' % (num1, num2, num1 - num2))
print('%d * %d = %d' % (num1, num2, num1 * num2))
print('%d / %d = %d' % (num1, num2, num1 / num2))

# 입력 받기.
name = input("이름을  입력하시오")

kor = input("국어 점수를 입력하시오")

eng = input("영어 점수를 입력하시오")

mat = input("수학 점수를 입력하시오")

kor=int(kor)
mat=int(mat)
eng=int(eng)

tot=kor+mat+eng
print(tot)

avg=tot/3
print(avg)

#print('{0}, {1}'.fomat(name, kor))
#print('{0}, {1}'.fomat(tot, avg))
#print('{0}, {1:.1f}'.fomat(tot, avg))
#print('{name}, {kor}'.fomat(name='혜교', kor=98) )

print('이름= %s, 국어= %d, 영어= %d, 수학= %d, 총점= %d, 평균= %d'%(name, kor, eng, mat, tot, avg) )
print('이름= %s, 국어= %d, 영어= %d, 수학= %d, 총점= %d, 평균= %d'\
      %(name, kor, eng, mat, tot, avg) )
# money = int(input('바꿀 돈은 얼마?'))
#
# fithousand = money // 50000
# tthousand = (money - fithousand * 50000) // 10000
# fthousand = (money - fithousand * 50000 - tthousand * 10000) // 5000
# fthousand = (money - fithousand * 50000 - tthousand * 10000 - fthousand*5000) // 1000
#
# print(fithousand)
# print(tthousand)
# print(fthousand)
# print(thousand)

def myRange(start, end, hop = 1):
    retVal = start

    while retVal <= end:
        yield retVal
        retVal += hop

hap = 0
for i in myRange(1, 5, 2): # 종료값을 포함한 range 함수 작성
                           # 결국 리스트 형태의 값이 출력된다
# for i in range(1, 5, 2): # i = 1,3
# for i in [1, 3, 5]: # 1, 3, 5
    hap += i
print(hap)

def myRange2(start, end, hop = 1):
    retVal = start

    while retVal <= end:
        # return retVal ??   # 중간 계산 결과를 출력 또는 처리
        yield retVal         # 실행 중에 계산한 값은 generator 타입에 저장해둔다.
        retVal += hop

myRange2(1, 5, 2)
a = myRange2(1, 5, 2)    #yield로 넘긴 데이터는 순환형식으로 된 generator(임시로 사용하는 리스트 같은 것) 타입 생성
print(a)
print(next(a))  # generator 타입에 저장한 값은 iterator 형식으로 다룰 수 있다.
                # iterator는 리스트에 저장한 객체를 순환하며 하나씩 꺼내어 사용하는 자료 구조.
print(next(a))
print(next(a))

for i in a:     # generator 타입에 저장한 값은 for문으로도 출력 가능.
    print(i)

#3.

myList = []             # myList를 리스트로 설정
for i in range(0, 3):    # 아래 문장을 3회 반복
    myList.append(0)    # my list에 0을 추가함(위의 조건으로 3번 반복한다)
hap = 0                 # 합 변수 선언

for i in range(0, 3):   # 아래 문장을 3회 반복
    myList[i] = int(input(str(i+1) + "번째 숫자 :"))    # 마이리스트[i(= 0, 1, 2)]에 숫자를 추가

for k in range(i+1):    # 0, 3도 된다
     hap = hap + myList[k]   # 합은 += mylist(k번)

print("합계 ==> %d" % hap)

# 5
aoa = ['설현','초아', '지민', '유나', '유경', '혜정', '민아', '찬미']
print(aoa[2])
print(aoa[-2])
print(aoa[0:1])
print(aoa[6:])
print(aoa[-7:-5])
print(aoa[1::3])
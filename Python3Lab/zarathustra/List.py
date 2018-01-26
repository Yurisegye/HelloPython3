# 파이썬 자료 구조
# 리스트: sequence 자료구조를 사용
# sequence: 순서가 있는 데이터 구조를 의미
# 리스트, 튜플, 레인지, 문자열 등이 sequence 구조 사용
# 리스트는 []를 이용해서 각 요소에 접근할 수 있다.
msg = 'Hello, World'

# 파이썬에서는 자료 구조를 의미하는 접미사를 변수명에 사용하기도 한다
list1_list = []   # 빈 리스트
list2_list = [1, 2, 3, 4, 5] # 숫자
list3_list = ['a', 'b', 'c'] #문자
list4_list = ['a', 'b', 'c', 1, 2, 3, True]  # 혼합

print(list1_list)

# 가벼운 연산
# 요고 존재 여부 파아기 in/not in 연산자
print(1 in list1_list)
print('a' in list1_list)
print(3 in list2_list)


# 길이 연산 len()
print(len(list1_list))
print(len(list2_list))

# 연결 연산
print(list1_list * 2)

# 연속 연산
print(list2_list * 2)

# 요소의 특정값 참죄 index 사용
print( msg[4], msg[9])
print( list2_list[2])
print( list3_list[2])
print( list4_list[5])

# 요소값 변경: index, =사용
list2_list[2] = -3
print(list2_list)

# 주민코드에서 상별 가려내기
jumin = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7]
birth = 0
if jumin[6] == 1:
    gender = "남자"
elif jumin[6] == 2:
    gender = "여자"
else:
    gender = "메롱"

print("당신은 %s입니다" % (gender))

# 주민번호에서 생년원일 추출
for i in range(0, 6):
    print(jumin[i], end = '') # end: 줄바꿈없이 출력 시 종결문자를 지정

# 특정 범위 내 요소들을 추출할 때는 슬라이스를 사용[i:j:step]
print(jumin[0:6])   # 생년원일
print(jumin[:6])
print(jumin[6:])    # 생년원일을 제외한 나머지 부분
print(jumin[:]) # 전부

print(jumin[0:6:2]) #홀수 자리만 추출
print(jumin[::-1]) #역순으로 추출

# print(jumin[100]) #인덱스 초과 - 에러?
# print(jumin[0:100:2]) #인덱스 초과 - 에러?

#리스트 관련 통계 함수
print(sum(list2_list)) # 총합
print(min(list2_list)) # 최솟값
print(max(list2_list)) # 최댓값

# 리스트가 주어지면 그중 가운데에 위치한 요소값을 출력
# [1, 2, 6, 8, 4] => 6
# [1, 2, 6, 8, 4, 10] => 6, 8
#list = [1, 2, 6, 8, 4]

list = [1, 2, 3, 4, 5, 6]
size = len(list)
mid = int(size/2)
# print('가운데 값:', list[mid]) # 요소 추가 홀수
# print('가운데 값:', list[mid-1], list[mid])
print('가운데 값:', list[mid-1:mid+1]) # 요소 추가 짝수

def listcenter(list):
    size = len(list)
    mid = int(size / 2)
    if size %2 == 0:
        print(list[mid - 1:mid + 1])
    else:
        print(list[mid])

listcenter([1,2,3])
listcenter([1,2,3,4])

# 리스트 조작 함수
# 요소 추가: append
list = [1, 2, 3, 4, 5]
list.append(9)
list.append(8)
print(list)

# 요소 추가: insert(위치, 값)
list.insert(6, 7)
print(list)

# 요소 제거: remove(값), 왼쪽부터 검색 후 삭제
list.remove(9)
print(list)

# 요소 제거: pop(), pop(위치)
list.pop(5)
print(list)
list.pop()  # 마지막 요소 제거
print(list)

# 모두 제거: clear()
list.clear()
print(list)




# 리스트 조작 함수들
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x)
x.append(10) # 하나만 추가할 때
print(x)
x.extend([11, 12]) # 하나 이상을 넣을 때
print(x)
x.remove(11) # 값으로 제거
x.remove(12)
print(x)
x.reverse() # 역순
print(x)
x.pop() # 맨끝을 삭제

x = [10, 5, 1, 4] #비정렬 리스트
x.sort() # 리스트 정렬
print(x)
x.insert(3, 7) # 10 앞에 7을 삽입
print(x)

print(x.count(4)) # 지정한 요소 수
print(x.index(5)) # 요소의 위치값 출력

#### 튜플 tuple
# 리스트 자료구조와 유사하지만
# 한번 입력한 자료는 변경 불가
# 즉, 요소 추가는 가능하나 수정, 삭제는 불가하다.
# 튜플은 ()을 이용한다.
# 튜플 생성시 단일 요소는 요소 뒤에 ,를 추가

#### 집합 set
# 저장한 데이터를 순서에 따라 관리하지 않고
# 중복을 허용하지 않는(unique) 자료 구조.
# 집합은 {}을 이용
# 집합 개념에 따라 합/교/차집합 등의 연산을 지원한다

# 집합 정의
# 1월 중 교육받은 날을 집합으로 정의
edu = {1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 15, 16, 17, 18, 19, 22, 23, 24, 25, 26, 29, 30, 31}

# 집합의 기본 연산
동물 = {'사자', '늑대', '호랑이', '얼룩말'}
육상동물 = {'여우', '고양이', '개', '표범'}
해상동물 = {'돌고래', '해마', '새우', '고등어'}
조류 = {'독수리', '참새', '까마귀', '매'}

print(len(동물)) # 길이
print('여우' in 육상동물) # 여우 검색: in 연산자
print('여우' in 조류) # 여우 검색: in 연산자
# print(동물[2])# index 연산: 3번째 동물은? = 집합에선 지원하지 않는다.

print('합집합')
print(육상동물.union(해상동물)) # 합집합
print(육상동물 | 해상동물) # .union = |
새로운동물 = 육상동물 | 해상동물

print('교집합')
print(새로운동물.intersection(육상동물)) # 교집합
print(새로운동물 & 해상동물) # .intersection = &

print('차집합')
print(새로운동물.difference(육상동물)) # 차집합
print(새로운동물-해상동물) # .difference = -

print('대칭차집합')
print(새로운동물.symmetric_difference(육상동물)) # 여집합(합집합-교집합)
print(새로운동물^육상동물)

# 집합에서 제공하는 메서드
동물.add('사람')    # 데이터 추가
print(동물)
동물.discard('사람')    # 데이터 제거
print(동물)
해상동물.remove('고등어') # 데이터 제거
print(해상동물)

print(육상동물.pop()) # 데이터 확인 후 제거
print(육상동물)

동물.clear()
print(동물)

# 집합과 중복

myDate = {1, 1, 1, 2, 2, 3, 3} # 요소는 모두 3개
print(myDate)
myDate.add(1)   # 의미 없는 코드
print(myDate)   # 어쨌든 3개

### 패킹, 언패킹
# 패킹/packing: 여러 데이터를 변수 하나에 묶어 담기
# 언패킹/unpacking: 변수에 담긴 데이터를 여러 변수에 풀어 넣기

numbers = (1, 2, 4, 5) #튜블 생성(패킹)
a, b, c, d, e = numbers
print(c)

numbers = 1,2,3,4,5 # 패킹시 () 생략 가능
# x,t,x = numbers # 언패킹시 데이터 수와 변수개수 일치

x,y,*z = numbers
print(z)

#m, k, e, m = input().splite()

a, b, c =1, 2, 3        # 변수 초기화에 패킹, 언패킹 사용


# n, k, e, m = input().split()
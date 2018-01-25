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

#
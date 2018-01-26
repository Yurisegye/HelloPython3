## 딕셔너리: 매핑 자료 구조
# 키에 값(value)을 연결시키는 방식으로 데이터를 다루는 방법제공
# 키는 정장한 데이터를 식별하기 위한 번호나 이름
# 값은 각 키에 연결하여 저장한 데이터
# 따라서, 키만 알명 데이터를 바로 찾을 수 있음
# 딕셔너리는 {}에 키:값 형태로 이동.
# 키: 값이 여러개 존재할 경우 , 로

menu = {'1': 'newSungJuk', '2': 'showSungJuk',
        'abc': 'modifySungHuk'} # 키는 다양한 자료형으로 사용

book = { 'bookid': '1', 'bookname': '축구의 역사', 'publisher':'굿스포츠', 'price': 7000}
order = {'orderid':'1', 'custid':'1', 'bookid':'1', 'saleprice':7000, 'orderdate':'2014-07-01'}
customer = {'custid':'1', 'name':'박지성','address':'영국 멘체스터', 'phone':'000-5000-0001'}

print(book)

book_list = []
book_list.append(book)    # 생성한 딕셔너리를 배열에 저장
book_list.append(book)
book_list.append(book)

print(book_list)

# 딕셔너리 처리 메서드
print('1' in book) # '1'을 찾지 못함.
print('bookid' in book) # 딕셔너리에서 in 연산자는 key를 찾는다.

print(book['bookid']) # 따라서 키를 통해 값을 찾는다
print(book['bookname'])
print(book['price'])
# print(book['order']) # 없는 것을 찾으면 유오가 발생한다.

print(book.get('bookname'))
print(book.get('orderid')) # get을 이용하면 없는 것을 찾아도 유오 미발생. 대신 None으로 출력.

bkname = book['bookname'] # 키로 찾은 후 값을 출력
print(bkname)

print(book.get('bookid'))
book['bookid'] = 99   # 키로 값 수정
print(book.get('bookid'))

print(book)
book.update({'판형':'3x4'}) # 새로운 키:값 추가/수정
print(book)

book.update({'판형':'6x10'}) # 기존 키:값 추가/수정
print(book) # 기존 키에서 값만 바꿔 출력

del book['판형']  # 기존 키 삭제
print(book)

# book.clear() # 전부 삭제!

print(book.keys())  # 모든 키 출력
print(book.values())  # 모든 값 출력
print(book.items())     #모든 키:값을 튜플로 출력
items = book.items()    #모든 키:값을 튜플-리스트로 출력
print(list(items))

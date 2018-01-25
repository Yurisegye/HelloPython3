# 모듈 사용하기
# 프로그램을 구성하는 독립 단위(함수/클래스)를 
# 각각 정의하고 관리하는 방법
# 자주 사용하는 기본 기능은 모듈로 한번 말들어 두면
# 필요할 때마다 도입하여 활용할 수 있다.
# 모듈: 관련 있는 데이터들, 함수, 클래스

# 모듈을 사용하려면 import 명령으로
# 인터프리터(통역사)에게 사용여부를 알려야 한다.
# import Lab03 # 자신이 작성한 함수가 담긴 파일
# import random as r         # 별칭으로 줄여 쓰기
from random import randint   # 모듈명을 아예 줄이기
# from math import pi     #파이만
from math import pi, sqrt   # 파이와 제곱근만
# from math import *  # 전부 다(비추)
from zarathustra import zzyzzy
# import zarathustra.hello
from zarathustra.hello import sayhello

# 모듈을 호출할 때는 모듈명(파일명).함수명
from builtins import print

# print(random.randint(1, 10))
# print(r.randint(1, 10))
print(randint(1, 10))
print(pi)
print(sqrt(9))  # 제곱근

# 모듈 호출시 이름을 별칭으로 바꿔 정의
# import 모듈 이름 as 별칭

# 함수 호출시 모듈명까지 기술하는 것이 불편하다면?
# from 모듈명 import 함수명

# 사용자가 만든 모듈을 다른 파일에서 참조하려면
# 두 파일이 모두 같은 위치에 있어야 한다
# 즉, 프로젝트 안에서 서로 참조하려면
# 이 파일들을 같은 위치에 저장해야 한다.

# 한편, Python IDE나 다른 프로젝트에서 모듈을 참조하려면
# pathonPath가 정의한 위치에 모듈을 저장해둔다
# 파이썬 설치 위치나 '파이썬 설치 위치/Lib'

zzyzzy.isLeapYear()

# 파이썬 패키지
# 여러 개발자가 만든 모듈의 이름이 서로 같을 경우
# 파이썬에서는 패키지라는 개념을 이용해서 해결한다
# .연산자를 이용하여 모듈을 계층(디렉토리)으로 관리
# 파이썬에서 디렉토리를 패키지로 인식하려면
# __init__.py라는 파일이 반드시 있어야 한다

sayhello()
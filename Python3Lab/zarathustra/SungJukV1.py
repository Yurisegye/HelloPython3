print('-- 성적 처리 프로그램 v1 --')

name = input("이름을 입력하세요")
kor = int(input("국어 점수를 입력하세요"))
eng = int(input("영어 점수를 입력하세요"))
mat = int(input("수학 점수를 입력하세요"))
tot = kor + eng + mat
avg = tot / 3
grd = '가'
if avg >= 90:
    grd = '수'
elif avg >= 80:
    grd = '우'
elif avg >= 70:
    grd = '미'
elif avg >= 60:
    grd = '양'

#print('{0} {1} {2} {3} {4} {5:.2f} {6}'.format(name, kor, eng, mat, tot, avg, grd))
print('이름: %s, 국어: %d, 수학: %d, 영어: %d, 총점: %d, 평균: %.2f, 학점: %s' % (name, kor, eng, mat, tot, avg, grd))
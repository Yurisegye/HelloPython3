# 리스트 자료 구조를 응용하여 업그레이드!

def grade_list(avg):
    avg = avg_list[idx]
    grd = '가'
    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'
    return grd

name_list = []
kor_list = []
eng_list = []
mat_list = []

tot_list = []
avg_list = []
grd_list = []

print('-- 성적 처리 프로그램 v1 --')

while True:
    idx = len(name_list)    # 인덱스 지정


    name_list.append(input("이름을 입력하세요"))
    kor_list.append(int(input("국어 점수를 입력하세요")))
    eng_list.append(int(input("영어 점수를 입력하세요")))
    mat_list.append(int(input("수학 점수를 입력하세요")))

    tot_list.append(kor_list[idx] + eng_list[idx] + mat_list[idx])
    avg_list.append(tot_list[idx] / 3)
    grd_list.append(grade_list(avg_list[idx]))


    fmt = '이름: %s 국어: %d 수학: %d 영어: %d 총점: %d 평균: %.2f 학점: %s'
    print(fmt % (name_list[idx], kor_list[idx], eng_list[idx], mat_list[idx], \
                 tot_list[idx], avg_list[idx], grd_list[idx]))

    is_exit = input('종료하시려면 n을 누르세요')
    if is_exit == 'n':
        idx += 1
        print('성적', idx, '개를 처리했습니다')
        print('성적 처리 프로그램 종료')
        break
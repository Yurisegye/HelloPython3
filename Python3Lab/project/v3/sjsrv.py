class SungJukService:

    sjdb = []   # 성적 데이터를 저장하는 리스트
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 문자 타입
    # [(no, n, k, e, m, t, a, q, r), (no, n, k, e, m, t, a, q, r), (no, n, k, e, m, t, a, q, r)] 객체 타입은 sj.n 이런 식

    # 성적 처리 - 총점/평균/힉점 계산
    def computeSungJuk(self, sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot/3
        grd_list = '가가가가가가양미우수수'
        sj.grd = grd_list[int(sj.avg/10)]

    # 성적 데이터 추가
    def addSungJuk(self, sj):
        self.computeSungJuk(sj)
        sj.sjno = len(self.sjdb) + 1
        self.sjdb.append(sj)    # 리스트에 성적데이터 추가
        print(sj.to_str())      # 추가한 성적 데이터 확인

    # 전체 성적 데이터 조회
    def getSungJuk(self):
        str_list = []
        for sj in self.sjdb:
            str_list.append(sj.to_str_list())

        return str_list

    # 상세 성적 데이터 조회
    def getOneSungJuk(self, no):
        if no > len(self.sjdb) or no < 0:
            return "\n잘못된 값을 입력하셨습니다."
            result = ""
        for sj in self.sjdb:    # sjdb에서 성적 데이터를 하나씩 순환
            if sj.sjno == no:   # 만일 학생번호와 찾는 번호가 일치한다면
                result = sj.to_str()
                break

        return result

    # 성적 데이터 수정
    def modifySungJuk(self, sj):
        self.computeSungJuk(sj)                 # 성적 재계산
        self.sjdb[sj.sjno - 1] = sj             # 성적 데이터 수정

        return self.sjdb[sj.sjno - 1].to_str()  # 수정한 데이터 확인

    # 성적 데이터 제거
    def removeSungJuk(self, no):
        self.sjdb.pop(no - 1)
        # result = ""
        # for sj in self.sjdb:            # sjdb에서 성적 데이터를 하나씩 순환
        #     if no > len(self.sjdb) or no < 0:
        #         return "\n잘못된 값을 입력하셨습니다."
        #     if sj.sjno == no:           # 만일 학생번호와 찾는 번호가 일치한다면
        #         self.sjdb.pop(no-1)
        #         result = sj.to_str()
        #         break








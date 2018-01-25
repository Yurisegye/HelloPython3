total = 0
while True:
    num = input('더하려는 숫자들을 입력하세요(종료는 stop)')
    if num == 'stop':
        break  # stop 입력시 중지

    # if ord(num[0]) < ord('0') \
    #    or ord(num[0]) > ord('9'):
    if not num.isnumeric():
        print('숫자만 입력하세요')
        continue  # 숫자가 아니면 합산에서 건너뜀

    total += int(num)
    print('합계: ', total)


    def count():
        global times
        times += 1
        print(times)


    times = 0
    count()
    count()
    count()
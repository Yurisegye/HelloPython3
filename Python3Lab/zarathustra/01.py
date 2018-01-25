flag = input('맘에 드는 옷을 골랐나요? (예/아니오)')

if flag == '예':
    print('축하합니다! :)')

    price = int(input('얼마까지 보고 오셨어요?'))
    if price > 10000:
        print('어디서 바가지를 씌워? :(')
    else:
        print('Shut up and Take My Money! XD')

elif flag == '아니오':
    print('아쉽네요 :O')
else:
    print("'예' 또는 '아니오'로만 답해라 짜샤!")

flag = 1 # True의 정수값은 1
if flag:
    print(':)')


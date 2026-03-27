
def convetion_to_won() :
    yen = input("환전할 엔화를 입력해주세요.: ")
    rate = input("오늘자 환율 (100엔 기준)을 입력해주세요.: ")
    #일단은 문자열 자체로 받아드리게 하기.
    return yen, rate

def Cal(a, b) :
    a = float(a)
    b = float(b)
    n = a*(b/100)
    return n

history = []

while True :
    yen, rate = convetion_to_won()
    big_money = [x for x in history if x>=10000]

    if yen=='q' : #만약 q를 누르면 종료되도록
            print('오늘의 환전을 마치도록 하겠습니다.')
            break

    elif yen=='p' : #p를 누르는 파트
        if len(history) == 0 :
            print ("환전한 금액이 없습니다. 입력 후 시도해주세요.")
        else :
            print(f"오늘하신 전체 환전은 {history}입니다.")
            print(f"오늘하신 전체 총합은 {sum(history)}원입니다.")
            print(f"오늘하신 환전의 평균은 {sum(history)/len(history)}원입니다.")
            print(f"오늘하신 환전의 최댓값은 {max(history)}원입니다.")
            print(f"오늘하신 환전의 횟수는 {len(history)}번입니다.")
            print(f"10,000원 이상 환전하신 것은 {big_money}입니다.")
            continue
            
    try : #p나 q가 아니라면 계산시키게끔
        yen1 = float(yen)
        rate1 = float(rate)
        #yen, rate를 실수로 만들어서 수와 문자를 구분하기 위한 노력
        result = Cal(yen1, rate1)
        print(f"환전하신 금액은 {result} 원입니다.") #기본계산영역
        history.append(result)

    except ValueError : 
        print("숫자나 p, q만 입력해주세요.")
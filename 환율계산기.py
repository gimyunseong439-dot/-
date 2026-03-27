
def get_input() : #엔화와 환율 입력
    yen = input ("환전할 엔을 입력해주세요.")
    rate = input ("환율을 입력해주세요.")
    if yen=='q' : #yen이 'q'라면 'q'로 출력
        return 'q', 'q'
    if yen=='p' : #yen이 'p'라면 'p'로 출력
        return 'p', 'p'
    
    if rate=='q' : #rate가 'q'라면 'q'로 출력
        return 'q', 'q'
    if rate=='p' : #yen이 'p'라면 'p'로 출력
        return 'p', 'p'
    
    return float(yen), float(rate)

def calculate(a, b) : #계산
    t = a * (b / 100)
    return t

def display(n) : #출력
    print (f"환전결과 {n}원입니다.")
    return n

history = [] #과거 환전 내역 바구니

while True :
   yen, rate = get_input()
   
   if yen=='q' :
        print("오늘의 환전은 여기까지입니다. 감사합니다.")
        break
   
   elif yen=='p' :
        big_money = [x for x in history if x>=10000] #만 원이 넘는 환전금액들의 바구니
        print(f"오늘 환전한 기록들 : {history} \n 총 합은 {sum(history)}입니다. ")
        # 과거 환전 내역을 보여주고, 합계를 보여줌
        print(f"10,000원이 넘는 금액들 : {big_money}") #만 원이 넘는 것만 보여줌
        print(f"총 환전 횟수 : {len(history)}")
        print(f"최대 환전 금액 : {max(history)}")
        print(f"평균환전 금액 : {sum(history)/len(history)}")
   else : 
       gyesan = calculate(yen, rate)
       display(gyesan)
       history.append(gyesan)
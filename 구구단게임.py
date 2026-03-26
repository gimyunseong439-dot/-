import random

score=0

while True :
 a=random.randrange(2,10)
 b=random.randrange(2,10)

 ans = input(f"{a}×{b}는?")

 if ans=='q' :
     print(f"오늘 수업 끝! 오늘 {score}개 맞췄어!")
     break

 try :
  ans1 = int(ans)

  if ans1==a*b :
    print(f"넌 수학계의 천재야! {score+1}점!")
    score+=1

  else :
    print("어, 아니야. 다시!")

 except ValueError :
    print("q 또는 정답만 넣어줘!")
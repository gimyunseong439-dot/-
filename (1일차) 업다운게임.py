
import random

Com = random.randrange(1, 101)
Count = 0

while Com%10==0:
    Com = random.randrange(1, 101)

while True :
   User = input("내가 생각한 수는? : ")

   if User=='q' :
      print ("그래~ 수고했어! 오늘은 여기까지!")
      break
   
   try :
        User = int(User)

        if User%10==0 :
            print ("10의 배수는 너무 쉬워서 안 알려줌!")
            Count+=1
            continue
        
        if User > Com :
            print ("너무 커!")
            Count+=1
        elif User < Com :
            print ("너무 작아!")
            Count+=1
        else :
            print (f"정답이야! {Count}번 만에 맞췄어!")
            break


   except ValueError:
      print ("q 또는 숫자만 넣어줘!")
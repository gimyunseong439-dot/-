import random

Com = random.randint(1, 100)
print("컴퓨터: 1부터 100까지 중에 하나 골랐어. 맞춰봐!")
count = 0

while True:
    try :
        a = int(input("숫자를 입력해봐: "))
        count += 1
        if a == Com:
            print("으악! 어떻게 알았지? 정답이야!")
            print(f"넌 {count}번만에 맞췄어!")
            break
        elif a < Com:
            print("업!! 좀 더 커야해!")
        elif a > Com:
            print("다운!! 더 작아야해!")
            
    except ValueError:
        print("숫자를 쓰라고 병신아 ^^")
while True:
    a = input("원하는 첫번째 수를 입력해줘! (종료하려면 q!) ")
    if a == "q": 
        print("수고했어! 종료할게!")
        break

    a = float(a)
    b = float(input("원하는 두번째 수를 입력해줘! "))
    cal = input("덧셈, 뺄셈, 곱셈, 나눗셈 중에 뭘 해줄까? ")

    if cal == "덧셈":
        print(f"결과: {a + b}")
    elif cal == "뺄셈":
        print(f"결과: {a - b}")
    elif cal == "곱셈":
        print(f"결과: {a * b}")
    elif cal == "나눗셈":
        if b == 0:
            print("0으로 나눌 수 없어! 띨빡아^^")
        else:
            print(f"결과: {a / b}")
    else:
        print("제대로 입력해줘!")

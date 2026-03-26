ID = input("아이디를 만들어주세요.")
password = input("비밀번호를 만들어주세요")

while True :
 a=input("아이디를 입력해주세요.")
 if a==ID :
    b = input ("비밀번호를 입력해주세요.")
    if b==password :
        print("로그인이 되었습니다.")
        break
    else: print("비밀번호가 틀렸습니다.")
 else: print("아이디가 틀렸습니다.")
   
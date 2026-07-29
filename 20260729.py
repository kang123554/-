##txt1 = input("닉네임을 입력하세요 : ")
##print("환영합니다", f"{txt1}님!")

##txt1 = float(input("실수를 입력하세요 : "))
##print(f"{float(txt1*10):.3f}")

##txt1 = int(input("첫번째 숫자를 입력하세요 : "))
##txt2 = int(input("두번째 숫자를 입력하세요 : "))
##txt3 = int(input("세번째 숫자를 입력하세요 : "))
##print("종합은", txt1 + txt2 + txt3)

##txt1 = int(input("반지름을 입력하세요 : "))
##print("원의 넓이는", txt1 * txt1 * 3.14)
##print("원의 둘레길이는", f"{(txt1 * 2 * 3.14):.1f}")

##txt1 = int(input("윗변을 입력하세요 : "))
##txt2 = int(input("밑변을 입력하세요 : "))
##txt3 = int(input("높이를 입력하세요 : "))
##print("사다리꼴의 넓이는", f"{float(txt1 + txt2) * txt3/2}")

##txt1 = input("문자열을 입력하세요 : ")
##print(txt1[1::2])

##txt1 = input("주민번호를 입력하세요(-포함):")
##print(txt1[2:6])

##txt1 = "타파에벅서이썬스나짱만스"
##print(f'"{txt1[11]+txt1[0]+txt1[3]+txt1[7]+txt1[2]+txt1[4]+txt1[10]+txt1[8]}"')

##txt1 = """동해물과 백두산이 마르고
##닳도록
##하느님이 보우하사
##우리나라 만세.
##무궁화 삼천리 화려 강산
##대한 사람, 대한으로
##길이 보전하세."""

##print(txt1[33:35])
##print(txt1[-3:-1])

##print(txt1[:36])
##print("무궁화 삼천리 화려", "강세")
##print(txt1[51:])

##txt1 = "강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩깍지다."

##print("첫번째 완두콩은 " + str(txt1.find("완두콩")) + "번째에 있습니다.")
##print("두번째 완두콩은 " + str(txt1.rfind("완두콩")) + "번째에 있습니다.")
##message1 = txt1.find("완두콩")
##message2 = txt1.rfind("강낭콩")
##print(txt1[message1:message1+11])
##print(txt1[message2:message2+11])

##txt1 = input("이메일을 입력해주세요 : ")
##message1 = txt1.find("@")
##find("이 이메일의 아이디는 " + txt1[message1:message1-6] + "입니다.")

##txt1 = input("이메일을 입력해주세요 : ")
##position = txt1.find("@")
##print("이 메일의 아이디는 " + txt1[:position] + "입니다.")

##txt1 = input("전화번호 입력 : ")
##n1,n2,n3= txt1.split("-")
##print(n1)
##print(n2)
##print(n3)

##txt1 = input("파일명을 입력해주세요 : ")
##txt2 = txt1.replace("jpg", "png")
##print(txt1, "파일을", txt2, "파일로 변경하였습니다.")

txt1 = "Hello, Python! Hello, String!"
print(txt1.upper())
print(txt1.lower())


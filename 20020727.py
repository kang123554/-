##sweat = '달디' * 20
##sweat2 = sweat * 10
##number = 255 
##message = sweat2 + ' ' + '단 밤양갱' + str(number) + '개'
##print(message)

##line = "=" * 20 
##header = "밤양갱 대박 세일"
##footer = "놓치지 마세요!"
##message = line + "\n" + header + "\n" + line + "\n" + footer + "\n" + line
##print(message)

##txt1 = input("아이디 : ")
##txt2 = input("비밀번호 : ")
##message = "당신의 아이디는" + f' "{txt1}"' + "이며," + " 비밀번호는" + f' "{txt2}"' + "입니다."
##print(message)

##txt1 = input("문자열을 입력하세요 : ")
##print(txt1[1::2])

##txt1 = input("주민번호를 입력하세요(-포함):")
##print(txt1[2:6])

##txt1 = "타파에벅서이썬스나짱만스"
##message = (txt1[11]) + (txt1[0]) + (txt1[3]) + (txt1[7]) + (txt1[2]) + (txt1[4]) + (txt1[10]) + (txt1[8])
##print(f'"{message}"')
##
##txt1 = """동해물과 백두산이 마르고
##닳도록
##하느님이 보우하사
##우리나라 만세.
##무궁화 삼천리 화려 강산
##대한 사람, 대한으로
##길이 보전하세."""
##
####print(txt1[34:36])
####print(txt1[-3:-1])
##
##print(txt1.replace("강산", "강세"))

##print(txt1[:48]+"강세")
##print(txt1[52:])

##txt1 = "강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩깍지다."
##message1 = "첫번째 완두콩은 " + str(txt1.find("완두콩")) + "번째에 있습니다."
##message2 = "두번째 완두콩은 " + str(txt1.rfind("완두콩")) + "번째에 있습니다."
##print(message1)
##print(message2)

##message1 = txt1.find("완두콩")
##print(txt1[message1:message1+11])
##message2 = txt1.rfind("강낭콩")
##print(txt1[message2:message2+11])

txt1 = input("이메일을 입력해주세요 : ")
message = txt1.find("@")
print("이 메일의 아이디는 " + txt1[message:message+6] + "입니다.")




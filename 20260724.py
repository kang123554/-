##txt = "강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고 완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩깍지다."
####
####print("첫번째 완두콩은 "+str(txt.find("완두콩"))+ "번째에 있습니다.")
####print("첫번째 완두콩은 "+str(txt.rfind("완두콩"))+ "번째에 있습니다.")
##
####message = txt.rfind("강낭콩")
######print(txt[message:message+11])
####print(txt[message:message+11])
##
##txt = input("이메일을 입력해주세요 : ")
##message = txt.find("l")
##print("이 이메일의 아이디는 "+txt[message:+6]+"입니다")

##dessert = "초코케이크 녹차마카롱 모카라떼"
##cake, macaron, coffee = dessert.split(" ")
##
##print("[ 오늘 먹을 간식 목록 ]")
##print("케이크 :", cake) 
##print("마카롱 :", macaron)
##print("커피 :", coffee)

##n1, n2 = input("int 둘 입력 : ").split()
##print(n1)
##print(n2)
##print(n1+n2)
##print(int(n1)+int(n2))

##a,b,c = input("알파벳 셋 입력 : ").split()
##print(c,b,a,sep=">")

##r1, r2 = input("float 둘 입력 : ").split()
##r1 = float(r1)
##r2 = float(r2)
##
##print(r1*r2)

##message = """대공원에 봄 벚꽃 놀이는
##낮 봄 벚꽃 놀이보다
##밤 봄 벚꽃 놀이니라."""
##
##print(message.replace("벚꽃","개나리"))

##win = "windowxp"
##update = win.replace("xp", "11")
##print(update + "로 업데이트 됐습니다")
##print(update,"로 업데이트 됐습니다")

##japangi = """이 자판기 안에는
##포도맛 사이다,
##포도맛 쥬스,
##포도맛 슬러쉬
##가 있습니다."""
##taste = input("무슨 맛 자판기로 바꿀까요 : ")
##print(japangi.replace("포도", taste))

##message = input("영어로 문장을 적어주세요 : ")
##print(message.upper())
##print(message.lower())

##message = "abcd 1234 ..@@ !!!"
##trans = message.upper()
##print(trans)

##txt = input("전화번호 입력 : ")
##n1,n2,n3 = txt.split("-")
##print(n1)
##print(n2)
##print(n3)

##txt1 = input("파일명을 입력해주세요 : ")
##print(txt1, "파일을", txt1.replace("jpg", "png"), "파일로 변경하였습니다.")

##message = "hello, python! hello, string!"
##print(message.upper())
##print(message.lower())

##string = "파이썬 {0}번 복습하기".format(10)
##print(string)

##string2 = f"문자열도 {10:8.2f}번 복습하기"
##print(string2)

##tips = "len 함수로 문자열의 갯수를 세봅시다."
##print(len(tips))
##number = 15335
##print(len(number))

##year = input("태어난 해를 입력해주세요 : ")
##month = input("태어난 월을 입력해주세요 : ")
##day = input("태어난 일을 입력해주세요 : ")
##date = "{}년 {}월 {}일".format(year, month, day)
##print("당신의 생일은"+ date + "입니다. happy brithday!")

##num1 = f'{10}/{20}'
##num2 = f'[{10.10}/{20.20}]'
##print(num1)
##print(num2)

##pi = 3.14
##num3 = f'[{pi:4.1f}/{pi:010.0f}]'
##print(num3)

##txt1 = input("영화 제목을 입력하세요: ")
##txt2 = input("개봉 연도를 입력하세요: ")
##txt3 = input("주연 배우를 입력하세요: ")
##message = "{}은 {}년에 개봉한 {} 주연의 영화입니다.".format(txt1, txt2, txt3)
##print(message)

txt1 = input("아이드를 입력해주세요(6글자 이상): ")
txt2 = txt1[:3]+"*****"
message = "암호화된 아이디 :"+txt2
print(message)

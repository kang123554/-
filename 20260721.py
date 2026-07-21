##print(type("안녕하세요"))
##<(class 'str')>
##print(type(273))
##<(class 'int')>
##
##print("# 하나만 출력합니다.")
##print("hello python programming...!")
##print()
##
##print("# 여러개를 출력합니다.")
##print(10, 20, 30, 40, 50)
##print("안녕하세요", "저의", "이름은", "윤인성입니다.!")
##
##print("안녕하세요")
##print('안녕하세요')
##print(""안녕하세요"라고 말했습니다.")

##print('"안녕하세요"라고 말했습니다.')

##print("'배가 고픕니다' 라고 생각했습니다")

##print("\"안녕하세요\"라고 말했습니다")
##print('\'배가 고픕니다\'라고 생각했습니다')
      
##print("안녕하세요\n안녕하세요")
##print("안녕하세요\t안녕하세요")

##print("이름\t나이\t지역")
##print("윤인성\t25\t강서구역")
##print("윤아린\t24\t강서구")
##print("구름\t3\t강서구")

##print("동해물과 백두산이 마르고 닳도록\n하느님이 보우하사 우리나라 만세\n무궁화 삼천리 화려강산 대한사람\n대한으로 길이 보전하세")
##print("""동해물과 백두산이 마르고 닳도록
##하느님이 보우하사 우리나라 만세
##무궁화 삼천리 화려강산 대한사람
##대한으로 길이 보전하세""")

##print("""
##동해물과 백두산이 마르고 닳도록
##하느님이 보우하사 우리나라 만세
##무궁화 삼천리 화려강산 대한사람
##대한으로 길이 보전하세
##""")

##print("""\
##동해물과 백두산이 마르고 닳도록
##하느님이 보우하사 우리나라 만세
##무궁화 삼천리 화려강산 대한사람
##대한으로 길이 보전하세\
##""")

##print("안녕" + "하세요")
##print("안녕하세요" + "!")
##print("안녕하세요" + "1")
##print("안녕하세요" * 3)

##print(3*"안녕하세요")

##print("문자 선택 연산자에 대해 알아볼까요?")
##print("안녕하세요"[0])
##print("안녕하세요"[1])
##print("안녕하세요"[2])
##print("안녕하세요"[3])
##print("안녕하세요"[4])

##print("문자를 뒤에서부터 선택해 볼까요?")
##print("안녕하세요"[-1])
##print("안녕하세요"[-2])
##print("안녕하세요"[-3])
##print("안녕하세요"[-4])
##print("안녕하세요"[-5])

##print("안녕하세요"[0:2])
##print("안녕하세요"[1:3])
##print("안녕하세요"[2:4])

##print("안녕하세요"[1:])
##print("안녕하세요"[:3])

##print(len("안녕하세요"))

##print("안녕하세요"[10])

##txt1 = input("아이디 : ")
##txt2 = input("비밀번호 : ")
##message = (f"당신의 아이디는 \"{txt1}\"이며, 비밀번호는 \"{txt2}\"입니다.")

##str1 = "파이썬 문자열을 골라보자"
##print(str1[0])
##print(str1[4])
##print(str1[9])
##print(str1[2])
##print(str1[6])
##print(str1[12])

##word = "문자열과 인덱스"
##print(word[0])
##print(word[3])
##print(word[5])
##print(word[-1])

##snack = "떡볶이 순대 튀김"
##setmenu = snack[0] + snack[4] + snack[7]
##print(setmenu)

##word = "부분만 바꾸려고 하면 에러가 나요"
##print(word)

##word[0] = "수" # 에러나면 주석처리해서 다시
##word = "새로 만들어 덮어쓰기는 가능"
##print(word)

##word = "슬라이싱으로 다양하게 문자를 잘라봅시다"
##
##print(word[0:4])
##print(word[7:9])
##print(word[5:])
##print(word[:12])
##print(word[::3])
##print(word[::-3])

song = "록도닳 고르마 이산두백 과물해동"

reverse = song[::-1]
print(reverse)

song ="동해물과 백두산이 마르고 닳도록"

part_song = song[0:4]
print(part_song)
part_song = song[5:13]
print(part_song)
part_song = song[14:]
print(part_song)



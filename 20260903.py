###변수 1개
##month = int(input("월을 입력하면 계절이 나와요 : "))
##
##if 3 <= month <= 5:
##    print("봄")
##elif 6 <= month <= 8:
##    print("여름")
##elif 9 <= month <= 11:
##    print("가을")
##elif 12 == month or 1 <= month <=2:
##    print("겨울")
##else:
##    print("잘못입력했어요")

#변수 2개
##month = int(input("월을 입력하면 계절이 나와요 : "))
##count 
##
##if 3 <= month <= 5:
##    print("봄")
##elif 6 <= month <= 8:
##    print("여름")
##elif 9 <= month <= 11:
##    print("가을")
##elif 12 == month or 1 <= month <=2:
##    print("겨울")
##else:
##    print("잘못입력했어요")

#while 사용

##while True"month = int(input("월을 입력하면 계절이 나와요 : "))
##    if 3 <= month <= 5:
##        print("봄")
##    elif 6 <= month <= 8:
##        print("여름")
##    elif 9 <= month <= 11:
##        print("가을")
##    elif 12 == month or 1 <= month <=2:
##        print("겨울")
##    else:
##        print("입력오류")

#while 사용 + 봄이 2회 + 여름 2회 일경우 그만

count1 = 0
count2 = 0 

while True:
    month = int(input("월을 입력하면 계절이 나와요 : "))
    
    if 3 <= month <= 5:
        print("봄")
        count1 += 1
        print(f"봄 {count1}")
    elif 6 <= month <= 8:
        print("여름")
        count2 += 1
        print(f"봄 {count2}")
    elif 9 <= month <= 11:
        print("가을")
    elif 12 == month or 1 <= month <=2:
        print("겨울")
    else:
        print("입력오류")
        
    print(f"봄은 {count1}회, 여름은 {count2} 입니다")
    
    if count1 >= 2 and count2 >= 2:
        break

    

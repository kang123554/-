##money = int(input("얼마인가요 : ")) #원금
##person = 1 #사람
##balance = money #잔액
###원금 - 잔액 
##
##while person <= 5:
##    #person += 1
##    if balance % 5 == 0:
##        balance = money // 2 
##    elif balance % 5 != 0:
        
        
##money = int(input("얼마인가요 : ")) #원금
##balance = money #집어 넣는다는 의미다
##
##balance = balance // 2 #잔금
##print(f"1번 사람은 {balance}원")
##balance = balance // 2 #누적
##print(f"2번 사람은 {balance}원")
##balance = balance // 2 #누적
##print(f"3번 사람은 {balance}원")
##balance = balance // 2 #누적
##print(f"4번 사람은 {balance}원")
##balance = balance // 2 #누적
##print(f"5번 사람은 {balance}원")


##money = int(input("얼마인가요 : ")) #원금
##balance = money #집어 넣는다는 의미다
##person = 1 #사람
##
##while person <= 5:
##    balance = balance // 2 #잔금
##    print(f"{person}번 사람은 {balance}원")
##    person += 1

##money = int(input("얼마인가요 : ")) #원금
##balance = money #집어 넣는다는 의미다
##person = 1 #사람
##
##while person <= 5:
##    balance = balance // 2
##    print(f"{person}번 사람은 {balance}원")
##    person += 1

##while num1 <= count < num2: #
##    count += 1
##    if count == 10:
##        continue
##    print(count * count, end=" ")

  
##        if count == 10:
##            continue
##        print(count * count, end=" ")
##        count += 1
##    if num2 <= count < num1:
##        if count == 10:
##            continue
##        count += 1
##        print(count * count, end=" ")

##num1 = int(input("숫자1 : ")) #숫자1
##num2 = int(input("숫자2 : ")) #숫자2
##start = 0
##end = 0
####count = 5
##
##if num1 < num2:
##    start = num1
##    end = num2
##else:
##    start = num2
##    end = num1
    
##start += 1
##
##while start < end:
##    
##    print(start * start, end=" ")
##    start += 1

##while True:
##    start += 1
##    print(start * start, end=" ")
##    if start == end:
##        break

#테스트입니다
#0 1 2 3 4 5
#■ ■

txt1 = input("문장을 입력해주세요 : ")
count = 0
print(f"바뀐문장 : txt1[count]")

while count < len(txt1): #0<6
    if count % 2 == 1: #홀수일 경우
        print(txt1[count], end="")
    else: #짝수일 경우
        print("■", end="")
    count+=1
##    print(f"바뀐문장 : txt1[count]")











    

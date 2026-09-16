#정확도 4번 입력 후 평균 구하기

##txt1 = int(input("입력 : "))
##count = 0 #횟수
##total = 0 #합계. 평균처리 필요 
##
##while count < 4:
##    txt1 = int(input("입력 : "))
##    count += 1
##    total = total + txt1 
##print(total / 4)

##import random
##
##count = 0 #횟수
##total = 0 #합계. 평균처리 필요 
##
##while count < 4:
##    txt1 = random.randint(1,100)
##    count += 1
##    total = total + txt1 
##print(total / 4)

#3백만원에서 매월 20퍼씩 차감, 잔여 10만 남았을때 종료

##money = int(input("총 얼마 : "))
##balance = money 
##count = 1 
##
##while True:
##    balance = balance * 0.8
##    count += 1 
##    print(f"{count}개월 잔액 {balance:.0f}원")
##
##    if balance < 100000:
##        break
##print()
##print(f"{count} 개월")

##import random
##
##money = random.randint(1000000,3000000)
##balance = money 
##count = 0
##
##while True:
##    balance = balance * 0.8
##    count += 1 
##    print(f"{count}개월 잔액 {balance:.0f}원")
##
##    if balance < 100000:
##        break
##print()
##print(f"{count} 개월")

#계단 오를때마다 점수 상승 (1층 3점, 2층 5점) n층 몇점?

##num1 = int(input("입력 : "))
##stairs =1
##score = 3 
##
##while stairs < num1:
##    stairs +=1
##    score = score + 2
##
##print(f"{stairs}층을 올라가면 {score}점")

##import random
##
##num1 = random.randint(1,20)
##stairs =1
##score = 3 
##
##while stairs < num1:
##    stairs +=1
##    score = score + 2
##
##print(f"{stairs}층을 올라가면 {score}점")

#1~100 사이의 랜덤숫자

##import random 
##
##score = int(input("1~100사이 숫자를 입력해주세요 : "))
##count = 0
##
##while True:
##    count += 1
##    num1 = random.randint(1,100)
##
##    if num1 > score :
##        print("더 낮은 숫자가 정답입니다.")
##    elif num1 < score:
##        print("더 높은 숫자가 정답입니다.")
##    elif num1 == score:
##        print("정답입니다.")
##
##    if count < 4:
##        break

##import random 
##
##num1 = random.randint(1,100)
##count = 0
##
##while True:
##    count += 1
##    score = int(input("1~100사이 숫자를 입력해주세요 : "))
##
##    if num1 < score :
##        print("더 낮은 숫자가 정답입니다.")
##    elif num1 > score:
##        print("더 높은 숫자가 정답입니다.")
##    elif num1 == score:
##        print("정답입니다.")
##        break
##    
##print("정답까지 ", count,"번")

import random 

num1 = random.randint(0,9)
num2 = num1
num3 = num1 

while num1 == num2 or num1 == num3 or num2 == num3:
    num2 = random.randint(0,9)
    num3 = random.randint(0,9)
    print(num1, num2, num3)

num_all=str(num1)+str(num2)+str(num3)
print("정답:",num_all)

    




















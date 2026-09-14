#짝수번째 □ 넣기 

##txt1 = input("입력 : ") #테스트입니다
##count = 0 
##
##while count < len(txt1): # 0<count<6 
##    if count % 2 == 0:
##        print(txt1[count], end="")
##    else:
##        print("□", end="")
##    count += 1     

#3백만원에서 매월 20퍼씩 차감, 잔여 10만 남았을때 종료 
    
##money = int(input("총 얼마 : ")) #3백만
##balance = money #처음 잔액은 총액과 같다
##count = 1 #매월 20%씩 차감횟수
##
##while True:
##    balance = balance * 0.8
##    print(f"{count}개월 남은금액 {balance:.2f}원") #소수점 적용 어떻게?
##    count += 1
##
##    if balance <= 100000:
##        break 

#정확도 4번 입력받고 정확도의 평균구하기

##count = 1 #정확도 1,2,3,4
##total = 0 #평균을 내기위한 합계필요
##
##while count <= 4:
##    txt1 = int(input("정확도는 : "))
##    count += 1
##    total = total + txt1
##
##print(total / 4)

#1층을 올라가면 3점, 2층 올라가면 5점,3층 올라가면 7점
#층마다 2점씩 추가, N층을올라가면 몇점? 

##layor = int(input("숫자입력 : "))
##total = 3 #점수가 필요함
##
##while layor < 10:
##    print(f"{layor}층 올라가면 {total}점")
##               
##    layor += 1 #1층 ~ N층
##    total = total + 2 #점수계산 

##lastlayer = int(input("숫자입력 : "))
##layer = 1
##total = 3 #점수가 필요함
##
##while layer < lastlayer:          
##    layer += 1 #1층 ~ N층
##    total = total + 2 #점수계산
##
##print(f"{layor}층 올라가면 {total}점")

##import random
##value1 = random.randint(시작,끝)
##value2 = random.randrange(시작,끝전,증감)

#랜덤한 10이상 101미만의 숫자를 만듬

##import random
##count = 0
##
##while count < 10:
##    print(random.randint(10,101))
##    count += 1 

#랜덤한 10이상 101미만의 10단위의 숫자를 만듬

##import random
##count = 0
##
##while count < 2:
##    print(random.randrange(10,101,10))
##    count += 1 
    
#3이상 11미만 20개 출력 

##import random
##count = 0
##
##while count < 20:
##    print(random.randint(3,11) , end=" ")
##    count += 1 
##
###일의 자리 2나 7인 100이하의 숫자 7개 출력 
##
##import random
##count = 0
##
##while count < 7 :
##    print(random.randrange(2,100,5))
##    count += 1 

#1~100 사이의 

##import random
##txt1 = int(input("1~100 사이 숫자를 입력해 주세요 : "))
##score = 66 
##count = 0
##
##while count <= 4
##    if txt1 > score:
##        print("더 낮은 숫자가 정답입니다.")
##    elif txt1 < score:
##        print("더 높은 숫자가 정답입니다.")
##    else:
##        print("정답입니다.")
##        break
    
##import random
txt1 = int(input("1~100 사이 숫자를 입력해 주세요 : "))
score = 66 
count = 0

while count < 4:
##    print(random.randint(1,100))
    if txt1 > score:
        print("더 낮은 숫자가 정답입니다.")
    elif txt1 < score:
        print("더 높은 숫자가 정답입니다.")
    elif txt1 == score:
        print("정답입니다.")

    count += 1 







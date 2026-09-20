#1~6눈금 주사위 값을 랜덤하게 받아와서 홀짝 맞추는 프로그램 작성

import random

##txt1 = random.randint(1,6)
##count = 0 
##
##while count < 10:
##    txt1 = random.randint(1,6)
##    if txt1 % 2 == 0:
##        print("짝수")
##    else:
##        print("홀수")
##    count += 1 

#choice 사용예제
##import random
##
##fruits = ["사과", "바나나", "딸기", "포도"]
##
##print(random.choice(fruits))


#랜덤한 길이의 패스워드 만들기(숫자 조합)

##import random

##txt1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
##txt1 = "0123456789"
##count = 0
##
##while count < 8:
##    print(random.choice(txt1),end="")
##          
##    count += 1

#input으로 시간 하나 입력 받아서 매시간마다 뭐했는지 출력
#밥먹기, 잠자기, 공부하기 중에서만 선택

##import random 
##
##work = input("뭐했누?? : ")
##txt1 = 밥먹기
##txt2 = 잠자기
##txt3 = 공부하기 
##count = 0
##
##while count < 2:
##    print(random.choice(txt1, txt2, txt3))
        
import random

time = int(input("몇 시간 동안 할까요? "))

count = 1

while count <= time:
    num = random.randint(1, 3)

    if num == 1:
        print(count, "시간째: 밥먹기")
    elif num == 2:
        print(count, "시간째: 잠자기")
    else:
        print(count, "시간째: 공부하기")
    count += 1 





    

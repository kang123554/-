#1~6눈금 주사위 값을 랜덤하게 받아와서 홀짝 맞추는 프로그램 작성

##import random
##txt1 = random.randint(1,6)
##
##if txt1 % 2 == 0:
##    print("짝수")
##else:
##    print("홀수")

##import random
##count = 0
##
##while count < 10:
##    txt1 = random.randint(1,6)
##    if txt1 % 2 == 0:
##        print("짝", end=" ")
##    else:
##        print("홀", end=" ")
##    count += 1

#for 예제

##for num in range(10):
##    print(num,end=" ")

##for num in range(1,20):
##    print(num,end=" ")

##for num in range(1,19,3):
##    print(num,end=" ")

##for i in range(10):
##    print("안녕", i , "번째")

##for i in range(10):
##    print("안녕", i , "번째")

##for i in range(1,11):
##    print("안녕", i , "번째")

##for i in range(2,101,2):
##    print(i , end=" ")

##for i in range(1,101,2):
##    print(i , end=" ")

##for i in range(10,0,-1):
##    print(i , end=" ")

##total = 0
##
##for i in range(1, 101):
##    total += i
##    
##print(total)

##5의 배수 만들기
##
##for i in range(5,101,5):
##    print(i, end=" ")
##
##3~99까지의 3의 배수의 합을 출력

##total = 0 
##
##for i in range(3,100,3):
##    total += i
##    
##print(f"3의 배수의 합 : {total}")

##for i in range(1,11):
##    if i % 2 == 0:
##        print("짝수 안녕")
##    elif i % 2 == 1:
##        print("홀수 안녕")

##first_num = int(input('시작값 입력 : '))
##last_num = int(input('끝값 입력 : '))
##
##for i in range(first_num, last_num+1):
##    if i % 2 == 0:
##        print('짝수 :', i)
##    elif i % 2 == 1:
##        print('홀수 :', i)                      

##print('시작값 입력 : ')
##first_num = int(input())
##
##print('끝값 입력 : ')
##last_num = int(input())
##
##for i in range(first_num, last_num+1):
##    if i % 2 == 0:
##        print('짝수 :', i)
##    elif i % 2 == 1:
##        print('홀수 :', i)        

##for i in range(0,200,15):
##    print(i,end=" ")

##first = int(input("시작값 입력 : "))
##last = int(input("끝값 입력 : "))
##
##for i in range(first, last):
##    if i % 3 == 0 and i % 5 ==0:
##        print(i, end=" ")

##for num in range(1,100):
##    if num > 55:
##        break
##    print(num, end=" ")

#2의 제곱을 출력

##for num in range(1,7):
##    power = 2 ** num
##    if power > 64:
##        break
##    print(power, end=" ")

#13의 배수를 제외한 홀수를, 그 합이 500 넘을 때까지 출력

##total = 0
##
##for i in range(1,500,2):
##    if i % 13 == 0:
##        continue
##    print(i, end=" ")
##    total += i
##    if total > 500:
##        break
##print()
##print(total)
    
#20까지의 홀수 곱 출력

##count = 1
##for i in range(1,20,2):
##    count *= i
##    print(f"{i} = {count}")

#숫자를 입력받아 거듭제곱 값이 나오도록 만들고 10000이 넘으면 멈춤 

##num1 = int(input("숫자를 입력해주세요 : "))
##total = num1 
##
##for num1 in range(1,30):
##    total = total ** num1
##    if total > 10000:
##        break
##    print(total, end=" ")

num1 = int(input("숫자를 입력해주세요 : "))

for num1 in range(1,20):
    total = total * num1 
    if total > 10000:
        break
    total += num1
print(total, end=" ")

##for num in range(7):
##    power = 2 ** num
##    if power > 64:
##        break
##    print(power, end=" ")


















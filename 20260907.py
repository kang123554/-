##count = 3
##while True:
##    print("숫자가 점점 작아져갑니다...")
##    count -= 1
##    if count < 0:
##        break

##count = 0
##while count < 5:
##    count += 1
##    if count % 3 == 0:
##        continue
##    print(f"{count}번째 반복중")

##count = 0
##while True:
##    print(f"{count}번째 반복중...")
##    count += 1
##    if count >= 5:
##        break

##count = 0
##while count < 13:
##    count += 1
##    if count % 6 == 0:
##        continue
##    print(f"{count}는 6의 배수가 아닙니다.")

##count = 0
##
##while True:
##    num1 = int(input("양수를 입력해주세요 : "))
##    count += num1
##    if num1 > 0:        
##        print(f"현재까지의 양수의 합은 {count}입니다")
##    elif num1 < 0:
##        print(f"음수를 입력하셨습니다")
##    else:
##        print(" ")
##        break

##total = 0
##while True:
##    number = int(input("양수를 입력해주세요 : "))
##    if number == 0:
##        break
##    elif number < 0:
##        print("음수를 입력하셨습니다")
##        continue
##    else:
##        total = total + number
##        print("현재까지의 양수의 합은 {0}입니다".format(total))

##word = "Hellowhile"
##count = 0
##
##while count < len(word):
##    if count % 2 == 1:
##        count += 1
##        continue
##    print(word[count], end = " ")
##    count += 1 

##result = ""
##while True:
##    word = input("단어를 입력하세요('end'를 입력하면 종료): ")
##    if word == "end":
##        break
##    if len(word) < 3:
##        continue
##    result += word + " "
##print(f"입력된 단어들: {result}")

##while True:
##    sentence = input("10글자 이상의 문장을 입력하세요('quit'이 포함되면 종료): ")
##    if "quit" in sentence:
##        break
##    if len(sentence) < 10:
##        print("10글자 미만입니다")
##        continue
##    print(sentence[::-1])

##number = 1
##multi = 1
##
##while True:
##    number += 1
##    multi *= number
##    if multi >= 5000:
##        break
##print(number)
##print(multi)

num1 = 0 
while 0 <= num1 < 49:
    num1 += 1
    if num1 % 3 == 0 or num1 % 5 == 0: 
        continue
    print(num1, end=" ")
##    num1 += 1
##    if num1 > 1:        

num1 = int(input("숫자1 : "))
num2 = int(input("숫자2 : "))

while True:
    








        

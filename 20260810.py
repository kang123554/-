##num1 = int(input("첫 번째 숫자 입력 : "))
##num2 = int(input("두 번째 숫자 입력 : "))
##
##print(f"num1 + num2 = {num1 + num2}")
##print(f"num1 - num2 = {num1 - num2}")
##print(f"num1 * num2 = {num1 * num2}")
##print(f"num1 / num2 = {num1 / num2:.2f}")

##num1 = int(input("숫자를 입력해주세요 : "))
##
##print(num1 + 50)
##print(num1 - 50)
##print(num1 * 50)
##print(f"{num1 / 50:.3f}")
##
##print(f"{num1 + 50}")
##print(f"{num1 - 50}")
##print(f"{num1 * 50}")
##print(f"{num1 / 50:.3f}")

##w1 = 3
##w2 = 4
##h = 5
##print(f"사다리꼴의 넓이는 ({w1} + {w2}) * {h} / 2 = {(w1 + w2) * h / 2}")

##num1 = int(input("첫 번째 숫자 입력 : "))
##num2 = int(input("두 번째 숫자 입력 : "))
##
##print(f"num1 // num2 = {num1 // num2}")
##print(f"num1 % num2 = {num1 % num2}")
##print(f"num1 ** num2 = {num1 ** num2}")

##num1 = int(input("숫자를 입력해주세요 : "))
##
##print(f"{num1 // 4}")
##print(f"{num1 % 4}")
##print(f"{num1 ** 4}")

##num1 = int(input("몸무게(kg)를 입력하세요 : "))
##num2 = float(input("키(m)를 입력하세요 : "))
##
##print(f"BMI 지수는 {num1 / (num2 ** 2):.2f}")

##sec = int(input("초 입력 : "))
##min = sec // 60
##sec = sec % 60
##hour = min // 60
##min = min % 60
##day = hour // 24
##hour = hour % 24
##
##print(f"{day}일{hour}시간{min}분{sec}초")

##num1 = int(input("물건의 가격을 입력합니다 : "))
##price1 = 1000 - num1
##price2 = price1 // 500  
##price3 = price1 % 500   
##price4 = price3 // 100
##price5 = price3 % 100   
##price6 = price5 // 50   
##price7 = price5 % 50    
##price8 = price7 // 10   
##price9 = price7 % 10    
##
##print(f"500원 {price2}개")
##print(f"100원 {price4}개")
##print(f"50원 {price6}개")
##print(f"10원 {price8}개")

number = int(input("세 자리 숫자 입력 : "))
number1 = number % 10
number = number // 10
number10 = number % 10
number = number // 10
number100 = number % 10

print(f"백의 자리 : {number100}")
print(f"십의 자리 : {number10}")
print(f"일의 자리 : {number1}")










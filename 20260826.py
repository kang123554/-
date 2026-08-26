##print("숫자 1과 숫자 2를 입력해주세요.")
##number1 = int(input())
##number2 = int(input())
##
##if number1 > number2:
##    print("숫자 1이 숫자 2보다 큽니다.")
##else:
##    if number1 < number2:
##        print("숫자 2가 숫자 1보다 큽니다.")
##    else:
##        print("숫자 1과 숫자 2가 같습니다.")

##print("숫자 1과 숫자 2를 입력해주세요.")
##number1 = int(input())
##number2 = int(input())
##
##if number1 > number2:
##    print("숫자 1이 숫자 2보다 큽니다.")
##elif number1 < number2:
##    print("숫자 2가 숫자 1보다 큽니다.")
##else:
##    print("숫자 1과 숫자 2는 같습니다.")

##score = 75
##
##if score > 90:
##    print("성적은 A등급 입니다.")
##elif score > 80:
##    print("성적은 B등급 입니다.")
##elif score > 70:
##    print("성적은 C등급 입니다.")
##elif score > 60:
##    print("성적은 D등급 입니다.")
##else:
##    print("성적은 F등급 입니다.")

##weight = int(input('무게를 입력해주세요 : '))
##express = input('특송여부 (y/n) : ')
##domestic = input('국내 배송 여부 (y/n) : ')
##
##if weight <= 2 and (express=='y' or domestic=='y'):
##    print("무료 배송입니다.")
##if weight <= 5 and (express=='y' or domestic=='y'):
##    print("유료 배송입니다.")
##else:
##    print("배송 불가합니다.")

##player_atk = int(input("현재 공격력 : "))
##player_exp = 10
##monster_atk = 100
##
##if monster_atk > player_atk:
##    print("몬스터의 승리!")
##    print("경험치를 잃었다...")
##    player_exp -= 5
##elif monster_atk < player_atk:
##    print("플레이어의 승리!")
##    print("경험치를 얻었다...")
##    player_exp += 5
##else:
##    print("몬스터와 무승부...")
##    print("아무런 일도 일어나지 않았다.")
##
##print(f"현재 경험치 : {player_exp} / 다음 레벨업까지 : {100-player_exp}")

##print("[계산기 프로그램]")
##
##choice = input("연산자를 입력해주세요. (+,-,*,/): ")
##
##num1 = float(input("첫 번째 숫자 : "))
##num2 = float(input("두 번째 숫자 : "))
##
##if choice == '+':
##    result = num1 + num2
##    print(f"결과: {num1} + {num2} = {result}")
##elif choice == '-':
##    result = num1 - num2
##    print(f"결과: {num1} - {num2} = {result}")
##elif choice == '*':
##    result = num1 * num2
##    print(f"결과: {num1} * {num2} = {result}")
##elif choice == '/':
##    if num2 != 0:
##        result = num1 / num2
##        print(f"결과: {num1} / {num2} = {result}")
##    else:
##        print("오류: 0으로 나눌 수 없습니다.")
##else:
##    print("연산자를 잘못 입력하셨습니다.")
     
##num1 = int(input("숫자를 입력해주세요.(0~100) : "))
##
##if 45 < num1 < 55:
##    print("Perfect!!")
##elif 35 < num1 < 65:
##    print("Excellent!!")
##else:
##    print("Good!!")

##num1 = int(input("연도를 입력해주세요"))
##
##if num1 % 4 == 0 and num1 % 100 != 0:
##    print("윤년이 아닙니다.")
##elif num1 % 400 == 0:
##    print("윤년입니다.")

##print("연도를 입력해주세요")
##
##num1 = int(input())
##
##if num1 % 400 == 0 or (num1 % 4 == 0 and num1 % 100 != 0):
##    print("윤년입니다.")
##else :
##    print("윤년이 아닙니다.")

##num1 = int(input("첫번째 숫자를 입력해 주세요 : "))
##num2 = int(input("두번째 숫자를 입력해 주세요 : "))
##num3 = int(input("세번째 숫자를 입력해 주세요 : "))
##
##if num1 < num2:
##    if num2 < num3:
##        print(f"{num1} {num2} {num3}")
##    elif num1 > num3:
##        print(f"{num3} {num1} {num2}")       
##    else:
##        print(f"{num1} {num3} {num2}")        
##else: #num1 > num2 
##    if num2 > num3:
##        print(f"{num3} {num2} {num1}")
##    elif num1 < num3:
##        print(f"{num2} {num1} {num3}")
##    else:
##        print(f"{num2} {num3} {num1}")     

##if num3 > num2 > num1:
##    print(f"{num3} {num2} {num1}")
##elif num3 > num1 > num2:
##    print(f"{num2} {num1} {num3}")
##elif num2 > num1 > num3:
##    print(f"{num3} {num1} {num2}")
##elif num2 > num3 > num1:
##    print(f"{num1} {num3} {num2}")
##elif num1 > num2 > num3:
##    print(f"{num3} {num2} {num1}")
##else:
##    print(f"{num3} {num2} {num1}")

    












    











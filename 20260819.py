##num_ori = 1357
##num = num_ori
##num_ori //= 10 #135
##num %= 10      #7
##print(num)
##
##num = num_ori  #135
##num_ori //= 10 #13
##num %= 10      #5
##print(num)
##
##num = num_ori  #13
##num_ori //= 10 #1
##num %= 10      #3
##print(num)
##
##print(num_ori) #1 

##num1 = num % 10     #7
##num2 = num // 10    #135
##num3 = num2 % 10    #5
##num4 = num2 // 10   #13
##num5 = num4 % 10    #3
##num6 = num4 // 10   #1 
##
##print(num1)
##print(num3)
##print(num5)
##print(num6)

##txt1 = input("숫자 5개를 입력해주세요 : ").split()
##
##num1 = int(txt1[0])
##num2 = int(txt1[1])
##num3 = int(txt1[2])
##num4 = int(txt1[3])
##num5 = int(txt1[4])
##
##sum1 = num1 + num2 + num3 + num4 + num5
##count = len(txt1)
##avg = sum1/count
##
##print(f"{avg:.3f}")
##
##txt1 = input("문자열을 입력해주세요 : ").split()
##sen1 = txt1[0]
##sen2 = txt1[1]
##
##txt2 = (sen1[0]).upper() + (sen1[1:])
##txt3 = " " 
##txt4 = (sen2[0]).upper() + (sen2[1:])
##
##print(txt2 + txt3 + txt4)

##num1 = float(input("첫 번째 숫자 입력 : "))
##num2 = float(input("두 번째 숫자 입력 : "))

##print(f"num1 > num2 = {num1 > num2}")
##print(f"num1 < num2 = {num1 < num2}")

##print(f"num1 >= num2 = {num1 >= num2}")
##print(f"num1 <= num2 = {num1 <= num2}")

##print(f"num1 == num2 = {num1 == num2}")
##print(f"num1 != num2 = {num1 != num2}")

##num1 = float(input("첫 번째 숫자 입력 : "))
##num2 = float(input("두 번째 숫자 입력 : "))
##num3 = float(input("세 번째 숫자 입력 : "))
##
##ascending = num1 < num2 < num3
##descending = num1 > num2 > num3
##
####print(type(ascending),type(descending))
##print(f"num1<num2<num3 = {ascending}")
##print(f"num1>num2>num3 = {descending}")

##num1 = float(input("숫자를 입력해주세요 : "))
##num2 = 100
##
##print(f"{num1 < num2}")
##
##num1 = float(input("숫자를 입력해주세요 : "))
##num2 = 30
##num3 = 60
##
##print(f"{num2 < num1 < num3}")

##num1 = int(input("첫 번째 숫자 입력 : "))
##num2 = int(input("두 번째 숫자 입력 : "))

##print(f"둘 다 양수? = {num1 > 0 and num2 > 0}")
##print(f"하나라도 양수? = {num1 > 0 or num2 > 0}")

##print(f"num1은 0인가? = {not num1}")
##print(f"num2는 0인가? = {not num2}")

##num1 = int(input("첫 번째 숫자 입력 : "))
##num2 = int(input("첫 번째 숫자 입력 : "))
##
##print(f"""둘 다 0이 아니고 곱하면 양수인가? = {num1 != 0 and num2!= 0 and num1*num2 > 0}""")

##num1 = int(input("숫자를 입력해주세요 : "))
##print(f"{num1 == 0 or num1 == 10 or num1 == 100}")
##
##num1 = int(input("숫자를 입력해주세요 : "))
##print(f"{num1 == 0 or num1 == 10 or num1 == 100}")

##num1 = int(input("숫자를 입력해주세요 : "))
##print(f"{num1 != 0 and num1 % 2 != 0 or num1 % 8 == 0}")

##num1 = int(input("숫자를 입력해주세요 : "))
##print(f"{num1 != 0 and (num1 % 2 != 0 or num1 % 8 == 0)}")

















#產生一個1~100的隨機數字
#讓使用者重複去猜，
#錯了要跟他說比答案大還是小，對了要印出"終於答對了"

import random
answer = random.randint(1,100)
#print(r)
#userinput != answer
while True: 
	userinput = input('請輸入1~100的數字')
	userinput = float(userinput)
	if userinput == answer:
		print('你答對了！')
		break
	elif answer > userinput:
		print('答案比你輸入數值的大')
	elif answer < userinput:
		print('答案比你輸入數值的小')
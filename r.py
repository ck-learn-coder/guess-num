#產生一個1~100的隨機數字
#讓使用者重複去猜，
#錯了要跟他說比答案大還是小，對了要印出"終於答對了"

import random
start = input('請輸入隨機數字的起始值: ')
end = input('請輸入隨機數字的結束值: ')
start = int(start)
end = int(end)
answer = random.randint(start, end)
count = 0

while True: 
	count += 1
	userinput = input('請猜猜數字: ')
	userinput = int(userinput)
	if userinput == answer:
		print('你答對了！')
		print('你輸入了', count,'次')
		break
	elif answer > userinput:
		print('答案比你輸入數值的大')
	elif answer < userinput:
		print('答案比你輸入數值的小')
	print('你輸入了', count,'次')

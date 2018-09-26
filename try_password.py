i = 3
while True:
	password_try = input('請輸入密碼:')
	i = i - 1
	if password_try == 'a123456':
		print('恭喜答對了')
		break
	else:
		if i > 0:
			print('答錯了,剩下', i, '次機會')
		else:
			print('沒機會了!')
			break


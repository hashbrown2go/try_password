i = 2
password_try = input('請輸入密碼:')
while password_try != 'a123456':
	if i > 0:
		print('答錯了,剩下', i, '次機會')
		i = i - 1
		password_try = input('請輸入密碼:')
	else:
		print('沒機會了!')
		break
else:	
	print('恭喜答對了')	
driving = input('請問你有沒有開過車？')
age = input('請問你的年齡？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('你無照開車喔')
elif driving =='沒有':
	if age >= 18:
		print('你可以去找駕照')
	else:
		print('等你到18歲就可以考駕照了')
else:
	print('請輸入「有」或是「沒有」')
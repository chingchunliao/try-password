password = 'a123456'
i = 3
while True :
    pwd = input('請輸入密碼: ')
    if pwd == password :
        print('輸入正確')
        break
    else :
        i = i - 1
        print('你還有' , i , '次機會')
        if i == 0:
            break
d={}

print('歡迎進入系統~')

while True:
    print('1.建立詞彙')
    print('2.列出所有單字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗學習成果')
    print('6.離開系統')
    x=int(input('請輸入選項:'))
    
    if x==1:
        while True:
            a=input('請輸入英文單字(按0退出):')
            if a=='0':
                break
            b=input('請輸入中文意思:')
            d[a]=b
        
    elif x==2:
        print(d)
        
    elif x==3:
        while True:
            a=input('請輸入英文單字(按0退出):')
            if a=='0':
                break
            print(a,'的中文是',d[a])
        
    elif x==4:
        while True:
            b=input('請輸入中文(按0退出):')
            if b=='0':
                break
            for k,v in d.items():
                if v==b:
                    print(b,'的英文是',k)
        
    elif x==5:
        for k in d.keys():
            print('請問',k,'的中文是什麼?')
            a=input('請輸入答案:')
            if a==d[k]:
                print('答對了!')
            else:
                print('答錯啦!')
                
    elif x==6:
        print('bye~~')
        break
        
        
        

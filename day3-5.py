while True:
    print('------------------------------')
    print('1.加法')
    print('2.減法')
    print('3.乘法')
    print('4.除法')
    print('5.離開')
    x=int(input('請輸入選項:'))
    if x==5:
        print('Bye~~')
        break
    a=int(input('請輸入第一個數:'))
    b=int(input('請輸入第二個數:'))
    if x==1:      
        c=a+b
        print('Ans:',c)
    elif x==2:
        c=a-b
        print('Ans:',c)
   
    elif x==3:
        c=a*b
        print('Ans:',c)
    
    elif x==4:
        c=a/b
        print('Ans:',c)



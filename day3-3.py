names=[]
scores=[]
total=0
avg=0
highest=0
highest_name=''
lowest=999
lowest_name=''
n=int(input('請輸入班級總人數:'))
for a in range(n):
    name=input('請輸入你的名字:')
    score=int(input('請輸入你的分數:'))
    names.append(name)
    scores.append(score)
print(scores)

def avg(scores,n):
    total=0
    for i in scores:
        total=total+i
    a=total/n
    return a
print('平均是:',avg(scores,n))

def high(n,scores,names):
    highest=0
    for i in scores:
        if i>highest:
            highest=i           
    return highest
print('最高分為:',high(n,scores,names),'分')

def low(n,scores,names):
    lowest=99999
    for x in scores:
        if x<lowest:
            lowest=x   
    return lowest
print('最低分為:',low(n,scores,names),'分')












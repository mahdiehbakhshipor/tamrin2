import math
while True:
    a = int(input())
    b = int(input())
    print('wellcome to sajjadb univercity ')
    print('1) jam')
    print('2) afright')
    print('3) zarb')
    print('4) taghsim')
    print('5) sin')
    print('6) cos')
    print('7) tan')
    print('8) cot')
    print('9) log')
    op=input()

    if op=='jam':
        result=a+b
        print(result)
    elif op=='afright':
        result=a-b
        print(result)
    elif op=='zarb':   
        result=a*b  
        print(result)
    elif op=='taghsim':
     if b !=0:
        result=a/b 
        print(result)
     else:
        result='error'
        print(result)
    elif op=='sin':
        p=(a*3.14)/180
        result=math.sin(p)
        print(p)
    elif op=='cos':
        p=(a*3.14)/180
        result=math.cos(p)
        print(p)
    elif op=='tan':
        p=(a*3.14)/180
        result=math.tan(p)
        print(p)
    elif op=='cot':
        p=(a*3.14)/180
        result=1/math.tan(p)
        print(p)
    elif op=='log':
        result=math.log(a)
        print(result)
    elif op=='exit':
        break
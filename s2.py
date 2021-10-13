[۱۶:۱۱, ۱۴۰۰/۷/۲۱] My Love: import random
# score
Score = {
    'HumanScore': 0,
    'pc1Score': 0,
    'pc2Score': 0,
}

Select = {
    'Human': 0,
    'pc1': 0,
    'pc2': 0,
}

for i in range(5):
    print('------------------')
    print('You={}  vs  PC1={}  vs  PC2={}'.format(
        Score['HumanScore'], Score['pc1Score'], Score['pc2Score']))
    print('Select one...')
    print('1. Up')
    print('2. Down')
    Select['Human'] = int(input())
    Select['pc1'] = random.randint(1, 2)
    Select['pc2'] = random.randint(1, 2)
    print('h={}  pc1={}  pc2={}'.format(
        Select['Human'], Select['pc1'], Select['pc2']))

    if(Select['Human'] != Select['pc1'] and Select['Human'] != Select['pc2']):
        Score['HumanScore'] += 1

    if(Select['pc1'] != Select['Human'] and Select['pc1'] != Select['pc2']):
        Score['pc1Score'] += 1

    if(Select['pc2'] != Select['pc1'] and Select['pc2'] != Select['Human']):
        Score['pc2Score'] += 1
[۱۶:۱۵, ۱۴۰۰/۷/۲۱] My Love: import random
i=0
u=0
c=0
while(i<5):
    print('Enter the number of your sellection: ')
    print('1. sang')
    print('2. kaqz')
    print('3. gheichi')
    a=int(input())
    b=random.randint(1,3)
    if((a==1 and b==3) or (a==2 and b==1) or (a==3 and b==2)):
        u += 1
    elif((b==1 and a==3) or (b==2 and a==1) or (b==3 and a==2)):
        c += 1
    print("User: ",u)
    print("Computer: ",c)
    i += 1
if(u>c):
    print("User WON!!")
elif(c>u):
    print("Computer WON!!")
elif(c==u):
    print("DRAW!!!")
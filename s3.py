import random
i=0

def w_sh(shoma,com1,com2):
    if(shoma=='posht' and com1=='roo' and com2=='roo') or (shoma=='roo' and com1=='posht' and com2=='posht'):
        return True
def w_com1(shoma,com1,com2):
    if( shoma=='posht' and  com1=='roo' and com2=='posht') or ( shoma=='roo' and com1=='posht' and com2=='roo'):
        return True
def w_com2(shoma,com1,com2):
    if(shoma=='roo' and com1=='roo' and com2=='posht') or ( shoma=='posht' and com1=='posht' and com2=='roo'):
        return True
def papupi(c1,c2,p):
    shoma=input('posht ya roo ? ')
    choices=["roo","posht"]
    com1=random.choice(choices) 
    print('com1 = ',com1)       
    com2=random.choice(choices)
    print('com2 = ',com2)

    if(shoma==com1 and shoma==com2):
        return print('barande nadasht')
    if w_sh(shoma,com1,com2):
        p[0]+=1
        return print('shoma barande shodid :) ')
    if w_com1(shoma,com1,com2):
        c1[0]+=1
        return print('computer 1 barande shod ')
    if w_com2(shoma,com1,com2):
        c2[0]+=1
        return print('computer 2 barande shod ')

nc1=[0]
nc2=[0]
nc3=[0]

while(i<5):
    papupi(nc1,nc2,nc3)
    i+=1
print("\n\nemtiaz shoma: ", nc3 ,"\temtiaz computer 1 : ", nc1 ,"\temtiaz computer 2 : ", nc2,"\n\n")
if (nc3 > nc1 and nc3> nc2) or (nc2 == nc1 and nc3> nc2):
    
    print(" barande bazi : shoma hastid  ")   

if (nc3 < nc1 and nc1> nc2) or (nc3 == nc2 and nc3< nc1):
    
    print("  barande bazi : computer 1 ast  ")   

if (nc2 > nc1 and nc3< nc2) or (nc3 == nc1 and nc3< nc2):
    
    print(" barande bazi : computer 2 ast ")

if (nc3 == nc1 and nc3> nc2):
    
    print(" barande bazi : shoma  va computer 1 hastid  ")  

if (nc2 == nc1 and nc3< nc2):
    
    print("  barande bazi : computer 1 va computer 2 hastand ")

if (nc3 == nc2 and nc3> nc1):
    
    print(" barande bazi : shoma va computer 3 hastid ")

if (nc3 == nc2 and nc3 == nc1):
    
    print(" hame mosavi shodin va barande nadarim... ")
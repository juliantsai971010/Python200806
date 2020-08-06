import os.path

d={}

if os.path.isfile('hello.txt'):
    fo=open('hello.txt','r')
    print('old')
else:
    print('new')
    fo=open('hello.txt','w')
def menu():
    print('1.add score')
    print('2.show all the score')
    print('3.find the score')
    print('4.離開')
'''
for row in fo.readlines():
    d=row.split(':')
    k=d[0]
    v=d[1]
    d[k]=v
    print(d)
'''

            
    
while True:
    menu()
    a=input('enter')
    a=int(a)
   


    
    if a==1:
        k=input('name')
        v=input('score')
        d[k]=v


        print(d)
 
        
       
    elif a==2:
        
        print(d)
        
        
    elif a==3:
        b=input('name')
        print(d[b])
        
        
    else:
        break

        
fo=open('hello.txt','w')
for A,B in d.items():
    fo.write(A)
    fo.write(':')
    fo.write(B)
    fo.write('\n')
            
        
fo.close()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

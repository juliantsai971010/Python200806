import os.path


if os.path.isfile('hello.txt'):
    print('存在')
else:
    print('不存在')
fo=open('hello.txt')
fo=open('hello.txt','w')
fo.write('hello')
fo=open('hello.txt','r')
fo.read()   
print(fo) 
fo.close()

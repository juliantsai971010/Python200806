file=open('1.png','rb')
img=file.read()
file.close()
file=open('2.png','wb')
img=file.write(img)
file.close()
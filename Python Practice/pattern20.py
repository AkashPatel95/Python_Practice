'''
A  
B C  
D E F  
G H I J  
K L M N O  
P Q R S T U  
V W X Y Z [ \ 
'''

ascii_number=65

n=7

for i in range(0,n):
    for j in range(0,i+1):
        char=chr(ascii_number)
        print(char,end=' ')
        ascii_number+=1
    print("")
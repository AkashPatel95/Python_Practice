'''
            A  
           B C  
          D E F  
         G H I J  
        K L M N O  
       P Q R S T U  
      V W X Y Z [ \ 
'''

rows = 7 
current_char = 65  

for i in range(1, rows + 1):
   
    print(" " * (rows - i), end="")

  
    for j in range(1, i + 1):
        print(chr(current_char), end=" ")
        current_char += 1

    print() 

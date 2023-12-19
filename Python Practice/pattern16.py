'''
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9
'''

n=5

for i in range(1,2*n,2):
    for j in range((i//2)+1):
        print(i,end=' ')
    print("")

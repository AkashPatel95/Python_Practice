'''
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1
'''

n=5

for i in range(0,n):
    for j in range(0,n-i+1):
        print(j,end=' ')
    print("")
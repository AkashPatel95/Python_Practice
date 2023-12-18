#Python: Map two lists into a dictionary

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']

dict1={}

for i in range(0,len(keys)):
    dict1[keys[i]]=values[i]

print(dict1)
#Python – All pair combinations of 2 tuples
from itertools import chain, product
test_tuple1=(7,2)
test_tuple2=(7,8)

new_tuple=list(chain(product(test_tuple1,test_tuple2),product(test_tuple2,test_tuple1)))

for i in new_tuple:
    print(i)
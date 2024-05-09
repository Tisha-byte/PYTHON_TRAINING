#iterator tool 1)infinite=>count(start,step),cycle(),repeat() 2)combinatoric 3)terminating
import itertools
for i in itertools.count(10,5):      #count(start,step)
    if i==50:
        break
    else:
        print(i,end=" ")
#cycle()
count=0
for i in itertools.cycle('123'):      #cycle
    if(count>8):
        break
    else:
        print(i,end=" ")
        count=count+1
#repeat()
print(list(itertools.repeat(40,15)))

#2)combinatoric =>permutation,combination
#product
from itertools import product
print(list(product([1,2,3],repeat=4)))
print()

#permutation
from itertools import permutations
print(list(permutations([3,"python"],2)))

#combination
from itertools import combinations
print(list(combinations([3,"python"],2)))

#combination with replacement
from itertools import combinations_with_replacement
print(list(combinations_with_replacement("XY",3)))

#terminating
#1)accumulate
import itertools
import operator
list1=[1,4,5,7,9,11]
print(list(itertools.accumulate(list1)))
print(list(itertools.accumulate(list1,operator.mul)))

#chain
import itertools
list1=[12,3,4,6,7]
list2=[1,2,3,4,5]
list3=[21,32,43,54,65]
print(list(itertools.chain(list1,list2,list3)))

#dropwhile
import itertools
list1=[2,4,5,7,8]
print(list(itertools.dropwhile(lambda x:x%2==0,list1)))

#filterfalse
import itertools
list1=[12,14,15,27,28]
print(list(itertools.filterfalse(lambda x:x%2==0,list1)))

#islice
import itertools
list1=[12,14,15,27,28,33,23,45,67]
print(list(itertools.islice(list1,2,8,2)))





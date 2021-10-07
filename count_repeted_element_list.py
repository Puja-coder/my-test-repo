#Method 1:
from collections import Counter
list1 = ['x','y','z','x','x','x','y', 'z']
print(Counter(list1))

#Method 2:
list1 = ['x','y','z','x','x','x','y', 'z']
res = {i : list1.count(i) for i in set(list1)} 
print ("The count of all characters in list is : \n" + str(res))

#Method 3:
list1 = ['x','y','z','x','x','x','y', 'z']
for i in set(list1):
	print(i, ":", list1.count(i))

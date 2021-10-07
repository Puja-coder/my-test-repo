#Method 1:
from collections import Counter
str1 = "india"
print(Counter(str1))

#Method 2:
test_str = "india"
res = {i : test_str.count(i) for i in set(test_str)} 
print ("The count of all characters in string is : \n" + str(res))

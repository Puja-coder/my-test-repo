#Method 1:
Mystr ="myteststring"
print(Mystr[::-1])

#Method 2:
str1 = "myteststring"
str2= ""
i = len(str1)-1
while i >= 0:
    str2 = str2 + str1[i]
    i = i-1
print(str2)

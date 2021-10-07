
the_list = [1,2,True,3,5,5,'string1',5.6,8,6,3,2.1,'string2']
the_list1 =[]

for item in the_list:
    if type(item) is int:
        the_list1.append(item)
l = [the_list1[i:i+3] for i in range(0, len(the_list1), 3)]
print(l)

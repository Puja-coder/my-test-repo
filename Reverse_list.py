#Method 1:

MyList = ["a", "b", "a", "c", "c", "a", "c"]
print(MyList[::-1])

#Method 2:
MyList =  ["a", "b", "a", "c", "c", "a", "c"]
MyList1= []
i = len(MyList)-1
while i >= 0:
    MyList1.append(MyList[i])
    i = i-1
print(MyList1)

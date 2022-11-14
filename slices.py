list1 = [1, 2, 3, 4, 5]
list2 = list1[0:3]
print(list2)
list3 = list1[3:len(list1)]
list4 = list2 + list3
print(list3)
print("Is list4 the same as list1?")

strHello = "Hello, World!"
substr = strHello[0:5]
print(strHello)
print(strHello[-1])
print(strHello[-6:-1])
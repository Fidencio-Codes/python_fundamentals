# myList = ['a', 'b', 'c', 'd', 'e']
# print(myList[:-1])

l = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz&']

# from 'vwx' so -2;to 'def' just before 'abc' so -9; backwards all so -1.
l[-2:-9:-1]
print(l)
# ['vwx', 'stu', 'pqr', 'mno', 'jkl', 'ghi', 'def']

# For the same 'vwx' 7 to 'def' just before 'abc' 0, backwards all -1
l[7:0:-1]
print(l)
# ['vwx', 'stu', 'pqr', 'mno', 'jkl', 'ghi', 'def']

# Slicing lists
print(l[1:5])
print(l[3:9:2])
print(l[-2::-1])
print(l[-1::-1])
print(l[1::-1])
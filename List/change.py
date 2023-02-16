thislist = ["aaaa", "bbbb", "cccc"]
thislist[1]="dddd"
print(thislist)

thislist1 = ["aaaa", "bbbb", "cccc", "dddd", "eeee", "ffff"]
thislist1[1:3]=["gggg","hhhh"]
print(thislist1)

thislist2 = ["apple", "banana", "cherry"]
thislist2[1:3] = ["watermelon"]
print(thislist2)

thislist3 = ["apple", "banana", "cherry"]
thislist3.insert(2,"mango")
print(thislist3)
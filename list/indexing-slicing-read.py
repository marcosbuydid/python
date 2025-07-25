l = [6, 7, 8, 9, 10]
l1 = [12, 45, 23, 15, 67]

# indexing-read
print(l[4])  # 10
print(l[-1])

# slicing-read
print(l[2:5])  # [8,9,10]
print(l1[0:4:2])  # [12,23]

# indexing-write
l[2] = 4  # [6, 7, 4, 9, 10]

# slicing-write
l1[3:4:1] = [56, 67, 90]  # [12, 45, 23, 56, 67, 90, 67]

l1[1:4] = [55, 88, 99]  # [12, 55, 88, 99, 67, 90, 67]

l1[3:0:-1] = [25, 98, 99]  # [12, 99, 98, 25, 67, 90, 67]

studentList = ["hasan","mamad","ali","hosein",
               "soheil","soroush","arman","mojtaba","ali"]

# Count (video)
print(studentList.count("ali"))

# Len
print(len(studentList))

# Append
print(studentList.append("mamadHasan"))

# Insert
print(studentList.insert(0,"mamadHosain"))

# Index
print(studentList.index("mamadHasan"))
print(studentList.index("mamadHosain"))

# Slice (video)
print(studentList[0:4])
print(studentList[5:10])

# Remove
print(studentList.remove("mamadHosain"))
print(studentList)

# Pop
print(studentList.pop())
print(studentList)

# Del (video)
del studentList[0]
print(studentList)


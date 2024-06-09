#
# num = 3
# for i in range(1, num+1):
#     print(" "*(2*num-i+3), end="")
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()

# x = 8
# for i in range(1, 7):
#     print(" " * (8 - i), end="")
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

x = 8
for i in range(1, 7):
    print(" " * (x - i), end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
for k in range(1, 4):
    print("      * *     ")
############## Logical Operators
#1
a = 5
b = 10
print(a > 0 and b > 0)

#2
x = 1
y = 7
z = x + y
print(x > 0 and z == 10)

#3
m = 15
n = 10
print(m > n and n == 10)

############## Conditions
#1
num = int(input("یک عدد وارد کنید: "))
if(num % 2 == 0):
    print("عدد زوج است")
else:
    print("عدد فرد است")

#2
num = int(input("یک عدد وارد کنید: "))
if num > 0:
    print("عدد مثبت است")
elif num < 0:
    print("عدد منفی است")
else:
    print("عدد صفر است")

#3
a = 15
b = 25
c = 20
if a > b and a > c:
    print("a بزرگ‌ترین است")
elif b > a and b > c:
    print("b بزرگ‌ترین است")
else:
    print("c بزرگ‌ترین است")

#4
price = int(input("what range of price to buy phone? "))
if price < 10000000:
    print("Poco m5s")
elif price < 20000000:
    print("Poco x6 Pro")
elif price < 4000000
    print("iPhone 15")
else:
    print("iPhone 13 Pro Max")

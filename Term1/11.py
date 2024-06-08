#نوشتن در فایل
with open("example.txt","w",encoding="utf-8") as file:
    file.write("Hello World")

#خواندن از فایل
with open("example.txt","r", encoding="utf-8") as file:
    content = file.read()
    print(content)

#افزودن متن به فایل
with open("example.txt","a",encoding="utf-8") as file:
    file.write("what's up?")

#خواندن خط به خط از فایل
with open("example.txt","r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

#استفاده از try except برای مدیریت خطا
try:
    with open("test.txt","r", encoding="utf-8") as file:
        content = file.read()
        print()
except FileNotFoundError:
    print("file not found!")

#استفاده از try except برای مدیریت خطاهای مختلف
try:
    with open("test.txt","r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file not found!")
except Exception as ex:
    print(ex)

#ایجاد خطای سفارشی
try:
    user = input("Username: ").lower()
    if user != "admin":
        raise ValueError("User isn't admin!")
    print(user)
except Exception as ex:
    print(ex)

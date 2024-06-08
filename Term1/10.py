student = {"name":"Ali", "age":20, "major":"Computer"}

#ایجاد و دسترسی به مقادیر
print(student["name"])
print(student["age"])
print(student["major"])

#اضافه کردن و بروزرسانی مقادیر
student["grade"] = 18.5
student["age"] = 21

#استفاده از متودهای دیکشنری
print(student.keys())
print(student.values())
print(student.items())

#حذف یک آیتم
del student["major"]
print(student)

#بررسی وجود یک کلید
if "grade" in student:
    print("The word 'grade' was found in 'student' dictionary!")
else:
    print("The word 'grade' didn't found in 'student' dictionary!")

#پیمایش در دیکشنری
for key,value in student.items():
    print(f"{key}: {value}")

#کپی کردن دیکشنری
student_copy = student.copy()
student_copy["name"] = "reza"
print("دیکشنری اصلی:", student)
print("دیکشنری کپی:", student_copy)
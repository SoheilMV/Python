############### variables
#1
name = "ali"
print(name)

#2
a = 10
b = 20
c = a + b
print(c)

# mohit mostatil       2*(w+h)
# masahat mostatil     w*h

# daiere mohit  2pr
# daiere pr*r

############### datatype
integer_var = 100
float_var = 3.14
string_var = "Hello"
boolean_var = True
print(type(integer_var))
print(type(float_var))
print(type(string_var))
print(type(boolean_var))


############### typecast
#1
num_str = "123"
num_int = int(num_str)
print(num_int + 10)

#2
float_str = "3.14"
num_float = float(float_str)
print(num_float + 2.0)


############### input
#1
name = input("نام خود را وارد کنید: ")
print("سلام " + name)

#2
num1 = float(input("عدد اول را وارد کنید: "))
num2 = float(input("عدد دوم را وارد کنید: "))
print("جمع: ", num1 + num2)
print("تفریق: ", num1 - num2)
print("ضرب: ", num1 * num2)
print("تقسیم: ", num1 / num2)

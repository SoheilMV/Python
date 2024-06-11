############## string methods

#1 F-string
message = "Hello World"
print(f"{message} is first project")

#2 Format
message = "Hello {0}"
print(message.format("World"))

#3 Split
message = "Hello:World"
print(message.split(':'))

#4 Strip
message = "  Hello World  "
print(message.strip())

#5 Upper
message = "Hello World"
print(message.upper())

#6 Lower
message = "Hello World"
print(message.lower())

#7 Capitalize
message = "hello world"
print(message.capitalize())

#8 Replace
message = "Hello w"
print(message.replace("w", "World"))

#9 Title
message = "hello world"
print(message.title())

#10 Count
message = "Hello World"
print(message.count('o'))

#11 Start With
message = "Hello World"
print(message.startswith("Hello"))

#12 End With
message = "Hello World"
print(message.endswith("World"))

# barname benvisim k az karbar jomle daryaft kone va
# Harf aval kalame aval bozorg bashe.
# space haye aval va akhar pak beshe.
# agar char '-' didi ba ',' avaz kon.
# agar '//n' dar jomle bud ba '/n' avaz kon.

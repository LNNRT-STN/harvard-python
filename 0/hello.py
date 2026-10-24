#first lesson starten on 14/10/26, disabled all AI help inside VSCODE

print_var="hello! world!"
print(print_var)

#space for aestethic cursor
print("what is your name? ")
name = input()
print("Hello, "+name)

#here no space needed
print("Hello,",name)

#str means string

#using arguments in functions, parameters
#use docs.python.org
print("hello")
print(name,end="???")

#most recent way of doing the printing with variable
print(f"hello, {name}")

name = "lennart"
name = name.strip()
print(name)

#overwrite the newline usual behaviour of print
#you can use 'end' aswell, be consistent
print("hello, ",end="")
print("lennart")

#paramters vs named parameters

print('hello, "friend"')
print("hello, \"friend\"")

print(f"hello,{name}")

#stopped at 46 minutes
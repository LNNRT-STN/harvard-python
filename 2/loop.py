i = 0

while i < 3:
    print("hi "+str(i))
    i = i+1

#you can use _ instead of i
for i in range(3):
    print("meow")

#other method, end doesn't add a line break after the final line
print("other method\n" * 3, end="")


while True:
    n = int(input("what's n \n"))
    if n < 0:
        continue
    else:
        break
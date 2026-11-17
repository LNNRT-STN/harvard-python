
def main():
    x = int(input("what's x "))
    is_even(x)


def is_even(n):
    if n % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")


main()
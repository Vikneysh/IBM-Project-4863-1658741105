#Write a python prg to display prime number series up to given number

def is_prime(n):
    return 0 not in [n%i for i in range(2,(n//2)+1)]
num = int(input("Enter the number: "))
[print(n, end = " ") if(is_prime(n)) else() for n in range(2, num)]



#Write a python prg to test a given number is prime or not.
n = int(input("Enter a number : "))
print("Its a Prime Number") if( n != 1 and 0 not in [n%i for i in range(2,n//2+1)]) else print("Not a Prime")

#Write a program to generate odd numbers from m to n using while loop
m = int(input("Enter value for m:"))
n = int(input("Enter value for n:"))

while m <= n:
    if(m%2!=0):
        print(m)
    m += 1
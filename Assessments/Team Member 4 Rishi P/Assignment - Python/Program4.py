def main():
    n=int(input("Enter the value of n: "))
    a=-1
    b=1
    print("Fibonacci Series:\n")
    i=0
    while(i<n):
        t=a+b
        a=b
        b=t
        print(t)        
        i+=1


if __name__ == "__main__":
    main()

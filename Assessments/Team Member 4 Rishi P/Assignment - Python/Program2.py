def main():
    m = int(input("Enter m: "))
    n = int(input("Enter n: "))
    if(m>n):
        print("m value is greater than n. Please check!")
    while(m<=n):
        if(m%2!=0):
            print(m)
        m=m+1

if __name__ == "__main__":
    main()

def fibonacciSeries(n):
    a=-1
    b=1
    print("Fibonacci Series:\n")
    for i in range(0,n):
        t=a+b
        a,b=b,t
        print(t)
if __name__ == "__main__":
    n = int(input("Enter the number: "))
    fibonacciSeries(n)
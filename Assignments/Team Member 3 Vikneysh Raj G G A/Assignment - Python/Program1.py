
def primecheck(num):
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        return flag
        
    
def main():
    num = int(input("Enter the number: "))
    flag=primecheck(num)
    if flag:
        print(num, "is not prime")
    else:
        print(num, "is prime")
    
if __name__ == "__main__":
    main()

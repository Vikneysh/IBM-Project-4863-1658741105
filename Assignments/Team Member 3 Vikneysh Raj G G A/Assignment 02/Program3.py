
def primecheck(num):
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        return flag
        
    
def main():
    n = int(input("Enter the number: "))
    for num in range(0,n):
        flag=primecheck(num)
        if flag==False:
            print(num)
    
if __name__ == "__main__":
    main()

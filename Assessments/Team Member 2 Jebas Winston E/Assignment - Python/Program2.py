start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
while start <= end:
    if(start%2 != 0):
        print("{0}".format(start))
    start = start + 1
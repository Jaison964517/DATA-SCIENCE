start = int(input("enter the start number"))
end = int(input("enter the end number"))
notprime = []
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                notprime.append(num)

                break
print("no prime between", start, "and", end, "are:")
print(notprime)

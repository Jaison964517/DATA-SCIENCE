lo =int(input("Enter lower range:"))
up=int(input("Enter upper range:"))
for no in range(lo , up +1):
    od =len(str(no))
    sum = 0
    temp = no
    while temp > 0:
        digit = temp % 10
        sum += digit ** od
        temp //= 10
    if no == sum:
        print(no)

#
# loer =int(input("Enter lower no:"))
# upper = int(input("Enter upper no:"))
# for num in range (loer,upper +1):
#     order =len(str(num))
#     temp = num
#     sum = 0
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 10
#         temp //= 10
#     if num == sum:
#         print(num)



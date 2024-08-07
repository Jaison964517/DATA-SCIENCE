# no =int(input("Enter a number:"))
# s_of_fact =0
# for i in range (1 , no):
#     if no% i==0:
#         s_of_fact +=1
# if s_of_fact ==no:
#     print(no,"is perfect no")
# else:
#     print(no,"not perfect no")


n =int(input("enter no:"))
sofn =0
for i in range(1, n):
    if n%i==0:
        sofn +=1
if sofn==n:
    print(n,"perfect no")
else:
    print(n,"not perfect no")


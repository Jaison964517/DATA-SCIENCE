r = int(input("Enter the number of elements: "))
elements = []
print("Enter the elements:")
for i in range(r):
    num = int(input())
    elements.append(num)
print("Original array:", elements)
n = len(elements)
for i in range(n):

    for j in range(0, n-1):

        if elements[j] > elements[j+1]:
            elements[j], elements[j+1] = elements[j+1], elements[j]
print("Sorted array:", elements)
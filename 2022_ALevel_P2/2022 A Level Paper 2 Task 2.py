#Task 2
import random

#Task 2.1

def task2_1():
    lst = []
    for i in range(100):
        lst.append(random.randint(1,100))

    return lst

unsorted_lst = task2_1()
print(unsorted_lst)


#Task 2.2

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1],lst[j]
    
    return lst
    



#Task 2.3

def merge_sort(lst):
    n = len(lst)

    if n <= 1:
        return lst
    mid = n // 2
    
    a = lst[:mid]
    b = lst[mid:]

    a = merge_sort(a)
    b = merge_sort(b)
    
    lst = merge(a,b)
    return lst
    


def merge(a,b):
    j = 0
    k = 0
    c = []

    while j < len(a) and k < len(b) :
        if a[j] > b[k]:
            c.append(b[k])
            k += 1
        else:
            c.append(a[j])
            j += 1

    while j < len(a):
        c.append(a[j])
        j += 1

    while k < len(b):
        c.append(b[k])
        k += 1

    return c


print()

valid = False
while valid == False:
    sorting_method = input("Enter the sorting method you would like to use(bubble/merge): ")
    if sorting_method == 'bubble' or sorting_method == 'merge':
        valid = True
        
print()

if sorting_method == 'bubble':
    sorted_lst = bubble_sort(unsorted_lst)
    print(sorted_lst)
else:
    sorted_lst = merge_sort(unsorted_lst)
    print(sorted_lst)


print()
#Task 2.4

low = 0
high = len(sorted_lst)
def binary_search(num,low,high):
    while low <= high:

        mid = (high + low)//2

        if sorted_lst[mid] == num:
            return mid
    
        if num > sorted_lst[mid]:
            low = mid +1
            high = high
            return binary_search(num,low,high)
        else:
            low = low
            high = mid -1
            return binary_search(num,low,high)
    else:
        return -1

num = int(input("Enter the number you are searching for: "))

position = binary_search(num,low,high)
if position == -1:
    print("Not found")
else:
    print(position)


#Task 1.1

def push(stack,topPointer,data_item):
    if (topPointer+1) >= len(stack):
        stack.append(data_item)
    else:
        stack[topPointer+1] = data_item

    topPointer += 1
    return topPointer

#Task 1.2

def pop(stack,topPointer):
    if topPointer == -1:
        return False
    data_item = stack[topPointer]
    topPointer -= 1
    return data_item,topPointer

#Task 1.3

def main():
    stack = []
    topPointer = -1

    number = int(input("Enter the number: "))

    while number != 0:
        remainder = number % 2
        result = push(stack,topPointer,remainder)
        topPointer = result
        number = number // 2

    binary_str = ''

    count = 0
    while pop(stack,(topPointer)) != False:
        data_item,topPointer = pop(stack,(topPointer))
        binary_str += str(data_item)
        count += 1

    if count < 8:
        count = 8
        n = len(binary_str)
        binary_str = ((count-n)*'0') + binary_str
    return binary_str


print(main())
print(main())
print(main())

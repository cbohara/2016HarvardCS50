def main():
    x = 1
    y = 2

    print("x is " + str(x))
    print("y is "+ str(y))
    print("swapping...")
    swap(x, y)
    print("swapped")
    print("x is " + str(x))
    print("y is " + str(y))

def swap(a, b):
    temp = a
    a = b
    b = temp

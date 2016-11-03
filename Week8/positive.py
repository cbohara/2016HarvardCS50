def main():
    i = get_positive_int()
    print(str(i) + " is a positive integer")

def get_positive_int():
    while True:
        print("Input positive integer: ", end="")
        n = input()
        if int(n) >= 1:
            break
    return n

if __name__ == "__main__":
    main()

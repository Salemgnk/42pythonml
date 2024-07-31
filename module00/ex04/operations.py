import sys

def print_operations(a, b):
    try:
        print("Sum:\t\t", a + b)
        print("Difference:\t", a - b)
        print("Product:\t", a * b)
        print("Quotient:\t", a / b)
        print("Remainder:\t", a % b)
    except ZeroDivisionError:
        print("Divison by zero is impossible")

def main():
    if len(sys.argv) != 3:
        print("Incorrect number of argument")
    else:
        if sys.argv[1].isnumeric() == False or sys.argv[2].isnumeric() == False:
            print("Arguments must be numbers")
        else:
            a, b = int(sys.argv[1]), int(sys.argv[2])
            print_operations(a, b)

if __name__ == "__main__":
    main()
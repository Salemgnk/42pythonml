import sys

def number_checker(num):
    try:
        num = int(num)
        if num == 0:
            print("I'm Zero.")
        elif num % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")

def main():
    if len(sys.argv) > 2:
        print("AssertionError : more than one argument are povided")
    else:
        number_checker(sys.argv[1])

if __name__ == "__main__":
    main()

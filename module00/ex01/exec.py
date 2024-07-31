import sys

def revalpha(string):
   return string[::-1].swapcase()

def main():
    if len(sys.argv) < 2:
      print("Usage: python3 exec.py <string>")
      return
    else:
        input = " ".join(sys.argv[1:])
        print(revalpha(input))
        return


main()
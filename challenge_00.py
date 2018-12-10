import sys

count = 0

def add(addNumber):
    global count
    global stack
    count = count + int(addNumber)

def subtract(number):
    global count
    count = count - int(number)

def main():
    for line in sys.stdin:
        if (line[0] == '+'):
            add(line[1:])
        else:
            subtract(line[1:])
    print(count)

if __name__== "__main__":
  main()

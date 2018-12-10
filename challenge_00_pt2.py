import sys

count = 0
stack = []

def add(addNumber):
    global count
    count = count + int(addNumber)

def subtract(number):
    global count
    count = count - int(number)

def main():
    global count
    global stack
    found = 0
    firstLine = 0
    lines = sys.stdin.readlines()

    while(found == 0):
        for line in lines:
            # print("This is the line: " + line)
            if (line[0] == '+'):
                add(line[1:])

            else:
                subtract(line[1:])


            if(count in stack):
                found = 1
                break
            else:
                if(firstLine != 0):
                    stack.append(count)
                    # print(count)
                else:
                    firstLine = 1
                    continue
    print(count)

if __name__== "__main__":
  main()

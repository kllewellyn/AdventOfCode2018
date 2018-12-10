import sys
import collections

twos = 0
threes = 0

def main():
    global twos
    global threes

    for line in sys.stdin:
        results = collections.Counter(line)
        if (2 in results.values()):
            twos += 1
        if (3 in results.values()):
            threes += 1
    print(twos * threes)



if __name__== "__main__":
  main()

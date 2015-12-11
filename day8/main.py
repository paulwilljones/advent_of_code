import json

def main():

    a = 0
    b = 0

    def calculate(s):
        print s
        print s[:-1]
        print eval(s)
        print len(s[:-1])
        print len(eval(s))
        print sum(len(s[:-1]) - len(eval(s)))

    def another(s):
        print sum(2+s.count('\\')+s.count('""'))

    for line in open("input.txt"):
        calculate(line)
        another(line)


    #for line in open("input.txt"):
    #    a += len(line) - 1 - len(eval(line))
    #    b += len(json.dumps(line)) - len(line) - 1
    #    print line
    #    print eval(line)
    #    print json.dumps(line)

    #print(a)
    #print(b)
    #print b+a

if __name__ == "__main__":
    main()
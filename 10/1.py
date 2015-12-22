import sys

def readaloud(number):
    out = []
    while number != []:
        seed = number.pop(0)
        reps = 1
        while True:
            try:
                nxt = number[0]
            except IndexError:
                out += [str(reps),seed]
                break

            if nxt == seed:
                reps += 1
                del number[0]
            else:
                out += [str(reps),seed]
                break
    return out

number = list(sys.argv[1])
for i in range(int(sys.argv[2])):
    print(i)
    number = readaloud(number)

print(len(number))

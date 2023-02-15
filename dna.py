import csv
import sys


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    source_data = []
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        for row in reader:
            source_data.append(row)

    with open(sys.argv[2], 'r') as sub_data:
        seq = sub_data.read()

    sub_strs = []
    for i in range(1, len(source_data[0])):
        v = max_repeat(seq, source_data[0][i])
        sub_strs.append(v)

    print(match(source_data, sub_strs))
    sys.exit(0)


def max_repeat(string, shtr):
    c = 0
    repeats = []
    for i in range(0, len(string)):
        if string[i:i + len(shtr)] == shtr and string[i + len(shtr): i + len(shtr) + len(shtr)] == shtr:
            c += 1
        elif string[i:i + len(shtr)] == shtr and not string[i + len(shtr): i + len(shtr) + len(shtr)] == shtr:
            repeats.append(c + 1)
            c = 0

    if len(repeats) > 0:
        m = max(repeats)
        return m


def match(list_data, sub_values):
    for i in range(1, len(list_data)):
        c = 0
        for j in range(1, len(sub_values) + 1):
            if str(sub_values[j - 1]) == list_data[i][j]:
                c += 1

        if c == len(sub_values):
            return list_data[i][0]
            break
    return "No match"


if __name__ == "__main__":
    main()
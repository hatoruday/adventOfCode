import sys

lines = open(sys.argv[1]).read().splitlines()
summation = 0
for line in lines:
    temporal = ""
    for i in range(len(line)):
        if line[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            temporal += line[i]
            continue
        elif line[i : i + 3] == "one":
            temporal += "1"
            i += 3
        elif line[i : i + 3] == "two":
            temporal += "2"
            i += 3
        elif line[i : i + 5] == "three":
            temporal += "3"
            i += 5
        elif line[i : i + 4] == "four":
            temporal += "4"
            i += 4
        elif line[i : i + 4] == "five":
            temporal += "5"
            i += 4
        elif line[i : i + 3] == "six":
            temporal += "6"
            i += 3
        elif line[i : i + 5] == "seven":
            temporal += "7"
            i += 5
        elif line[i : i + 5] == "eight":
            temporal += "8"
            i += 5
        elif line[i : i + 4] == "nine":
            temporal += "9"
            i += 4

    summation += int(temporal[0] + temporal[-1])
print(summation)

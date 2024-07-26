import sys

lines = open(sys.argv[1]).read().splitlines()
summation = 0
for line in lines:
    temporal = ""
    for l in line:
        if l in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            temporal += l
    print(temporal)
    summation += int(temporal[0] + temporal[-1])
print(summation)

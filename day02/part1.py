import sys

lines = open(sys.argv[1]).read().splitlines()

input_color_dict = {"red": 12, "green": 13, "blue": 14}

answer = 0
for line in lines:
    is_possible = True
    for set in line.split(":")[1].split(";"):

        current_color_dict = input_color_dict.copy()
        for colors in set.split(","):
            color = colors.split(" ")
            # print(int(color[1]), end=" ")
            current_color_dict[color[2]] -= int(color[1])
        # print()
        if not all(value >= 0 for value in current_color_dict.values()):
            is_possible = False
            break
    if is_possible:
        answer += int(line.split(":")[0].split(" ")[1])
print(answer)

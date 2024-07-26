import sys

lines = open(sys.argv[1]).read().splitlines()

input_color_dict = {"red": 0, "green": 0, "blue": 0}

answer = 0
for line in lines:
    is_possible = True
    current_color_dict = input_color_dict.copy()
    for set in line.split(":")[1].split(";"):

        for colors in set.split(","):
            color = colors.split(" ")
            # print(int(color[1]), end=" ")
            if current_color_dict[color[2]] < int(color[1]):
                current_color_dict[color[2]] = int(color[1])
        # print()

    answer += (
        current_color_dict["red"]
        * current_color_dict["green"]
        * current_color_dict["blue"]
    )
print(answer)

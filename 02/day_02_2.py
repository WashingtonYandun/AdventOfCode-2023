def main() -> int:
    """
    Calculate the total value of the sum of the multiplication of the minimun cubes in a game.

    Returns:
        int: The total value calculated from the game data.
    """
    total = 0

    with open('input.txt', 'r') as file:

        for game_data in file:
            game_data = game_data.strip().split(";")
            
            red = []
            green = []
            blue = []

            for group in game_data:

                group = group.strip().split(",")
                group = [cube.strip().split(maxsplit=2) for cube in group]

                if len(group[0]) == 3:
                    group[0] = group[0][-1].split(" ")

                for i in group:
                    val = int(i[0])
                    color = i[1]


                    if color == "red":
                        red.append(val)
                    elif color == "green":
                        green.append(val)
                    elif color == "blue":
                        blue.append(val)

                    min_red = 1
                    min_green = 1
                    min_blue = 1

                if len(red) != 0:
                    min_red = max(red)
                if len(green) != 0:
                    min_green = max(green)
                if len(blue) != 0:
                    min_blue = max(blue)

                current_product = min_red * min_green * min_blue

            total = total + current_product
        return total
                    


if __name__ == "__main__":
    print(main()) # 64097
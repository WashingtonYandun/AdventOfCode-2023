def is_possible(game_data: str, config: dict[str, int]) -> bool:
    """
    Determines if it is possible to create the given game data using the provided configuration.

    Args:
        game_data (str): The game data representing the cubes.
        config (dict[str, int]): The configuration of available cubes.

    Returns:
        bool: True if it is possible to create the game data using the configuration, False otherwise.
    """

    universe = sum(config.values()) # sum of all cubes

    for game_set in game_data.split(";"): # split the game data into sets
        cubes_data = game_set.strip().split(",") # split the set into cubes
        total_cubes = 0 # total cubes in the set

        for c in cubes_data:
            data = c.strip().split(maxsplit=2) # split the cube data into color and number

            if len(data) == 3: # the first one is always a side case
                data = data[-1]
                data = data.split(" ")

            n = int(data[0])
            color = data[1]
            
            if n > config[color]:
                return False
            
            total_cubes += n

            if total_cubes > universe:
                return False
    return True



def main() -> int:
    config={"red": 12, "green": 13, "blue": 14}
    total = 0

    with open('input.txt', 'r') as file:
        for i, game_data in enumerate(file):
            i += 1
            if is_possible(game_data, config):
                total += i

    return total


if __name__ == "__main__":
    print(main()) # 2265
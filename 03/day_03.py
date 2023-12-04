def has_surrounding_chars(grid: list[str], row: int, start: int, end: int) -> bool:
    """
    Checks if there are non-digit and non-dot characters in the surrounding area of a given position in the grid.

    Args:
    - grid (List[str]): The grid represented as a list of strings.
    - row (int): The row index.
    - start (int): The starting column index.
    - end (int): The ending column index.

    Returns:
    - bool: True if there are surrounding characters, False otherwise.
    """
    for i in range(max(0, row - 1), min(len(grid), row + 2)):
        for j in range(max(0, start - 1), min(len(grid[row]), end + 2)):

            if grid[i][j] != "." and not grid[i][j].isdigit():
                return True
            
    return False


def main() -> int:
    """
    Reads a grid from an 'input.txt' file and calculates the sum of numbers that are surrounded by characters in the grid.

    Returns:
    - int: The total sum of numbers meeting the specified criteria.
    """
    grid = None
    total = 0

    # Read the grid from the 'input.txt' file
    with open('input.txt', 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    for i, row in enumerate(grid):

        number = ""

        for j, c in enumerate(row):
            if c.isdigit():
                # If the character is a digit, append it to the current number
                number += c
                # Check if it's the last character in the row and has surrounding characters
                if j == len(row) - 1 and has_surrounding_chars(grid, i, j - len(number) + 1, j):
                    total += int(number) # transform the number into an integer and add it to the total

            elif number:
                # If the character is not a digit and there's a preceding number, check for surrounding characters
                if has_surrounding_chars(grid, i, j - len(number), j - 1):
                    total += int(number) # transform the number into an integer and add it to the total
                number = ""
    return total


if __name__ == "__main__":
    # Print the result of the main function
    print(main())  # 550934

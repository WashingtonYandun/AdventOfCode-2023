def main() -> int:
    with open('input.txt', 'r') as file: 
        total = 0

        for line in file:
            line = line.strip().split("|")

            # split the string into win and have, win[0] and have[1] from splited string "|"
            wins = set(int(c) for c in line[0].split(": ")[1].strip().split(" ") if c != "")
            have = set(int(c) for c in line[1].strip().split(" ") if c != "")

            matches = len(wins & have)

            if matches != 0:
                total += 2 ** (matches - 1)
    return total

        


if __name__ == "__main__":
    print(main()) # 18619
from collections import defaultdict


def main() -> tuple:

    with open('input.txt', 'r') as file:

        total = 0
        scratch_dict = defaultdict(int)

        for index, line in enumerate(file):
            
            scratch_dict[index] += 1

            line = line.strip().split("|")

            wins = set(int(c) for c in line[0].split(": ")[1].strip().split(" ") if c != "")
            have = set(int(c) for c in line[1].strip().split(" ") if c != "")

            matches = len(wins & have)

            if matches != 0:
                total += 2 ** (matches - 1)

            for times in range(1, matches + 1, 1):
                scratch_dict[index + times] += scratch_dict[index]
        
    return total, sum(scratch_dict.values())

        
if __name__ == "__main__":
    print(main()) # (18619, 8063216)
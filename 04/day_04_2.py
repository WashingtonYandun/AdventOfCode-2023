from collections import defaultdict


def main() -> int:
    with open('input.txt', 'r') as file: 
        total = 0

        scratch_dict = defaultdict(int)

        for l, line in enumerate(file):
            
            scratch_dict[l] += 1

            line = line.strip().split("|")

            wins = set(int(c) for c in line[0].split(": ")[1].strip().split(" ") if c != "")
            have = set(int(c) for c in line[1].strip().split(" ") if c != "")

            n = 0

            for num in have:
                if num in wins:
                    n += 1

            if n != 0:
                total += 2**(n - 1)

            for t in range(n):
                scratch_dict[l + t + 1] += scratch_dict[l]
        
    return total, sum(scratch_dict.values())

        
if __name__ == "__main__":
    print(main()) # (18619, 8063216)
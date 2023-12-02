def search(line):
    nums = [c for c in line if c.isdigit()]
    if len(nums) != 0:
        conc = nums[0] + nums[-1]
    else:
        return 0
    return int(conc)

def main():
    count = 0
    with open('input.txt', 'r') as file:    
        for line in file:
            count += search(line)

    return count

if __name__ == '__main__':
    print(main())
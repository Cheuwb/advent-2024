#only increasing or decreasing is "safe" x

#going between levels has to be within range of 1:3 x

#find how many reports are safe x


def main():
    with open('input', 'r') as file:
        count_safe_reports(file)


def count_safe_reports(file):
    safe_count = 0
    for report in file:
        level = list(map(int, report.split()))
        if (check_level(level) or check_with_removal(level)):
            safe_count += 1
    print(safe_count)

def check_level(level):
        for i in range(len(level)-1):
            current_level = level[i]
            next_level = level[i+1]            
            #check range
            if not (1 <= abs(next_level - current_level) <=3):
                break

            if (i > 0):
                prev_level = level[i-1]
                #check order on elements > 2, 2 elements will always be ascending, descending, or equal
                if not ((prev_level <= current_level <= next_level) or (prev_level >= current_level >= next_level)):
                    break

            # Last middle element in the list
            if (i == len(level)-2):
                return True
            
        return False

# part 2, trying combination levels,
# smarter way is to impose the restrictions from day1 into this method to remove smarter but takes more coding work
# it would limit the number of tries if required up to 5 additional calls instead of trying each level
# 2 re-try checks in {check range} and 3 re-try checks in {check ascending / descending}
def check_with_removal(level):
    for i in range(len(level)):
        mod_level = level[:i] + level[i+1:]
        if check_level(mod_level):
            return True
    return False

if __name__ == '__main__':
    main()
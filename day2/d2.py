#only increasing or decreasing is "safe" x

#going between levels has to be within range of 1:3 x

#find how many reports are safe x

with open('input', 'r') as file:
    safe_count = 0
    for reports in file:
        level = list(map(int, reports.split()))

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
                safe_count += 1

    print(safe_count)
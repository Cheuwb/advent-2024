with open('input', 'r') as file:

    column1 = []
    column2 = []

    for line in file:
        a,b = line.split()
        column1.append(a)
        column2.append(b)
    
    column1.sort()
    column2.sort()

    sum_answer = 0

    for i in range(len(column1)):
        sum_answer = sum_answer + abs((int(column1[i]) - int(column2[i])))

    print(sum_answer)

    #part2
    score2 = 0
    p1 = 0
    p2 = 0

    while p1 < len(column1) and p2 < len(column2):
        #equal value, count the number of times it shows up in column2
        if column1[p1] == column2[p2]:
            count_in_column2 = 0
            #counting in column2
            while p2 < len(column2) and column2[p2] == column1[p1]:
                count_in_column2 += 1
                p2 += 1
            #score after calculating
            score2 += int(column1[p1]) * count_in_column2
            #next number in column1
            p1 += 1
        #shift the pointers when they are not equal
        elif column1[p1] < column2[p2]:
            p1 += 1
        else:
            p2 += 1

    print(score2)
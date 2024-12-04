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
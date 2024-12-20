# read in the file
# every mul(%d,%d) found, add the two %d as a tuple into a list of tuples
# for each tuple in list, multiple the pair and add to target sum
# return the target sum

import re

with open('input', 'r') as file:
    content = file.read()
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    # matches = re.findall(pattern, content)
    # print(matches)

    result = 0
    execute = True

    for match in re.finditer(pattern, content):
        string = match.group(0)
        if (string == "do()"):
            execute = True
        elif (string == "don't()"):
            execute = False
        else:
            #multiple case
            if (execute):
                left_bracket = string.index('(')
                right_bracket = string.index(')')
                comma = string.index(',')

                number1 = string[left_bracket+1 : comma]
                number2 = string[comma+1 : right_bracket]
                product = int(number1) * int(number2)
                result += product
    
    print(result)

#part 2 -> 2 patterns to match; while in do() sum; when don't() skip until do() -> flag
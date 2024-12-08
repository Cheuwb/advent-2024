# read in the file
# every mul(%d,%d) found, add the two %d as a tuple into a list of tuples
# for each tuple in list, multiple the pair and add to target sum
# return the target sum

import re

with open('input', 'r') as file:
    content = file.read()
    pattern = r"mul\(\d+,\d+\)"
    # matches = re.findall(pattern, content)
    # print(matches)

    result = 0

    for match in re.finditer(pattern, content):
        string = match.group(0)
        left_bracket = string.index('(')
        right_bracket = string.index(')')
        comma = string.index(',')

        number1 = string[left_bracket+1 : comma]
        number2 = string[comma+1 : right_bracket]
        product = int(number1) * int(number2)
        result += product
    
    print(result)
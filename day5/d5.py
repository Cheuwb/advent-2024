class Manual:
    def __init__(self, rules, updates):
        self._rules = rules
        self._updates = updates
    
    def get_rules(self):
        return self._rules
    
    def get_updates(self):
        return self._updates


def rules_to_dict(rules):
    rules_dict = {}
    rules = rules.split('\n')
    for rule in rules:
        key, value = rule.split('|')
        rules_dict.setdefault(int(key), []).append(int(value))
    return rules_dict

def read_file_to_manual(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    manual = content.strip().split('\n\n')
    rules = rules_to_dict(manual[0])
    updates = [list(map(int, line.split(','))) for line in manual[1].split('\n')]
    return Manual(rules, updates)

def calculate_ordering(manual):
    rules = manual.get_rules()
    updates = manual.get_updates()
    total_ordering = 0
    
    for update in updates:
        #fault update if found rule Y when reading X
        faulty_update = False
        #checked numbers per update
        checked_numbers = set()
        for i in range(len(update)):
            # looking at each number in index
            x_value = update[i] # current value being read in
            y_values = rules.get(x_value) # list of corresponding Y rules (which X cannot be written after a Y has been read into set)
            # Y cannot exist before X is read in
            for y_value in y_values:
                if y_value in checked_numbers:
                    faulty_update = True
            if faulty_update:
                faulty_update = False
                break
            checked_numbers.add(x_value)
            if i == len(update)-1:
                total_ordering += update[(len(update)//2)]

    return total_ordering

if __name__ == "__main__":
    manual = read_file_to_manual("input")
    print(calculate_ordering(manual))
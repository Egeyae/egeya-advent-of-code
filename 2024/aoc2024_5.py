import re


def get_input():
    with open("./inputs/day5.txt") as f:
        return f.read()

def get_ruleset(input_):
    rules = [tuple(map(int, xy)) for xy in re.findall(r"(\d+)\|(\d+)", input_)]
    ruleset = {}
    for rule in rules:
        if rule[0] not in ruleset:
            ruleset[rule[0]] = {"before":[], "after":[]}
        if rule[1] not in ruleset:
            ruleset[rule[1]] = {"before":[], "after":[]}

        ruleset[rule[0]]["after"].append(rule[1])
        ruleset[rule[1]]["before"].append(rule[0])
    return ruleset

def get_updates(input_):
    updates = []
    for update in re.findall(r"^\d+(?:,\d+)*$", input_, re.MULTILINE):
        updates.append(tuple(map(int, update.strip().split(","))))
    return updates

def check_rule(rule_key, rule, update):
    """Check if a rule is validated for a given update"""
    if not rule_key in update:
        return True
    idx = update.index(rule_key)

    for after in rule["after"]:
        if after in update[:idx]:
            return False

    for before in rule["before"]:
        if before in update[idx:]:
            return False

    return True

def check_all_rules(ruleset, update):
    for k, v in ruleset.items():
        if not check_rule(k, v, update):
            return False
    return True


def part_1():
    data = get_input()

    ruleset = get_ruleset(data)
    updates = get_updates(data)

    total = 0

    for update in updates:
        if check_all_rules(ruleset, update):
            total += update[len(update)//2]
    print(total)

def get_failing_couple(rule_key, rule, update):
    if not rule_key in update:
        return None
    idx = update.index(rule_key)
    for after in rule["after"]:
        if after in update[:idx]:
            return rule_key, after

    for before in rule["before"]:
        if before in update[idx:]:
            return rule_key, before
    return None

def get_first_failing_rule(ruleset, update):
    for k, v in ruleset.items():
        failing = get_failing_couple(k, v, update)
        if failing:
            return failing
    return None


def correct_update(ruleset, update):
    update = list(update) # to allow modifications
    while True:
        failing = get_first_failing_rule(ruleset, update)
        if failing is None:
            return tuple(update) # back to immutable
        else:
            idx1, idx2 = update.index(failing[0]), update.index(failing[1])
            update[idx1], update[idx2] = update[idx2], update[idx1]


def part_2():
    data = get_input()

    ruleset = get_ruleset(data)
    updates = get_updates(data)

    total = 0

    for update in updates:
        if not check_all_rules(ruleset, update):
            update = correct_update(ruleset, update)
            total += update[len(update)//2]
    print(total)
if __name__ == "__main__":
    part_1()
    part_2()
import re


def construct_initial_state(s: str) -> list:
    lines = s.split("\n")
    for line in lines:
        stacks = [[] for _ in range(len(lines) + 1)]
    for line in lines:
        line = ([line[i:i + 4] for i in range(0, len(line), 4)])
        for count, value in enumerate(line):
            if re.search('[A-Z]', value):
                stacks[count + 1].append(value.strip())
    return stacks


def clean_movements(s: str) -> list:
    lines = s.split("\n")
    result = []
    for line in lines:
        if line != '':
            result.append([int(s) for s in re.findall(r'\d+', line)])
    return result


def handle_movements(movements: list[list[str]], stacks: list[list[str]]) -> list:
    for movement in movements:
        for i in range(movement[0]):
            temp = stacks[movement[1]].pop(0)
            stacks[movement[2]].insert(0, temp)

    return stacks


def get_top_elements(stacks: list[list[str]]):
    result = ""
    for stack in stacks:
        if stack:
            result += stack[0]

    return result


with open("data.txt", "r") as data:
    data = data.read().split("\n\n")
    initial_state = data[0]
    instructions = data[1]
    stacks = construct_initial_state(initial_state)
    movements = clean_movements(instructions)
    final_state = handle_movements(movements, stacks)
    get_top_elements(final_state)

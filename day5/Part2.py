from Part1 import construct_initial_state, clean_movements, get_top_elements


def handle_movements(movements: list[list[str]], stacks: list[list[str]]) -> list:
    for movement in movements:
        temp = []
        for i in range(movement[0]):
            temp.append(stacks[movement[1]].pop(0))
        stacks[movement[2]] = temp + stacks[movement[2]]

    return stacks


with open("data.txt", "r") as data:
    data = data.read().split("\n\n")
    initial_state = data[0]
    instructions = data[1]
    stacks = construct_initial_state(initial_state)
    movements = clean_movements(instructions)
    final_state = handle_movements(movements, stacks)
    print(get_top_elements(final_state))

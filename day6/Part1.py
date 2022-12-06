# n is the number of different characters and s is the input string
def find_n_different_characters(n: int, s: str):
    seen = {}
    for count, value in enumerate(s):
        if len(seen) == n:
            return seen
        elif value not in seen:
            seen[value] = count
        else:
            index = seen[value]
            seen = {k: v for k, v in seen.items() if v > index}
            seen[value] = count
    raise Exception("not found")

# with open("data.txt", "r") as data:
#     data = data.readline()
#     last_key = list(find_n_different_characters(4, data).values())
#     print(last_key[-1] + 1)

with open("data.txt", "r") as data:
    data = data.readline()
    last_key = list(find_n_different_characters(14, data).values())
    print(last_key[-1] + 1)


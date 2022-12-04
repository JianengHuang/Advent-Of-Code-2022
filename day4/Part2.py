def check_if_overlaps(s: str):
    lst = s.split(",")
    l1 = lst[0].partition("-")
    l2 = lst[1].partition("-")
    n1 = int(l1[0])
    n2 = int(l1[2])
    n3 = int(l2[0])
    n4 = int(l2[2])

    return (n1 <= n3 <= n2 or n1 <= n4 <= n2) or (n3 <= n1 <= n4 or n3 <= n2 <= n4)


with open("data.txt", "r") as data:
    data = data.read().split("\n")
    count = 0
    for line in data:
        if line and check_if_overlaps(line):
            count += 1

    print(count)

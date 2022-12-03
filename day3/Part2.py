class Solution2:
    def __init__(self, first: str, second: str, third: str):
        self.first = first
        self.second = second
        self.third = third

    def __str__(self):
        return f'{self.first} {self.second} {self.third}'

    def check_duplicates(self) -> list[str]:
        duplicates = []
        if self.first and self.second and self.third:
            shortest_string = min(self.first, self.second, self.third, key=len)
            i = 0
            for i in shortest_string:
                if i in self.first and i in self.second and i in self.third and i not in duplicates:
                    duplicates.append(i)
        return duplicates

    def check_duplicates_score(self) -> int:
        duplicates = self.check_duplicates()
        duplicate_score = 0
        if duplicates:
            alphabet_dictionary = {}
            with open("alphabet.txt", "r") as alphabet_file:
                for line in alphabet_file:
                    (key, val) = line.split()
                    alphabet_dictionary[key] = val
            for x in duplicates:
                duplicate_score += int(alphabet_dictionary.get(x))
        return duplicate_score


with open("data.txt", "r") as data:
    data = data.read().split("\n")
    data = list(filter(None, data))
    count = 1
    temp_list = []
    score = 0
    for line in data:
        if count % 3 == 0:
            temp_list.append(line)
            temp = Solution2(temp_list[0], temp_list[1], temp_list[2])
            score += temp.check_duplicates_score()
            count = 1
            temp_list = []
        else:
            temp_list.append(line)
            count += 1
    print(score)

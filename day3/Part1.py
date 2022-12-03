from string import ascii_letters as alc


def create_list() -> str:
    count = 0
    for index, char in enumerate(alc, start=1):
        print(char, index)


class Solution:
    def __init__(self, s: str):
        self.s_length_half = len(s) // 2
        self.left = s[:self.s_length_half]
        self.right = s[self.s_length_half:]

    def __str__(self):
        return f'{self.left} {self.right}'

    def check_duplicates(self) -> list[str]:
        duplicates = []
        if self.left and self.right:
            shortest_string = min(self.left, self.right, key=len)
            i = 0
            for i in shortest_string:
                if (i in self.right) and (i not in duplicates):
                    duplicates.append(i)
        return duplicates

    def check_duplicates_score(self) -> int:
        duplicates = self.check_duplicates()
        duplicates_score = 0
        if duplicates:
            alphabet_dictionary = {}
            with open("alphabet.txt", "r") as alphabet_file:
                for line in alphabet_file:
                    (key, val) = line.split()
                    alphabet_dictionary[key] = val
            for x in duplicates:
                duplicates_score += int(alphabet_dictionary.get(x))
        return duplicates_score


data_file = open("data.txt", "r")
data = data_file.read().split("\n")
data = list(filter(None, data))
score = 0
for item in data:
    item = Solution(item)
    score += item.check_duplicates_score()
print(score)

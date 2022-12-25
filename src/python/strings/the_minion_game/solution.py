def minion_game(string):
    for i, c in enumerate(string):
        print(i, c)

    s = sum([len(string) - i for i, c in enumerate(string) if c not in 'AEIOU'])
    k = sum([len(string) - i for i, c in enumerate(string) if c in 'AEIOU'])

    if k > s:
        print(f"Kevin {k}")
    elif s > k:
        print(f"Stuart {s}")
    else:
        print(f"Draw")


def first_answer(string):
    vowels = ['A', 'E', 'I', 'O', 'U']

    substrings = [
        string[j:j+1+i]
        for i in range(len(string))
        for j in range(len(string) - i)
    ]

    kevins_words = list(filter(lambda s: s[:1] in vowels, substrings))
    stuarts_words = list(filter(lambda s: s[:1] not in vowels, substrings))

    if len(kevins_words) > len(stuarts_words):
        print(f"Kevin {len(kevins_words)}")
    elif len(kevins_words) < len(stuarts_words):
        print(f"Stuart {s}")
    else:
        print(f"Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)

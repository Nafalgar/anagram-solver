def main():
    word = input("Enter the word to check against: ")

    dances = []
    with open('dances.txt', 'r') as file:
        for line in file:
            dances.extend(line.splitlines())

    for dance in dances:
        dance = dance.lower()
        result = match(word, dance)
        if result:
            print("The word '" + word + "' matches the dance: '" + dance + "' !")
            return
    print("No matches found in the dance list for the entered word :'(...")


def match(word, dance):
    for letter in word:
        if letter in dance:
            dance = dance.replace(letter, '', 1)
        else:
            return 0
    if not len(dance):
        return 1
    else:
        return 0


if __name__ == '__main__':
    main()


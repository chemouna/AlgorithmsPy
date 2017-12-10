"""
http://community.topcoder.com/stat?c=problem_statement&pm=608
"""


def getLettersDictionary(letters):
    dictionary = {}
    for i in range(len(letters)):
        letter = letters[i][0]
        dictionary[letter] = letters[i][1:len(letters[i])]
    return dictionary


def enlarge(message, letters):
    result = []
    dictLetters = getLettersDictionary(letters)
    for i in range(5):
        row = ""
        # Traverse by rows
        for j in range(len(message)):
            letter = message[j]
            letterStr = dictLetters[letter]
            orig = 5 * i + (i + 1)
            end = orig + 5
            row += letterStr[orig:end]
            if j < 4:
                row += "."
        result.append(row)
    return result

def main():
    print enlarge("TOPCODER", ["T:#####-..#..-..#..-..#..-..#..", "O:#####-#...#-#...#-#...#-#####",
                               "P:####.-#...#-####.-#....-#....", "C:.####-#....-#....-#....-.####",
                               "D:####.-#...#-#...#-#...#-####.", "E:#####-#....-####.-#....-#####",
                               "R:####.-#...#-####.-#.#..-#..##"])


print enlarge("DOK", ["D:####.-#...#-#...#-#...#-####.", "O:#####-#...#-#...#-#...#-#####",
                      "K:#...#-#..#.-###..-#..#.-#...#"])

print enlarge("RANDOMNESS", ["S:##.##-#####-#.#.#-#.#.#-####.", "N:#####-#####-#####-#####-#####",
                             "R:#####-#####-##.##-#####-#####", "A:.....-.....-.....-.....-.....",
                             "D:#.#.#-.#.#.-#.#.#-.#.#.-#.#.#", "O:#####-#...#-#.#.#-#...#-#####",
                             "E:#....-.#...-..#..-...#.-....#", "M:#....-.....-.....-.....-.....",
                             "X:#...#-.#.#.-..#..-.#.#.-#...#"])

if __name__ == '__main__':
    main()

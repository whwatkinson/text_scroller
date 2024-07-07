s = """###         
###         
###         
 #          
            
###      
###"""


def ascii_to_list(s: str):
    max_width = max([len(char_slice) for char_slice in s.split("\n")])
    # max_width = 25

    s = s.replace("\n", "")
    letter = []
    i = 0
    while i * max_width < len(s):

        # for i in range(12):

        char_slice = s[i * max_width: (i + 1) * max_width]
        i += 1
        if all(x == " " for x in char_slice):
            continue

        letter.append([char for char in char_slice])

    for row in letter:
        print("".join(row), end="\n")

    print(letter)


if __name__ == "__main__":
    ascii_to_list(s)

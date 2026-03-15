# CONST
LOW_CHARSET = "abcdefghijklmnopqrstuvwxyz"
UPP_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM_CHARSET = "0123456789"
SYM_CHARSET = "!@#$%^&*()-_+=~`[]{}|\\:;\"'<>,.?/"

def wordlist_generator(pattern, strings, output_file="out.txt"):
    charsets = []

    for char in pattern:
        if char == "@":
            charsets.append(strings)
        elif char == "%":
            charsets.append(NUM_CHARSET)
        elif char == "^":
            charsets.append(SYM_CHARSET)
        elif char == "!":
            charsets.append(LOW_CHARSET + UPP_CHARSET)
        elif char == "$":
            charsets.append(LOW_CHARSET)
        elif char == "&":
            charsets.append(UPP_CHARSET)
        else:
            charsets.append(char)

    def generate(index, current_word):
        if index == len(charsets):
            f.write(current_word + "\n")
            return
        for char in charsets[index]:
            generate(index + 1, current_word + char)

    with open(output_file, "w") as f:
        generate(0, "")

def main():
    pattern = "AIS@%"
    strings = "Aa5#"
    wordlist_generator(pattern, strings, "wordlist.txt")

if __name__ == "__main__":
    main()
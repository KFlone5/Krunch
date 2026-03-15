# CONST
LOW_CHARSET = "abcdefghijklmnopqrstuvwxyz"
UPP_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM_CHARSET = "0123456789"
SYM_CHARSET = "!@#$%^&*()-_+=~`[]{}|\\:;\"'<>,.?/"

def print_welcome():
    print("""$$\   $$\                                         $$\       
$$ | $$  |                                        $$ |      
$$ |$$  /  $$$$$$\  $$\   $$\ $$$$$$$\   $$$$$$$\ $$$$$$$\  
$$$$$  /  $$  __$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  __$$\ 
$$  $$<   $$ |  \__|$$ |  $$ |$$ |  $$ |$$ /      $$ |  $$ |
$$ |\$$\  $$ |      $$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |
$$ | \$$\ $$ |      \$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |  $$ |
\__|  \__|\__|       \______/ \__|  \__| \_______|\__|  \__|""")
    
    print("""
Pattern Symbols
-----------------------------------------------------------------------\\
| @  | Characters from your custom charset (-s)                        |
| %  | Digits 0-9                                                      |
| ^  | Special characters accessed via Shift + number key !@#$%^&*()   |
| !  | All letters, both uppercase and lowercase (a-z A-Z)             |
| $  | Lowercase letters only (a-z)                                    |
| &  | Uppercase letters only (A-Z)                                    |
-----------------------------------------------------------------------/    
\n\n""")

def wordlist_generator(pattern, strings, output_file):
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
    print_welcome()
    charset = ""
    
    print("Please enter the pattern of the password")
    pattern = input(">>>")
    
    if '@' in pattern:
        print("Please enter the charset")
        charset = input(">>>")
    
    print("Enter the filename where the wordlist will be written (out.txt by default)")
    output_file = input(">>>")

    if output_file == "":
        output_file = "out.txt"
    
    wordlist_generator(pattern, charset, output_file)

if __name__ == "__main__":
    main()
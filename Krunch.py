import os
import argparse

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

def calculate_stats(pattern, strings):
    total_passwords = 1
    password_length = len(pattern)

    for char in pattern:
        if char == "@":
            total_passwords *= len(strings)
        elif char == "%":
            total_passwords *= len(NUM_CHARSET)
        elif char == "^":
            total_passwords *= len(SYM_CHARSET)
        elif char == "!":
            total_passwords *= len(LOW_CHARSET + UPP_CHARSET)
        elif char == "$":
            total_passwords *= len(LOW_CHARSET)
        elif char == "&":
            total_passwords *= len(UPP_CHARSET)

    total_bytes = total_passwords * (password_length + 1)
    total_kb = total_bytes / 1024
    total_mb = total_kb / 1024
    total_gb = total_mb / 1024

    print(f"Krunch will now generate the following amount of data:")
    print(f"{total_bytes} B")
    print(f"{total_kb:.2f} KB")
    print(f"{total_mb:.2f} MB")
    print(f"{total_gb:.2f} GB")
    print(f"Number of passwords will be generated: {total_passwords}")
    
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--pattern", type=str, help="Pattern of the password for example (LTR202%@Y)")
    parser.add_argument("-c", "--charset", type=str, nargs="*", help="Custom charset for the pattern filled with the custom symbols for example (52iO*$}</)")
    parser.add_argument("-o", "--output", type=str, help="Name of the output file (by default \"out.txt\")")

    args = parser.parse_args()

    if args is None:
        print(args)
    else:
        pattern = args.pattern
        charset = args.charset
        output_file = args.output

        if pattern == "":
            print("Pattern is empty. Nothing to generate.")
            print(args.pattern)

        if charset == None:
            charset = ""
        
        if ("@" in pattern) and (charset == ""):
            print("Pattern has \"@\" but the charset was not specified.")
            print(args.charset)

        if output_file == None:
            output_file = "out.txt"
        
        if (pattern != "") and (not ("@" in pattern) and (charset == "")):
            if output_file == "":
                output_file = "out.txt"
            print(f"Wordlist will be saved as \"{output_file}\" at this directory \"{os.getcwd()}\"\n")
            
            calculate_stats(pattern, charset)
            wordlist_generator(pattern, charset, output_file)
            print("Krunch has finished generating the wordlist!")

if __name__ == "__main__":
    main()
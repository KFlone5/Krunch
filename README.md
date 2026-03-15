# Krunch

Custom wordlist generator with pattern-based rules, inspired by the classic Crunch tool from Kali Linux.

## Note
Krunch is currently in early development. Right now it runs as an interactive CLI, meaning it will ask you for input step by step after launch. Some of the text in this README (Usage, Arguments, Example) describes the planned argument-based usage and is not fully accurate yet. Argument-based usage (e.g. `python Krunch.py -t AIS@% -o wordlist.txt`) will be added in a future update.

## Installation
```bash
git clone https://github.com/KFlone5/Krunch.git
cd Krunch
```

No external dependencies, just Python 3.

## Usage
```bash
python Krunch.py -t <pattern> -o <output_file> -s <custom_charset>
```

## Arguments

| Argument | Description |
|----------|-------------|
| `-t` | Pattern template for wordlist generation |
| `-o` | Output file to save the wordlist |
| `-s` | Custom charset used for `@` in the pattern |

## Pattern Symbols

| Symbol | Meaning |
|--------|---------|
| `@` | Characters from your custom charset (`-s`) |
| `%` | Digits `0-9` |
| `^` | Special characters accessed via Shift + number key (`!@#$%^&*()`) |
| `!` | All letters, both uppercase and lowercase (`a-z A-Z`) |
| `$` | Lowercase letters only (`a-z`) |
| `&` | Uppercase letters only (`A-Z`) |

## Example
```bash
python Krunch.py -t AIS@@%^!$& -o wordlist.txt -s "LlTtRr0123456uU+=-_!@#$%^&*(){}[]|\/,.<>"
```

This generates words that start with `AIS`, followed by characters based on the pattern rules.

## Inspired By

Crunch, the wordlist generator that comes pre-installed in Kali Linux.

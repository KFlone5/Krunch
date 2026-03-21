# Krunch
Custom wordlist generator with pattern-based rules, inspired by the classic Crunch tool from Kali Linux.

## Note
Krunch is still in early development, so things may change between versions. The old interactive CLI version is still available in releases under v1.x.x if needed.

## Installation
```bash
git clone https://github.com/KFlone5/Krunch.git
cd Krunch
```
No external dependencies, just Python 3.

## Usage
```bash
python Krunch.py -p <pattern> -c <custom_charset> -o <output_file>
```

## Arguments
| Argument | Description |
|----------|-------------|
| `-p` | Pattern template for wordlist generation |
| `-c` | Custom charset used for `@` in the pattern |
| `-o` | Output file to save the wordlist (default: `out.txt`) |

## Pattern Symbols
| Symbol | Meaning |
|--------|---------|
| `@` | Characters from your custom charset (`-c`) |
| `%` | Digits `0-9` |
| `^` | Special characters accessed via Shift + number key (`!@#$%^&*()`) |
| `!` | All letters, both uppercase and lowercase (`a-z A-Z`) |
| `$` | Lowercase letters only (`a-z`) |
| `&` | Uppercase letters only (`A-Z`) |

## Example
```bash
python Krunch.py -p AIS@@%^!$& -c "LlTtRr0123456uU+=-_!@#$%^&*(){}[]|\/,.<>" -o wordlist.txt
```
This generates words that start with `AIS`, followed by characters based on the pattern rules.

## Inspired By
Crunch, the wordlist generator that comes pre-installed in Kali Linux.

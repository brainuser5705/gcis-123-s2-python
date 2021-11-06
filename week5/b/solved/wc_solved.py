"""
Input for a text file name and list its:
- word count (assume each word is separated by a single space)
- character count (not including whitespace)
- line count
"""

filename = input("What is the file name?")

line_count = 0
word_count = 0
character_count = 0
with open(filename) as file:
    for line in file:

        # increment line
        line_count += 1

        # increment word
        line = line.strip()
        words = line.split()
        word_count += len(words)

        # increment character
        for word in words:
            character_count += len(word)

print("Line count:", line_count)
print("Word count:", word_count)
print("Character count:", character_count)


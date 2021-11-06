"""
Open a text file and list its:
- word count
- character count
- line count
"""


def count_file(filename):

    lc = 0
    wc = 0
    cc = 0

    with open(filename) as file:
        for line in file:
            
            # increment line
            lc += 1

            words = line.strip().split()

            for word in words:
                # increment words
                wc += 1
                # increment characters
                cc += len(word)

    string = "lc:" + str(lc) + ",wc:" + str(wc) + ",cc:" + str(cc)
    return string

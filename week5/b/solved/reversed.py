def reversed(string):

    cpy_string = ''
    
    for i in range(len(string)-1,-1,-1):
        cpy_string += string[i]

    return cpy_string

def main():

    print(reversed("dancing"))

if __name__ == '__main__':
    main()
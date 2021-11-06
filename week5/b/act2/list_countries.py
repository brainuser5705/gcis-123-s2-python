def validate(value):
    """
    Changes value to appropiate type for data processing
    :param: value - the value from csv file
    """

    if value.strip() == '' or value == None:
        return 0 # simplify things

    return float(value)


def main():

    # get the columns
    with open("./factbook.csv") as factbook:
        columns = factbook.readline().split(',')

        # TO DO:
        # for each column/category:
        # print the smallest, largest values along with the country name
        # and average value 

if __name__ == '__main__':
    main()
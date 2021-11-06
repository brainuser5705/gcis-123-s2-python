def validate(value):

    if value.strip() == '' or value == None:
        return 0 # simplify things

    return float(value)

def main():      

    # get the columns
    with open("./factbook.csv") as factbook:
        columns = factbook.readline().split(',')
        
    i = 1
    while i < len(columns):

        with open("./factbook.csv") as fact:

            fact.readline() # skip the columns line

            # get the initial start values from the first country
            first_values = fact.readline().split(',')

            smallest_name = first_values[0]
            smallest_value = validate(first_values[i])

            largest_name = first_values[0]
            largest_value = validate(first_values[i])

            # aggregate data
            sum = 0
            num_countries = 0

            for country in fact:

                values = country.split(',')
                value = validate(values[i])

                if value < smallest_value:
                    smallest_value = value
                    smallest_name = values[0]

                if value > largest_value:
                    largest_value = value
                    largest_name = values[0]

                sum += value
                num_countries += 1

            print("\n" + columns[i])
            print("smallest:", smallest_name,"-", smallest_value)
            print("largest:", largest_name,"-", largest_value)
            print("average: ", sum/num_countries)

        i += 1



if __name__ == '__main__':
    main()
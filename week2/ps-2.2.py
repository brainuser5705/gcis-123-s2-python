def birthday():
    cy = int(input("current year: "))
    cm = int(input("current month: "))

    by = int(input("birth year: "))
    bm = int(input("birth month: "))

    # if birth month is larger than the current year,
    # cm-bm would be moving back months since it is
    # negative
    age = (cy-by)*12 + (cm-bm)

    print("Your current age is ", age)


def num_days():
    m = int(input("current month: "))
    d = int(input("current day: "))

    # This will be implicitly cast as a float
    total = ((m-1)*30.4) + d

    print("The approximate day of the year is:\n" + str(total))
    
#birthday()
num_days()

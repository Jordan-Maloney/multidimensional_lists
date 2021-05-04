##
# magic_calculator.py
# Jordan Maloney
# 16/4/21


def page_maker_1():
    """
    Creates page 1 of the Magic calculator
    """
    # Constants
    MIN = 1
    MAX = 64
    COUNT = 2
    # Code
    page = []
    for i in range(MIN, MAX, COUNT):
        page.append(i)
    return page


def page_maker_2():
    """
    Creates page 2 of the Magic calculator
    """
    # Constants
    ROW_COUNT = 4
    COLUMN_COUNT = 8
    ADJUST_1 = 1
    ADJUST_2 = 2
    ADJUST_3 = 8
    # Code
    page = []
    for i in range(ROW_COUNT):
        for j in range(COLUMN_COUNT):
            page.append(ADJUST_3 * ((
                ADJUST_2 * (i + ADJUST_1)) - ADJUST_1) + j)
    return page


def page_maker_3():
    """
    Creates page 3 of the Magic calculator
    """
    # Constants
    MIN = 2
    MAX = 63
    COUNT = 4
    ADJUST_1 = 1
    # Code
    page = []
    for i in range(MIN, MAX, COUNT):
        page.append(i)
        page.append(i + ADJUST_1)
    return page


def page_maker_4():
    """
    Creates page 4 of the Magic calculator
    """
    # Constants
    ROW_COUNT = 2
    COLUMN_COUNT = 16
    ADJUST_1 = 1
    ADJUST_2 = 16
    # Code
    page = []
    for i in range(ROW_COUNT):
        for j in range(COLUMN_COUNT):
            page.append((ADJUST_2 * (i + i + ADJUST_1)) + j)
    return page


def page_maker_5():
    """
    Creates page 5 of the Magic calculator
    """
    # Constants
    ROW_COUNT = 8
    COLUMN_COUNT = 4
    ADJUST_1 = 4
    ADJUST_2 = 8
    # Code
    page = []
    for i in range(ROW_COUNT):
        for j in range(COLUMN_COUNT):
            page.append((ADJUST_1 + (ADJUST_2 * i)) + j)
    return page


def page_maker_6():
    """
    Creates page 6 of the Magic calculator
    """
    # Constants
    MIN = 32
    MAX = 64
    # Code
    page = []
    for i in range(MIN, MAX):
        page.append(i)
    return page


def calculator(page_1, page_2, page_3, page_4, page_5, page_6):
    """
    Calculates the number the user thinks of
    """
    number = 0
    number += query(page_1)
    number += query(page_2)
    number += query(page_3)
    number += query(page_4)
    number += query(page_5)
    number += query(page_6)
    return number


def query(page):
    """
    Displays a page and asks the user if the number that they're thinking of
    is in the page, if it is then it returns the first number of the page
    to the calculator function
    """
    # Constants
    ROW_COUNT = 4
    COLUMN_COUNT = 8
    ADJUST_1 = 0
    ADJUST_2 = 8
    # Displaying page
    for i in range(ROW_COUNT):
        row = []
        for j in range(COLUMN_COUNT):
            row.append(page[(j + (i * ADJUST_2))])
        print(row)
    # Asking the user if the number that they're thinking of is in the page
    number_true = ""
    while number_true != "y" and number_true != "n":
        number_true = input(
            "Is the number you're thinking of in this list? ").lower()
        # Returning first number of the page
        if number_true == "y":
            return page[ADJUST_1]
        else:
            return ADJUST_1


# Main routine
if __name__ == "__main__":
    page_1 = page_maker_1()
    page_2 = page_maker_2()
    page_3 = page_maker_3()
    page_4 = page_maker_4()
    page_5 = page_maker_5()
    page_6 = page_maker_6()
    print("Think of a number from 0 to 63.", end=" ")
    print("I will guess it after you answer 6 questions.")
    number = calculator(page_1, page_2, page_3, page_4, page_5, page_6)
    print("The number you're thinking of is {}.".format(number))

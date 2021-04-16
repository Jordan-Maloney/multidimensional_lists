##
# magic_calculator.py
# Jordan Maloney
# 16/4/21


def page_maker_1():
    """
    Creates page 1 of the Magic calculator
    """
    page = []
    for i in range(1, 64, 2):
        page.append(i)
    return page
    

def page_maker_2():
    """
    Creates page 2 of the Magic calculator
    """
    page = []
    for i in range(4):
        for j in range(8):
            page.append(8 * ((2 * (i + 1)) - 1) + j)
    return page


def page_maker_3():
    """
    Creates page 3 of the Magic calculator
    """
    page = []
    for i in range(2, 63, 4):
        page.append(i)
        page.append(i + 1)
    return page


def page_maker_4():
    """
    Creates page 4 of the Magic calculator
    """
    page = []
    for i in range(2):
        for j in range(16):
            page.append((16 * (i + i + 1)) + j)
    return page


def page_maker_5():
    """
    Creates page 5 of the Magic calculator
    """
    page = []
    for i in range(8):
        for j in range(4):
            page.append((4 + (8 * i)) + j)
    return page


def page_maker_6():
    """
    Creates page 6 of the Magic calculator
    """
    page = []
    for i in range(32, 64):
        page.append(i)
    return page


def calculator():
    """
    Calculates the number the user thinks of
    """
    query(page_1)
    query(page_2)
    query(page_3)
    query(page_4)
    query(page_5)
    query(page_6)

# Main routine
if __name__ == "__main__":
    page_1 = page_maker_1()
    page_2 = page_maker_2()
    page_3 = page_maker_3()
    page_4 = page_maker_4()
    page_5 = page_maker_5()
    page_6 = page_maker_6()
    print("Think of a number from 0 to 63. I will guess it after you answer 6 questions.")
    calculator(page_1, page_2, page_3, page_4, page_5, page_6)
    

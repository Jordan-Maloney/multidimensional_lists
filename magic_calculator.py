##
# magic_calculator.py
# Jordan Maloney
# 14/4/21


def page_maker_1():
    """
    Creates page 1 of the Magic calculator
    """
    page = []
    for i in range(1, 64, 2):
        page.append(i)
    print(page)

if __name__ == "__main__":
    page_maker_1()

"""- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- Feel free to add new helper functions, but DO NOT modify/delete the given functions.

- You MUST complete the functions defined below, except the ones that are already defined.
"""


def items(i, j):
    itemlist = [['Tshirt', 'Apparels', 500],
                ['Trousers', 'Apparels', 600],
                ['Scarf', 'Apparels', 250],
                ['Smartphone', 'Electronics', 20000],
                ['iPad', 'Electronics', 30000],
                ['Laptop', 'Electronics', 50000],
                ['Eggs', 'Eatables', 5],
                ['Chocolate', 'Eatables', 10],
                ['Juice', 'Eatables', 100],
                ['Milk', 'Eatables', 45]]
    return itemlist[i][j]


def show_menu():
    """
        Description: Prints the menu as shown in the PDF

        Parameters: No paramters

        Returns: No return value
    """
    menu = """=================================================
                   MY BAZAAR
=================================================
Hello! Welcome to my grocery store!
Following are the products available in the shop:

-------------------------------------------------
CODE | DESCRIPTION |   CATEGORY   | COST (Rs)
-------------------------------------------------
  0  | Tshirt      | Apparels     | 500
  1  | Trousers    | Apparels     | 600
  2  | Scarf       | Apparels     | 250
  3  | Smartphone  | Electronics  | 20,000
  4  | iPad        | Electronics  | 30,000
  5  | Laptop      | Electronics  | 50,000
  6  | Eggs        | Eatables     | 5
  7  | Chocolate   | Eatables     | 10
  8  | Juice       | Eatables     | 100
  9  | Milk        | Eatables     | 45
------------------------------------------------
"""
    print(menu)


def get_regular_input():
    """
        Description: Takes space separated item codes (only integers allowed).
        Include appropriate print statements to match the output with the
        screenshot provided in the PDF.

        Parameters: No parameters

        Returns: Returns a list of integers of length 10, where the i_th
        element represents the quantity of the item with item code i.
    """
    menu = """

-------------------------------------------------
ENTER ITEMS YOU WISH TO BUY
-------------------------------------------------"""
    print(menu)
    a = [0] * 10
    x = input('Enter the item codes (space-separated): ')
    if x.strip() == '':
        print('There is no order but I still have to show order details and ask you for coupon code.')
        return a
    y = x.strip().split(' ')
    for i in y:
        if i not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            print(i, 'is invalid!')
            continue
        a[int(i)] += 1
    print()
    return a


def get_bulk_input():
    """
        Description: Takes inputs (only integers allowed) from a bulk buyer.
        For details, refer PDF. Include appropriate print statements to match
        the output with the screenshot provided in the PDF.

        Parameters: No parameters

        Returns: Returns a list of integers of length 10, where the i_th
        element represents the quantity of the item with item code i.
    """
    menu = """
-------------------------------------------------
ENTER ITEM AND QUANTITIES
-------------------------------------------------"""
    print(menu)
    a = [0] * 10
    while True:
        x = input('Enter code and quantity (leave blank to stop): ')
        if x.strip() == '':
            print('Your order has been finalized.')
            break

        (i, j) = map(int, x.strip().split(' '))  # (int(y[0]), int(y[1]))
        if j < 1 and (i not in range(0, 10)):
            print('Invalid code and quantity! Try again.')
            print()
            continue
        if i not in range(0, 10):
            print('Invalid code! Try again.')
            print()
            continue
        if j < 1:
            print('Invalid quantity! Try again.')
            print()
            continue
        print('You added', j, items(int(i), 0))
        print()
        a[int(i)] += int(j)
    print()
    return a


def print_order_details(quantities):
    """
        Description: Prints the details of the order in a manner similar to the
        sample given in PDF.

        Parameters: Takes a list of integers of length 10, where the i_th
        element represents the quantity of the item with item code i.

        Returns: No return value
    """
    menu = """
-------------------------------------------------
ORDER DETAILS
-------------------------------------------------"""
    print(menu)
    num = 1
    x = 0
    tot = 0
    for i in quantities:
        if i > 0:
            print('[' + str(num) + '] ' + items(x, 0) + ' * ' + str(i) + ' = Rs ' + str(items(x, 2)) + ' * ' + str(
                i) + ' = Rs ' + str(items(x, 2) * i))
            tot += items(x, 2) * i
            num += 1
        x += 1
    print()
    print('TOTAL COST =', tot)
    print()


def calculate_category_wise_cost(quantities):
    """
        Description: Calculates the category wise cost using the quantities
        provided. Include appropriate print statements to match the output with the
        screenshot provided in the PDF.

        Parameters: Takes a list of integers of length 10, where the i_th
        element represents the quantity of the item with item code i.

        Returns: A 3-tuple of integers in the following format:
        (apparels_cost, electronics_cost, eatables_cost)
    """
    menu = """
-------------------------------------------------
CATEGORY-WISE COST
-------------------------------------------------"""
    print(menu)
    ap = 0
    el = 0
    ea = 0
    x = 0
    for i in quantities:
        if i > 0:
            t = items(x, 1)
            if t == 'Apparels':
                ap += i * items(x, 2)
            elif t == 'Electronics':
                el += i * items(x, 2)
            elif t == 'Eatables':
                ea += i * items(x, 2)
        x += 1
    if ap > 0:
        print('Apparels = Rs', ap)
    if el > 0:
        print('Electronics = Rs', el)
    if ea > 0:
        print('Eatables = Rs', ea)
    print()
    return ap, el, ea


def get_discount(cost, discount_rate):
    """
        Description: This is a helper function. DO NOT CHANGE THIS.
        This function must be used whenever you are calculating discounts.

        Parameters: Takes 2 parameters:
        - cost: Integer
        - discount_rate: Float: 0 <= discount_rate <= 1

        Returns: The discount on the cost provided.
    """
    return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    """
        Description: Calculates the discounted category-wise price, if applicable.
        Include appropriate print statements to match the output with the
        screenshot provided in the PDF.

        Parameters: Takes 3 integer parameters:
        - apparels_cost: 	cost for the category 'Apparels'
        - electronics_cost: cost for the category 'Electronics'
        - eatables_cost: 	cost for the category 'Eatables'

        Returns: A 3-tuple of integers in the following format:
        (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost).
    """
    menu = """
-------------------------------------------------
DISCOUNTS
-------------------------------------------------"""
    print(menu)
    td = 0
    dap = apparels_cost
    dele = electronics_cost
    dea = eatables_cost
    if apparels_cost >= 2000:
        dis_ap = get_discount(apparels_cost, 0.1)
        td += dis_ap
        dap = int(apparels_cost - dis_ap)
        print('[APPAREL] Rs', apparels_cost, '- Rs', dis_ap, '= Rs', dap)

    if electronics_cost >= 25000:
        dis_ele = get_discount(electronics_cost, 0.1)
        td += dis_ele
        dele = int(electronics_cost - dis_ele)
        print('[ELECTRONICS] Rs', electronics_cost, '- Rs', dis_ele, '= Rs', dele)

    if eatables_cost >= 500:
        dis_eat = get_discount(eatables_cost, 0.1)
        td += dis_eat
        dea = int(eatables_cost - dis_eat)
        print('[EATABLES] Rs', eatables_cost, '- Rs', dis_eat, '= Rs', dea)
    print()
    tc = dap + dele + dea
    print('TOTAL DISCOUNT = Rs', int(td))
    print('TOTAL COST = Rs', int(tc))
    print()
    return dap, dele, dea


def get_tax(cost, tax):
    """
        Description: This is a helper function. DO NOT CHANGE THIS.
        This function must be used whenever you are calculating discounts.

        Parameters: Takes 2 parameters:
        - cost: Integer
        - tax: 	Float: 0 <= tax <= 1

        Returns: The tax on the cost provided.
    """
    return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    """
        Description: Calculates the total cost including taxes.
        Include appropriate print statements to match the output with the
        screenshot provided in the PDF.

        Parameters: Takes 3 integer parameters:
        - apparels_cost: 	cost for the category 'Apparels'
        - electronics_cost: cost for the category 'Electronics'
        - eatables_cost: 	cost for the category 'Eatables'

        Returns: A 2-tuple of integers in the following format:
        (total_cost_including_tax, total_tax)
    """
    menu = '''
-------------------------------------------------
TAX
-------------------------------------------------'''
    print(menu)
    apt, elt, eat = get_tax(apparels_cost, 0.10), get_tax(electronics_cost, 0.15), get_tax(eatables_cost, 0.05)
    if apt > 0:
        print('[APPAREL] Rs', apparels_cost, '* 0.10 = Rs', apt)
    if elt > 0:
        print('[ELECTRONICS] Rs', electronics_cost, '* 0.15 = Rs', elt)
    if eat > 0:
        print('[EATABLES] Rs', eatables_cost, '* 0.05 = Rs', eat)
    print()
    tt = apt + elt + eat
    tc = apparels_cost + electronics_cost + eatables_cost + tt
    print('TOTAL TAX = Rs', tt)
    print('TOTAL COST = Rs', tc)
    print()
    return tc, tt


def apply_coupon_code(total_cost):
    """
        Description: Takes the coupon code from the user as input (case-sensitive).
        For details, refer the PDF. Include appropriate print statements to match
        the output with the screenshot provided in the PDF.

        Parameters: The total cost (integer) on which the coupon is to be applied.

        Returns: A 2-tuple of integers:
        (total_cost_after_coupon_discount, total_coupon_discount)
    """
    menu = '''
-------------------------------------------------
COUPON CODE
-------------------------------------------------'''
    print(menu)
    tc = total_cost
    td = 0
    while True:
        coupon = input('Enter coupon code (else leave blank): ').strip()
        if coupon == 'HELLE25' and total_cost >= 25000:
            td = min(5000, total_cost * 0.25)
            tc = total_cost - td
            print('[HELLE25] min(5000, Rs', total_cost, '* 0.25 ) = Rs', td)
            print()
            print('TOTAL COUPON DISCOUNT = Rs', td)
            print('TOTAL COST = Rs', tc)
            break
        elif coupon == 'HELLE25':
            print('HELLE25 only valid for total cost >= 25000. Try again.')
            print()
        elif coupon == 'CHILL50' and total_cost >= 50000:
            td = min(10000, total_cost * 0.50)
            tc = total_cost - td
            print('[CHILL50] min(10000, Rs', total_cost, '* 0.50) = Rs', td)
            print()
            print('TOTAL COUPON DISCOUNT = Rs', td)
            print('TOTAL COST = Rs', tc)
            break
        elif coupon == 'CHILL50':
            print('CHILL50 only valid for total cost >= 50000. Try again.')
            print()
        elif coupon.strip() == '':
            print('No coupon code applied.')
            print()
            print('TOTAL COUPON DISCOUNT = Rs', td)
            print('TOTAL COST = Rs', tc)
            break
        else:
            print('Invalid coupon code. Try again.')
            print()
    return tc, td


def main():
    """
        Description: This is the main function. All production level codes usually
        have this function. This function will call the functions you have written
        above to design the logic. You will see how splitting your code into specialised
        functions makes the code easier to read, write and debug. Include appropriate
        print statements to match the output with the screenshots provided in the PDF.

        Parameters: No parameters

        Returns: No return value
    """
    show_menu()
    binp = input("Would you like to buy in bulk? (y or Y / n or N): ").lower().strip()
    while binp != 'y' and binp != 'n':
        print('Error! Enter (y or Y / n or N) only.')
        print()
        binp = input("Would you like to buy in bulk? (y or Y / n or N): ").lower().strip()
    bulk = binp == 'y'
    if bulk:
        quantities = get_bulk_input()
    else:
        quantities = get_regular_input()
    print_order_details(quantities)
    (apparels_cost, electronics_cost, eatables_cost) = calculate_category_wise_cost(quantities)
    (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost) = calculate_discounted_prices(
        apparels_cost, electronics_cost, eatables_cost)
    (total_cost_including_tax, total_tax) = calculate_tax(discounted_apparels_cost, discounted_electronics_cost,
                                                          discounted_eatables_cost)
    (total_cost_after_coupon_discount, total_coupon_discount) = apply_coupon_code(total_cost_including_tax)
    print()
    print('Thank you for visiting!')
    print()


if __name__ == '__main__':
    main()

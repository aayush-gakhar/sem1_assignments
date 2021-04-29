# Name - Aayush Gakhar
# Roll No - 2020006

"""
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions.

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
"""

# Write the code here for creating an interactive program.

import a2

menu = """
Hello! Welcome to THE RECORDS!
Following queries are available:
-------------------------------------------------
   CODE | DESCRIPTION
-------------------------------------------------
    1   | read_data_from_file
    2   | filter_by_first_name
    3   | filter_by_last_name
    4   | filter_by_full_name
    5   | filter_by_age_range
    6   | count_by_gender
    7   | filter_by_address
    8   | find_alumni
    9   | find_topper_of_each_institute
    10  | find_blood_donors
    11  | get_common_friends
    12  | is_related
    13  | delete_by_id
    14  | add_friend
    15  | remove_friend
    16  | add_education
------------------------------------------------"""
print(menu)
records = []
print('IMPORTANT:Your first input for query should be 1 so that the records file is read!')
print()
while True:
    q = input('Please enter a query code from 1 to 16 as shown above. If you want to exit you may enter -1.: ').strip()
    if q == '':
        print('Please enter something')
        continue
    q = int(q)
    if q == -1:
        break

    if q not in range(1, 17):
        print('Please enter valid inputs only. 1 to 16 or -1.')
        print()
        continue

    if q == 1:
        print('You want to read_data_from_file.')
        records = a2.read_data_from_file()
        print(records)
        print('Data read successfully!')
        continue

    elif q == 2:
        print('You want to filter_by_first_name.')
        s = input('Please enter the first_name you want to find.(STR): ')
        print('list of ids:', a2.filter_by_first_name(records, s))
        continue

    elif q == 3:
        print('You want to filter_by_last_name.')
        s = input('Please enter the last_name you want to find.(STR): ')
        print('list of ids:', a2.filter_by_last_name(records, s))
        continue

    elif q == 4:
        print('You want to filter_by_full_name.')
        s = input('Please enter the full_name you want to find.(STR): ')
        print('list of ids:', a2.filter_by_full_name(records, s))
        continue

    elif q == 5:
        print('You want to filter_by_age_range.')
        m, n = map(int, input('Please enter space separated min_age, max_age(range of age,both are inclusive).(INT): ').split())
        print('list of ids:', a2.filter_by_age_range(records, m, n))
        continue

    elif q == 6:
        print('You want to count_by_gender.')
        print(a2.count_by_gender(records))
        continue

    elif q == 7:
        print('You want to filter_by_address.')
        a = {}
        print('Now input the fields you want to search and leave others blank')

        i = input('house_no(INT): ').strip()
        if i != '':
            a["house_no"] = int(i)

        i = input('block(STR): ').strip()
        if i != '':
            a["block"] = i

        i = input('town(STR): ').strip()
        if i != '':
            a["town"] = i

        i = input('city(STR): ').strip()
        if i != '':
            a["city"] = i

        i = input('state(STR): ').strip()
        if i != '':
            a["state"] = i

        i = input('pincode(INT): ').strip()
        if i != '':
            a["pincode"] = int(i)

        print(a)

        print(a2.filter_by_address(records, a))
        continue

    elif q == 8:
        print('You want to find_alumni.')
        s = input('Please enter the institute_name you want to find.(STR): ')
        print(a2.find_alumni(records, s))
        continue

    elif q == 9:
        print('You want to find_topper_of_each_institute.')
        print(a2.find_topper_of_each_institute(records))
        continue

    elif q == 10:
        print('You want to find_blood_donors.')
        s = input('Please enter the receiver_person_id.(INT): ')
        print(a2.find_blood_donors(records, int(s)))
        continue

    elif q == 11:
        print('You want to get_common_friends.')
        lst = list(map(int, input('Please enter space separated list of ids.: ').split()))
        print(a2.get_common_friends(records, lst))
        continue

    elif q == 12:
        print('You want to find is_related.')
        p1, p2 = map(int, input('Please enter the space separated person_id_1 and person_id_2.: '))
        print(a2.is_related(records, p1, p2))
        continue

    elif q == 13:
        print('You want to delete_by_id.')
        s = input('Please enter the person_id which you want to delete.: ')
        print(a2.delete_by_id(records, int(s)))
        continue

    elif q == 14:
        print('You want to add_friend.')
        p, f = map(int, input('Please enter the space separated person_id and friend_id: ').split())
        print(a2.add_friend(records, p, f))
        continue

    elif q == 15:
        print('You want to remove_friend.')
        p, f = map(int, input('Please enter the space separated person_id and friend_id: ').split())
        print(a2.remove_friend(records, p, f))
        continue

    elif q == 16:
        print('You want to add_education.')
        person_id = int(input('Please enter the person_id which you want to update.: '))
        institute_name = input('Please enter the institute_name.: ')
        ongoing = input('Please enter if ongoing or not(enter True/False).: ').lower() == 'true'
        if ongoing:
            percentage = 0
        else:
            percentage = input('Please enter the percentage.: ').strip()
        percentage = float(percentage)
        print(a2.add_education(records, person_id, institute_name, ongoing, percentage))
        continue

print('Thank you for using our services.')

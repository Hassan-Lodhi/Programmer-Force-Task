print("""
Program to take list of integers From user and then Check it...
""")
# First is taking values from the user to enter in the list.....
int_list = []
count = 0
while count < 10:

    user_input = input("Enter integers to add to the list (separated by spaces), or 'done' to finish: ")
    count += 1
    if user_input == 'done':
        break

    try:
        num_list = [int(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        continue

    int_list.extend(num_list)

print(int_list)

while True:
    index_input = input("Enter an index number to search for in the list, or 'done' to exit: ")
    if index_input == 'done':
        break

    try:
        index = int(index_input)
        if index < 0 or index >= len(int_list):
            print("Index out of range.")
        elif int_list[index] == index:
            print("Index", index, "is already in the list.")
        else:
            int_list[index] = index
            print("Added index", index, "to the list.")
            break
    except ValueError:
        print("Invalid index. Please enter an integer value.")

print("""
2 Methode
Program to take value of integers From user and then add it in the list 
add one value at top and remove value from the bottom ...
""")

# These lines of code entering one value at top and removing value from the bottom if
# the list is greater then 5
print(int_list)

add_val = int(input('Enter value to add in the list? '))
int_list.insert(0, add_val)

print(f'Main list  {int_list}')
print(f' First five values in the list{int_list[:5]}')

print("""
3rd Methode 
Random Number is in the list Check to see if your number in the list or not
""")

search = int(input('Enter value to search '))
found = False

for num in int_list:
    if search == num:
        print('This value already exists in the list.')
        found = True
        break

if not found:
    print('Good job :) :) :)....')

def create_table(rows, cols):
    # Create the multidimensional array
    array = []
    for i in range(rows):
        sub_array = []
        for j in range(cols):
            sub_array.append((i, j))
        array.append(sub_array)

    # Print the table headers
    print("{:<10}".format(''))

    for j in range(cols):
        print("{:<10}".format('col{}'.format(j)), end='')
    print()

    # Print the table rows
    for i in range(rows):
        print("{:<10}".format('row{}'.format(i)), end='')
        for j in range(cols):
            print("{:<10}".format(str(array[i][j])), end='')
        print()

# Example usage
create_table(5, 6)
FILENAME = "sales_log.txt"
# Show menu
def show_menu():
    print('========================================')
    print('       SALES RECORD MANAGEMENT SYSTEM')
    print('========================================')
    print('1. Add Sale Record')
    print('2. View All Records & Summary Statistics')
    print('3. Clear All Sales Data')
    print('4. Exit System')
    print('========================================')

# Select choice
def main():
    while True:
        show_menu()
        choice = input('Select an option 1-4: ')

        if choice == '1':
            add_sale()
        elif choice == '2':
            view_records()
        elif choice == '3':
            clear_data()
        elif choice == '4':
            print('Thank you for using the Sales Record Management System.')
            break
        else:
            print('Invalid input. Choice 1-4.')

# Choice 1
def add_sale():
    try:
        item_name = input('Item Name: ')
        quantity_sold = int(input('Quantity Sold: '))
        price = float(input('Price per unit: '))
        total = item_name * quantity_sold

        with open(FILENAME, 'a') as f: # saves the record to the file
            f.write(f'{item_name}, {quantity_sold}, {price}, {total}')

    except ValueError:
        print('Error: Quantity must be a whole number and Price must be a digit')

# Choice 2
def view_records():
   total_units = 0
   grand_total = 0

    try:
        with open(FILENAME, 'r') as f: # read sales records from the file
            records = f.readlines()

        if not records:
            print('No records found.')
        print('')

    except FileNotFoundError:
        print('No records found.')

    print('========================================')
    print('             SALES RECORDS              ')
    print('========================================')

    for record in records:
         data = record.strip().split(',')
    try:
        item_name = data[0]
        quantity_sold = int(data[1])
        price = float(data[2])
        total = float(data[3])

    except ValueError:
        print('Invalid record found.')

print('Item name:', item_name)
print('Quantity sold:', quantity_sold)
print('Price per unit:', price)
print('Total amount:', total )






    # Choice 3
def clear_data():
    try:
        with open(FILENAME, 'w') as f:
            pass
        print('All records cleared. No records remaining.')

    except FileNotFoundError:
        print('Unable to clear sales records.')

main()
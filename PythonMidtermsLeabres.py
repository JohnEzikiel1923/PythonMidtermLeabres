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

def main():
    while True:
        show_menu()
        choice = input ('Select an option 1-4: ')

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

        with open(FILENAME, "a") as f:
            f.write(f'{item_name}, {quantity_sold}, {price}, {total}')

    except ValueError:
        print('Error: Quantity must be a whole number and Price must be a digit')

def view_records():
    print()
    exit()

def clear_data():
    print()
    exit()
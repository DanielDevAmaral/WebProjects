# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Use an f-string to print the current
# day of the week and the current time.



PRODUCT_INDEX = 0
QUANTITY_INDEX = 1

def main():
    try:    
        dic_requests = {}
        store_name = "Amaral's Store"

        products_dict = read_dictionary("C:\\Users\\Danie\\OneDrive\\Área de Trabalho\\BYUI\\cse111\\Week 9\\products.csv")
        print(f'{store_name}')
        #print(f"All Products: \n {products_dict}")
        print("\nRequested Items:")

        total_itens = 0
        subtotal = 0
        tax_amount = 0.06

        with open("C:\\Users\\Danie\\OneDrive\\Área de Trabalho\\BYUI\\cse111\\Week 9\\request.csv", "rt") as request:
            next(request)
            for requests in request:
                product, quantity = requests.split(",")
                quantity = quantity.strip()
                if product in products_dict:
                    print(f"{products_dict[product][1]}: {quantity} @ {products_dict[product][2]}")
                    price = float(products_dict[product][2]) * int(quantity)
                    total_itens += int(quantity)
                    subtotal += price

                else:
                    print(f"Product not found: {product}")
            sale_tax = (tax_amount * subtotal) + subtotal
            print()
            print(f"Number of itens: {total_itens}")
            print(f"Subtotal: {subtotal:.2f}$")
            print(f"Sales Tax: {sale_tax:.2f}$")
            print(f"Thank you for shopping at the {store_name}")
            print()
            print(f"{current_date_and_time:%A %I:%M %p}")
    except KeyError as ke:
        print('Key Not Found in the Dictionary:', ke)

    except FileNotFoundError as not_found_err:
      # This code will be executed if the user enters
      # the name of a file that doesn't exist.
      print()
      print(type(not_found_err).__name__, not_found_err, sep=": ")
      print(f"The file {products_dict} doesn't exist.")
      print("Run the program again and enter the" \
              " name of an existing file.")


        
    


def read_dictionary(filename):
    dic_products = {}
    with open(filename, "rt") as product:
        next(product)
        for products in product:
            product_id, name, price = products.split(",")
            price = price.strip()
            dic_products[product_id] = [product_id, name, price]
    return dic_products

main()

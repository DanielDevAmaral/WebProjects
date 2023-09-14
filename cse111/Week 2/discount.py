from datetime import datetime


# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Print the day of the week for the user to see.
print(day_of_week)

# Part 1

subtotal = float(input("Please enter the subtotal: "))
tax = float(input("Sales tax amount: "))

# Part 2

if day_of_week == 1 or 2 and subtotal >= 50:

    discount = 0.10 * subtotal
    total = (subtotal + tax) - discount
    print(f'Total: {total:.2f}')

else:

    discount = 0.10 * subtotal
    total = subtotal + tax
    print(f'Total: {total:.2f}')


    

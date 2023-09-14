from datetime import datetime
import math



# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Use an f-string to print only the date
# part of the current date and time.


width = int(input("Enter the width of the tire in mm (ex 205): "))
ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
desireToBuy = input("Do you want to buy a tire with that dimensions (Y = Yes or N = No): ")

volume = math.pi * width**2 * ratio * (width * ratio + 2540 * diameter) / 10000000000

print(f'The approximate volume is {volume:.2f} liters')
if desireToBuy.lower == 'y':
    phone_number = input("Please, enter your Phone number for a future contact about the tire: ")

    


with open("volume.txt", mode="a") as volume_file:

    print(f"{current_date_and_time:%y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}, {phone_number}",file=volume_file)

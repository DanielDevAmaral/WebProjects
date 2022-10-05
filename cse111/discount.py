from calendar import WEDNESDAY
from datetime import datetime



today = datetime.now(tz=None)
week_day = datetime.weekday(today)
week_day = 3


user_subtotal = float(input("Please enter the subtotal: "))

if user_subtotal >= 50 and (week_day == 3 or week_day == 4):
    discout = user_subtotal * 0.10
    taxes = (user_subtotal - discout) * 0.06
    print(f"Sales tax amount: {taxes:.2f}")
    print(f"Discount amount: {discout:.2f}")
    print(f"Total: {taxes + (user_subtotal - discout):.2f}")


else:
  
    taxes = user_subtotal * 0.06

    print(f"Sales tax amount: {taxes}")
    print(f'Total: {taxes + user_subtotal:.2f}')


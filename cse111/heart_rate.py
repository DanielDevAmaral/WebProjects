"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""
# Get the user age
person_age = int(input("How old are you? (Just numbers): "));

# Discovery the maximum heart rate per minute
maximum_heart_beat = 220 - person_age;

# Print the result using ''' to break the text and make the calculations inside of it.
print(f'''When you exercise to strengthen your heart, you should
keep your heart rate between {maximum_heart_beat * 0.65:.0f} and {maximum_heart_beat * 0.85:.0f} beats per minute.''')

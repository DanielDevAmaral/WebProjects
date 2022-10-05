numbers = []
total_numbers = 0

print("Enter a list of numbers, type 0 when finished.\n")

while total_numbers == 0:
    choose_number = int(input("Choose a number: "))
    numbers.append(choose_number)
    if choose_number == 0:
        numbers.remove(0)
        break

numbers.sort()


for drop in numbers:
    print(drop)


print(f"The smallest positive number is: {min([min_positive for min_positive in numbers if min_positive > 0])}")
print(f"The largest number is: {numbers[-1]}")
print(f"The average is: {sum(numbers) / len(numbers)}")
print(f"The sum is: {sum(numbers)}")

for sorted_numbers in numbers:
    print(sorted_numbers)


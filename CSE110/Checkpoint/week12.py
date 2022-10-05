
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
    ]
    
less_age = 130
max_age = 0
less_name = ""
max_name = ""

for a in people:
    separed = a.split(" ")
    name = separed[0]
    age = int(separed[1])

    if less_age > age:
        less_age = age
        less_name = name

    
    elif max_age < age:
        max_age = age
        max_name = name

print(f"{less_age} --- {less_name}")
print(f"{max_age} --- {max_name}")





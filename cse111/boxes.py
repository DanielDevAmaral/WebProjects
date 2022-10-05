import math

manufactured_itens = int(input("Enter the number of items: "));
itens_per_box = int(input("Enter the number of items per box: "));

shipping = math.ceil(manufactured_itens / itens_per_box)

print(f'For {manufactured_itens} items, packing {itens_per_box} items in each box, you will need {shipping} boxes.')



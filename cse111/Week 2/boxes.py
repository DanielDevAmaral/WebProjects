import math

numberItens = int(input("Enter the number of items: "))
numberBoxes = int(input("Enter the number of items per box: "))

boxes = numberItens / numberBoxes

print(f"For {numberItens} itens, packing {numberBoxes} items in each box, you will need {math.ceil(boxes)} boxes.")




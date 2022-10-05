import math
from datetime import datetime

width = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter) / 10000000000

today = datetime.now(tz=None)

with open("volume.txt", mode="at") as volume_file:
    print(f"{today:%y-%m-%d}",file=volume_file)
    print(f"{width}",file=volume_file)
    print(f"{aspect_ratio}",file=volume_file)
    print(f"{diameter}",file=volume_file)
    print(f"{volume:.2f}",file=volume_file)

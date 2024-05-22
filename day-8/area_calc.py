import math

def get_area(height, width):
    return height * width

def cans_required(height, width, coverage):
    area = get_area(height, width)
    return math.ceil(area/coverage)

height = float(input('Enter the height of the wall: '))
width = float(input('Enter the width of the wall: '))
coverage = float(input('How much area a can will paint: '))

cans_needed = cans_required(height, width, coverage)
print(f'Total {cans_needed} to paint the wall.')

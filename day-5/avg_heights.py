heights = input('Enter the heights of the students: ').split(",")

print(heights)

for n in range(len(heights)):
    heights[n] = int(heights[n].strip())

# total_heights = sum(heights)
total_heights = 0
total_items = 0
for height in heights:
    total_heights += height
    total_items += 1

avg_height = total_heights/(total_items * 1.0)  #len(heights)

print(f'Average heights of the students is: {avg_height}')
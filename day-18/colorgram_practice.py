import colorgram


colors = colorgram.extract('rupenzel.jpg', 30)
color_codes = []
for i, color in enumerate(colors):
    r, g, b = colors[i].rgb[0], colors[i].rgb[1], colors[i].rgb[2]
    color_codes.append((r, g, b))

    print(f'RED: {colors[1].rgb.r}')
    print(f'GREEN: {colors[1].rgb.g}')
    print(f'BLUE: {colors[1].rgb.b}')
    print()

print(color_codes)

from PIL import Image, ImageChops, ImageEnhance, ImageDraw

location = 'Z:/github/StackOverFlow/62368936/'
image = Image.open(location + 'source.png')

# contrasting to get (mostly) black & white image
enhancer = ImageEnhance.Contrast(image)
image_contrast = enhancer.enhance(500)


# converting to list
image_array = list(image_contrast.getdata())
w, h = image_contrast.size

pixels = []
for col in range(h):
    pixels.append([image_array.pop() for _ in range(w)])


# find where long white line, assuming it's position outside letter.
target = (255, 255, 255)
threshold = w//2

for idx, row in enumerate(pixels):
    max_length = 0
    starting = 0
    last_pixel = False
    for idx2, col in enumerate(row):
        if max_length >= threshold:
            break
        if col == target:
            if last_pixel:
                max_length += 1
            else:
                last_pixel = True
                starting = idx2
        else:
            max_length = 0
    else:
        continue
    break


fill_point = (idx2 - starting // 2, idx)
ImageDraw.floodfill(image_contrast, fill_point, (100, 100, 100))
compare = Image.new('RGB', (w, h), (100, 100, 100))
output = ImageChops.logical_and(compare, image_contrast)

# not working as intended..

output.save(location + 'new_name.png')

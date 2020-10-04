from PIL import Image, ImageChops

source = Image.open("outline.png")
print(source.mode)
source = source.convert("RGBA")

mask = Image.open("mask.png")
print(mask.mode)
mask = mask.convert("RGBA")

output = ImageChops.multiply(source, mask)
output.save("output.png")

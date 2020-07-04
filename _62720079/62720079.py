import pyautogui
from _62720079 import tool
from PIL import Image
import cv2

loc = 'Z:/github/StackOverFlow/_62720079/'
screen_area = tool.getCaptureArea()
image = Image.open(loc + 'sample.png')

found, result = tool.imageSearch(image, screen_area)
cv2.imwrite('Z:/github/StackOverFlow/_62720079/matched.png', result)

print(f"Selected area: {screen_area.p1}, {screen_area.p2}")
print(f"Image Size: {image.width, image.height}")
print(f"Matched point: {found}")

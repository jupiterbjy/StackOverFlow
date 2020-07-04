import time
import keyboard
import pyautogui
import cv2
from numpy import array, where


class Pos:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __len__(self):
        return 2

    def __mul__(self, other: (int, float)):
        return Pos(int(self.x * other), (self.y * other))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __iter__(self) -> iter:
        return iter((self.x, self.y))

    def __add__(self, other):
        x, y = other  # assuming other is following sequence protocol.
        return Pos(self.x + x, self.y + y)

    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return Pos(abs(self.x), abs(self.y))

    def __ge__(self, other):
        return (self.x >= other.x) & (self.y >= other.y)

    def __le__(self, other):
        return (self.x <= other.x) & (self.y <= other.y)

    def set(self, x=0, y=0):
        self.x, self.y = int(x), int(y)


class Area:
    """
    Sort given 2 coordinates to upper-left, down-right coordinates.
    """

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.p1 = Pos(x1, y1)
        self.p2 = Pos(x2, y2)
        self.sort()

    def __iter__(self):
        return iter((*self.p1, *self.p2))

    def __len__(self):
        return 4

    @classmethod
    def from_pos(cls, p1: Pos, p2: Pos):
        try:
            return cls(*p1, *p2)
        except TypeError:
            raise TypeError(f"'from_pos' only accept 'Pos', got {type(p1), type(p2)}.")

    @property
    def region(self) -> tuple:
        return *self.p1, *abs(self.p1 - self.p2)

    def sort(self):
        if all((self.p1, self.p2)):
            x, y = [sorted(list(i)) for i in zip(self.p1, self.p2)]
            self.p1.set(x[0], y[0])
            self.p2.set(x[1], y[1])

    def set(self, x1=0, y1=0, x2=0, y2=0):
        self.__init__(x1, y1, x2, y2)


def getCaptureArea():
    p1 = Pos()
    p2 = Pos()
    kill_key = "f2"

    def getPos(p):
        while not keyboard.is_pressed(kill_key):
            # fix loop here
            time.sleep(0.05)

        p.set(*pyautogui.position())

        while keyboard.is_pressed(kill_key):
            time.sleep(0.05)

    getPos(p1)
    getPos(p2)

    return Area.from_pos(p1, p2)


def imageSearch(target, area, precision=0.85):

    template = cv2.cvtColor(array(target), cv2.COLOR_RGB2GRAY)

    arr = array(pyautogui.screenshot(region=area))

    img = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_wh = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val < precision:
        return False, img
    else:
        pt2 = tuple(x + y for x, y in zip(img_wh, max_loc))
        cv2.rectangle(img, max_loc, pt2, (0, 0, 255), 2)

        return Pos(*max_loc), img


def scanOccurrence(target, area, precision=0.85, threshold=0.1):

    arr = array(pyautogui.screenshot(region=area))

    img = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    template = cv2.cvtColor(array(target), cv2.COLOR_RGB2GRAY)
    img_wh = Pos(*template.shape[::-1])

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = where(res >= precision)

    count = 0
    found = []
    threshold_pixel = img_wh * threshold

    for pt in sorted(zip(*loc[::-1])):
        try:
            if (
                (found[-1] + img_wh + threshold_pixel)
                >= Pos(*pt)
                >= (found[-1] - threshold_pixel)
            ):
                continue
        except IndexError:  # intentionally causing first run of for loop catch this
            pass

        found.append(Pos(*pt))
        count += 1
        cv2.rectangle(img, pt, Pos(*pt) + img_wh, (0, 0, 255), 2)

    return count, img, found

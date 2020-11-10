from os.path import abspath, dirname
from sys import path

path.append(dirname(abspath(__file__)) + "/..")
import Module


from os import getcwd

print(f"Current script dir: {__file__}")
print(f"Module dir: {Module.__file__}")
print(f"Working dir: {getcwd()}")

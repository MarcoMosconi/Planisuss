import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from erbasts.erbast import Erbast
from keygenerator import generateKey
import random
from constants import MOVE_PROBABILITY, MAX_HERD
from animals.groups import Group

class Pride(Group):
    def __init__(self, cell):
        super().__init__(cell)
    
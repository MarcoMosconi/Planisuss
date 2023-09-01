import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from visualization.visualize import *

def visualizing():
    totalDensity = visualize_V()
    totalNumberErbast = visualize_E()
    totalNumberCarviz = visualize_C()
    return totalDensity, totalNumberErbast, totalNumberCarviz
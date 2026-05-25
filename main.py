import time
from statistics import mean, stdev

import matplotlib.pyplot as plt
import seaborn as sns

from atom import Atom
from xyz_trajectory import XYZ_Trajectory
from hydrogen_bond import HB_Analyzer
from files_translator import Files_Translator

st = time.time()
codes = {"1": "C", "2": "H", "3": "N"}
Files_Translator.dump2xyz("my_file", atoms_codes=codes)

ft = time.time()
print(ft-st)

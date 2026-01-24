import time

import file_translator

st = time.time()
file_path = r"amidines_5.dump"

file_translator.dump2xyz(file_path)
ft = time.time()
print(ft-st)

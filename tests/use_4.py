import time

from files_translator import Files_Translator

st = time.time()
file_path = r"amidines_1.dump"

Files_Translator.dump2xyz(file_path)

ft = time.time()
print(ft-st)

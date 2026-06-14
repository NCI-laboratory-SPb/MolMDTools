import time

from molmdtools.files_translator import Files_Translator

st = time.time()
file_path = r"file.dump"

Files_Translator.dump2xyz(file_path)

ft = time.time()
print(ft-st)

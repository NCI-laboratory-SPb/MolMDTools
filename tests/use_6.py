import time

from files_translator import Files_Translator

st = time.time()

core = ""
files = ["file.dump", "file1.dump", "file2.dump", "file3.dump"]

for file in files:
    Files_Translator.dump2xyz(filename=core+file)

ft = time.time()
print(ft-st)

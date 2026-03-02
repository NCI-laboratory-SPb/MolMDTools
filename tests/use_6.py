import time

from files_translator import Files_Translator

st = time.time()

core = ""
files = ["amidines_2.dump", "amidines_3.dump", "amidines_4.dump", "amidines_5.dump"]

for file in files:
    Files_Translator.dump2xyz(filename=core+file)

ft = time.time()
print(ft-st)

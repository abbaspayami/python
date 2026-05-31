from pathlib import Path

p = Path("docs/1.txt")
# print(p.exists())

# read r, write w, create x, append a
file = open("docs/1.txt", "r")
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.name)

# for line in file:
#     print(line)
file.close()

# print(p.exists())
# print(p.resolve())

# write  first remove the content of file then will be added
# file = open("docs/1.txt", "w")
# file.write("Amir")

#  append just add new element at the end
# file = open("docs/2.txt", "a")
# file.write("\nAmir")

# create new file
# file = open("docs/3.txt", "x")
# file.write("\nAmir")

file.close()

# Another way to work on file without closing the file
my_file = Path("docs/1.txt")
# print(my_file.read_text())
# print(my_file.write_text("That is for test"))

# in order to copy one file to another
target = Path("docs/2.txt")
target.write_text(my_file.read_text())

import shutil
shutil.copy("docs/1.txt", "docs/4.txt")
# path folder files

from pathlib import Path
#
# Path("/user/local/bin")
# Path()

p = Path("/Users/abbas/PycharmProjects/first_app/lesson13/lesson13/path.py")
m = p.exists()
m1 = p.is_dir()
m2 = p.is_file()
m3 = p.name
m4 = p.stem
m5 = p.suffix
m6 = p.absolute()


print(m, m1, m2, m3, m4, m5, m6)
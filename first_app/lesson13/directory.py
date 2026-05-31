from pathlib import Path
import os
from importlib.resources import contents

# p = Path("docs")
# if not p.exists():
#     p.mkdir()
#
# p.rmdir()

os.mkdir("docs")
# os.rmdir("docs")
print(Path.cwd())
content = os.listdir(".")
print(content)
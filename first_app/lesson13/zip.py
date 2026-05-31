from zipfile import ZipFile
from pathlib import Path

# In order to make a zip file
with ZipFile("zip1.zip", "w") as zip_ref:
    for path in Path("docs").rglob("*.*"):
        zip_ref.write(path)

# In order to make it extract
with ZipFile("zip1.zip", "r") as zip_ref:
    print(zip_ref.namelist())
    zip_ref.extractall("extract")
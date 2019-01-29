import os
from pathlib import Path
path ="C:\\12.txt"
e = os.path.exists(path)
print(e)
my_file = Path(r"C:\1.txt")
if my_file.is_file():
    print("--")
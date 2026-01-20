import sys
import os
from pathlib import Path

for arg in sys.argv[1:-1]:
    print("hello , my name is ",arg)

a = [1,2,3,4,5,6]
print(a[1:-1])

print(os.getcwd())
filepath = os.path.join("day7","Student_Result.txt")

path = Path("day7")/"Readme.md"
print(path)
print(filepath)
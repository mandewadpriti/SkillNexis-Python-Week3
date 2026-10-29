def count_lines(filename):
    with open(filename, 'r') as f:
        count = len(f.readlines())
    print(f"Total lines: {count}")

count_lines('sample.txt')
def merge_files(file1, file2, output):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data = f1.read() + "\n" + f2.read()
    with open(output, 'w') as out:
        out.write(data)
    print(f"Merged into {output}")

merge_files('file1.txt', 'file2.txt', 'merged.txt')
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
print(df.describe())
print(df.info())
print(f"Total rows: {len(df)}")
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y, marker='o')
plt.title("Sales Graph")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
import json

data = {"name": "Nanded", "course": "Python", "week": 3}

# Create
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# Read
with open('data.json', 'r') as f:
    loaded = json.load(f)
    print(loaded)

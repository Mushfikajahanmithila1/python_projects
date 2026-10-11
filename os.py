import os 

os.mkdir("data")

if not os.path.exists("data"):
    os.makedirs("data")

for i in range(1, 101):
    os.mkdir(f"data/Day{i}")
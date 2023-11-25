import os

os.chdir("G:\\Python code\\py2")

if (not os.path.exists("data")):
    os.mkdir("data")

for i in range(0, 50):
    if (not os.path.exists(f"data/Day {i}")):
        os.mkdir(f"data/Day {i+1}")
    # os.rename(f"data/Tutorial{i}", f"data/Day {i}")
    # os.removedirs(f"data/Day {i}")
    pass

folders = os.listdir("data")
print(folders)

# for folder in folders:
#     print(folder)

print(os.getcwd())

